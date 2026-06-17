#!/usr/bin/env python3
"""
Script para generar imágenes de Cisneros con Stable Diffusion + ControlNet
Requiere: AUTOMATIC1111 WebUI o Forge con ControlNet instalado

Uso:
    python generate_cisneros_controlnet.py --reference iglesia.jpg --prompt "prompt.txt"
"""

import requests
import base64
import json
import argparse
import os
from pathlib import Path

# Configuración
SD_API_URL = "http://127.0.0.1:7860"  # URL de tu WebUI local
OUTPUT_DIR = "./output"

# Prompt optimizado para Cisneros
CISNEROS_PROMPT = """A premium immersive digital tourism experience poster for Cisneros, Antioquia, Colombia. 
1:1 square composition, photorealistic 8K quality, ultra-sharp detail.

A modern tourism experience center with holographic projections. 
Cyan holograms (#00D9FF), navy blue panels (#1B2A49), gold accents (#FFD700), dark background (#081120).

SEVEN floating holographic panels showing EXACT real landmarks:

PANEL 1 - IGLESIA PARROQUIAL: Distinctive modern church with steep TRIANGULAR A-frame facade, 
asymmetrical design, cream/beige concrete walls, RED CROSS on front center, tall golden spire with CLOCK, 
multiple small rectangular windows, wide concrete staircase. Looks like a ship's bow or tent. 
White/cream with red trim details.

PANEL 2 - ESTACIÓN FERROCARRIL: Historic railway station with LONG wooden platform, 
corrugated metal roof supported by wooden beams, tropical palm trees, vintage railway building 
with large arched openings, weathered wood and metal, rustic authentic Colombian 1920s-1930s station.

PANEL 3 - LOCOMOTORA No. 45: Black vintage steam locomotive with bright YELLOW stripes, 
number '45' visible, classic 1920s Baldwin design, large spoked wheels, red cowcatcher, brass fittings.

PANEL 4 - LOCOMOTORA N° 8: Green boiler with BLACK chassis and red lower details, 
number '8' visible, vintage 1921 steam locomotive, green cylindrical boiler, gold/brass accents.

PANEL 5 - PARQUE LINEAL: Colorful tourist train on tracks through tropical park, 
blue and yellow passenger car, green vegetation, walking paths.

PANEL 6 - BALNEARIOS NATURALES: Crystal clear natural swimming pools, small waterfalls, 
lush tropical forest, pristine turquoise water, Colombian Andes landscape.

PANEL 7 - TRAPICHES PANELEROS: Traditional Colombian sugar cane processing, 
large copper cauldrons with bubbling golden panela, wooden trapiche press, farmers in traditional clothing.

Four diverse tourists in foreground looking fascinated. Cinematic LED lighting, volumetric fog, 
luminous particles, holographic reflections. Title 'Los tesoros turísticos de Cisneros' at top. 
Brand 'Uni2 X Cisneros' at bottom. Contemporary technology style, Apple Store aesthetic."""

NEGATIVE_PROMPT = """blurry text, deformed faces, extra fingers, generic church, generic train station, 
wrong architecture, cartoonish, messy composition, pixelated, watermark, strange logos, bad anatomy, 
oversaturated, amateur, cropped elements, text errors, dark faces, jpeg artifacts, mutation, deformed, 
extra limbs, poorly drawn, ugly, tiling, cloned face, out of frame, overexposed, dated sci-fi, 
cyberpunk, neon overload, cluttered, CRT screens, old technology, traditional European church, 
Gothic cathedral, modern glass church, subway station, metro station, airport, generic locomotive, 
diesel train, electric train"""


def encode_image(image_path):
    """Codifica imagen a base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def check_sd_running():
    """Verifica si Stable Diffusion está corriendo"""
    try:
        response = requests.get(f"{SD_API_URL}/sdapi/v1/samplers", timeout=5)
        return response.status_code == 200
    except:
        return False


def get_controlnet_models():
    """Obtiene modelos de ControlNet disponibles"""
    try:
        response = requests.get(f"{SD_API_URL}/controlnet/model_list", timeout=10)
        if response.status_code == 200:
            return response.json().get("model_list", [])
        return []
    except:
        return []


def generate_with_controlnet(
    prompt,
    negative_prompt,
    reference_image_path,
    control_type="lineart",  # lineart, depth, canny, openpose, ip-adapter
    width=1024,
    height=1024,
    steps=30,
    cfg_scale=7.5,
    seed=-1,
    output_name="cisneros_controlnet"
):
    """
    Genera imagen usando ControlNet con imagen de referencia

    control_type:
        - "lineart": Mantiene líneas y estructura
        - "depth": Mantiene profundidad y perspectiva  
        - "canny": Mantiene bordes y contornos
        - "ip-adapter": Mantiene estilo y contenido (mejor para landmarks)
        - "reference_only": Referencia directa (requiere extensión adicional)
    """

    if not check_sd_running():
        print("❌ Error: Stable Diffusion no está corriendo en", SD_API_URL)
        print("   Inicia AUTOMATIC1111 o Forge con: ./webui.sh --api")
        return None

    # Codificar imagen de referencia
    reference_b64 = encode_image(reference_image_path)

    # Preparar payload
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "seed": seed,
        "sampler_name": "DPM++ 2M Karras",
        "batch_size": 1,
        "n_iter": 1,
        "restore_faces": True,
        "tiling": False,
        "send_images": True,
        "save_images": True,
        "alwayson_scripts": {
            "controlnet": {
                "args": [
                    {
                        "input_image": reference_b64,
                        "module": control_type,  # preprocessor
                        "model": f"control_v11p_sd15_{control_type}" if control_type != "ip-adapter" else "ip-adapter_sd15",
                        "weight": 0.8,  # 0.0-2.0, mayor = más fiel a referencia
                        "resize_mode": "Crop and Resize",
                        "lowvram": False,
                        "processor_res": 512,
                        "threshold_a": 100,
                        "threshold_b": 200,
                        "guidance_start": 0.0,  # Cuándo empieza ControlNet (0.0 = inicio)
                        "guidance_end": 1.0,    # Cuándo termina (1.0 = final)
                        "control_mode": "Balanced",  # Balanced, Prompt Important, ControlNet Important
                        "pixel_perfect": True
                    }
                ]
            }
        }
    }

    # Ajustar según tipo de ControlNet
    if control_type == "ip-adapter":
        # IP-Adapter es mejor para mantener estilo y contenido de landmarks
        payload["alwayson_scripts"]["controlnet"]["args"][0]["model"] = "ip-adapter_sd15_plus"
        payload["alwayson_scripts"]["controlnet"]["args"][0]["weight"] = 0.7
        payload["alwayson_scripts"]["controlnet"]["args"][0]["module"] = "ip-adapter_clip_sd15"
    elif control_type == "reference_only":
        # Reference-only (requiere extensión Reference-only o Inpaint)
        payload["alwayson_scripts"]["controlnet"]["args"][0]["model"] = "reference_only"
        payload["alwayson_scripts"]["controlnet"]["args"][0]["module"] = "reference_only"
        payload["alwayson_scripts"]["controlnet"]["args"][0]["weight"] = 1.0

    print(f"🎨 Generando con ControlNet ({control_type})...")
    print(f"   Referencia: {reference_image_path}")
    print(f"   Dimensiones: {width}x{height}")
    print(f"   Pasos: {steps} | CFG: {cfg_scale}")

    try:
        response = requests.post(
            f"{SD_API_URL}/sdapi/v1/txt2img",
            json=payload,
            timeout=300
        )

        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return None

        result = response.json()

        # Guardar imagen
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for i, img_data in enumerate(result.get("images", [])):
            output_path = os.path.join(OUTPUT_DIR, f"{output_name}_{control_type}_{i}.png")
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(img_data.split(",")[0]))
            print(f"✅ Imagen guardada: {output_path}")

        # Guardar info
        info_path = os.path.join(OUTPUT_DIR, f"{output_name}_{control_type}_info.json")
        with open(info_path, "w") as f:
            json.dump({
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "control_type": control_type,
                "reference_image": reference_image_path,
                "parameters": {
                    "width": width,
                    "height": height,
                    "steps": steps,
                    "cfg_scale": cfg_scale,
                    "seed": result.get("seed", seed)
                }
            }, f, indent=2)

        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def generate_multi_reference(
    prompt,
    negative_prompt,
    reference_images,  # Lista de paths
    weights=None,      # Pesos para cada referencia
    width=1024,
    height=1024,
    output_name="cisneros_multi"
):
    """
    Genera usando múltiples imágenes de referencia con ControlNet
    Útil para combinar: Iglesia + Estación + Locomotora en una sola imagen
    """

    if not weights:
        weights = [0.7] * len(reference_images)

    controlnet_args = []
    for img_path, weight in zip(reference_images, weights):
        controlnet_args.append({
            "input_image": encode_image(img_path),
            "module": "ip-adapter_clip_sd15",
            "model": "ip-adapter_sd15_plus",
            "weight": weight,
            "resize_mode": "Crop and Resize",
            "guidance_start": 0.0,
            "guidance_end": 1.0,
            "control_mode": "Balanced",
            "pixel_perfect": True
        })

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "steps": 35,
        "cfg_scale": 7.5,
        "seed": -1,
        "sampler_name": "DPM++ 2M Karras",
        "alwayson_scripts": {
            "controlnet": {
                "args": controlnet_args
            }
        }
    }

    print(f"🎨 Generando con {len(reference_images)} referencias...")
    for i, (path, w) in enumerate(zip(reference_images, weights)):
        print(f"   Referencia {i+1}: {path} (peso: {w})")

    try:
        response = requests.post(
            f"{SD_API_URL}/sdapi/v1/txt2img",
            json=payload,
            timeout=300
        )

        if response.status_code == 200:
            result = response.json()
            os.makedirs(OUTPUT_DIR, exist_ok=True)

            for i, img_data in enumerate(result.get("images", [])):
                output_path = os.path.join(OUTPUT_DIR, f"{output_name}_multi_{i}.png")
                with open(output_path, "wb") as f:
                    f.write(base64.b64decode(img_data.split(",")[0]))
                print(f"✅ Imagen guardada: {output_path}")

            return result
        else:
            print(f"❌ Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Generador de imágenes Cisneros con ControlNet")
    parser.add_argument("--reference", "-r", help="Imagen de referencia (para ControlNet)")
    parser.add_argument("--references", "-R", nargs="+", help="Múltiples imágenes de referencia")
    parser.add_argument("--prompt", "-p", help="Archivo con prompt personalizado")
    parser.add_argument("--control-type", "-c", default="ip-adapter",
                       choices=["lineart", "depth", "canny", "openpose", "ip-adapter", "reference_only"],
                       help="Tipo de ControlNet")
    parser.add_argument("--width", "-W", type=int, default=1024)
    parser.add_argument("--height", "-H", type=int, default=1024)
    parser.add_argument("--steps", "-s", type=int, default=30)
    parser.add_argument("--cfg", type=float, default=7.5)
    parser.add_argument("--seed", type=int, default=-1)
    parser.add_argument("--output", "-o", default="cisneros")
    parser.add_argument("--list-models", action="store_true", help="Listar modelos ControlNet disponibles")

    args = parser.parse_args()

    # Listar modelos
    if args.list_models:
        models = get_controlnet_models()
        print("📋 Modelos ControlNet disponibles:")
        for m in models:
            print(f"   - {m}")
        return

    # Verificar SD
    if not check_sd_running():
        print("❌ Stable Diffusion no está corriendo")
        print("   Inicia con: ./webui.sh --api")
        return

    # Cargar prompt personalizado si existe
    prompt = CISNEROS_PROMPT
    if args.prompt and os.path.exists(args.prompt):
        with open(args.prompt, "r") as f:
            prompt = f.read()

    # Generar
    if args.references:
        # Múltiples referencias
        weights = [0.8, 0.6, 0.5][:len(args.references)]  # Pesos decrecientes
        generate_multi_reference(
            prompt=prompt,
            negative_prompt=NEGATIVE_PROMPT,
            reference_images=args.references,
            weights=weights,
            width=args.width,
            height=args.height,
            output_name=args.output
        )
    elif args.reference:
        # Una referencia
        generate_with_controlnet(
            prompt=prompt,
            negative_prompt=NEGATIVE_PROMPT,
            reference_image_path=args.reference,
            control_type=args.control_type,
            width=args.width,
            height=args.height,
            steps=args.steps,
            cfg_scale=args.cfg,
            seed=args.seed,
            output_name=args.output
        )
    else:
        # Sin referencia (texto puro)
        print("⚠️ No se proporcionó imagen de referencia")
        print("   Usa --reference para ControlNet o --references para múltiples")
        print("
📖 Ejemplos:")
        print("   python generate_cisneros.py -r iglesia_cisneros.jpg -c ip-adapter")
        print("   python generate_cisneros.py -R iglesia.jpg estacion.jpg locomotora.jpg")
        print("   python generate_cisneros.py -r estacion.jpg -c depth -W 1024 -H 1024")


if __name__ == "__main__":
    main()
