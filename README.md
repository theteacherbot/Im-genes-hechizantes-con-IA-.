# 🎨 Generador de Imágenes - Cisneros Turismo

> **App generadora de imágenes con IA** para promocionar los tesoros turísticos de Cisneros, Antioquia, Colombia.
> 
> Desarrollado por **Uni2 X Cisneros** | *"Historia, cultura y naturaleza para el mundo"*

![Version](https://img.shields.io/badge/version-1.0.0-00D9FF?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-FFD700?style=flat-square)
![Tech](https://img.shields.io/badge/tech-HTML%2FCSS%2FJS-1B2A49?style=flat-square)

---

## 📸 Vista previa

```
┌─────────────────────────────────────────────────────────────┐
│  [Panel de Controles]              │  [Canvas 1:1]           │
│  ┌─────────────────────────────┐  │  ┌─────────────────┐   │
│  │ 🔑 API Key                  │  │  │                 │   │
│  │ Modo: Texto/Imagen          │  │  │   Imagen        │   │
│  │ Presets                     │  │  │   Generada      │   │
│  │ Estilo Artístico            │  │  │                 │   │
│  │ Animal/Elemento             │  │  │   1024x1024     │   │
│  │ Modelo de IA                │  │  │                 │   │
│  │ Prompt editable (JSON)      │  │  └─────────────────┘   │
│  │ [✨ Generar] [⬇️ Descargar]│  │                         │
│  └─────────────────────────────┘  │                         │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| 🎨 **8 estilos artísticos** | Fantasía cinematográfica, acuarela, surrealismo, cyberpunk, realismo mágico, óleo, anime, papel recortado |
| 🤖 **10 modelos de IA** | Flux, ZImage, Klein, Grok-Imagine, Nanobanana, GPTImage, GPTImage-Large, Wan-Image, Qwen-Image, GPT-Image-2 |
| 🖼️ **Image-to-Image** | Sube hasta 5 imágenes de referencia para mayor fidelidad |
| ⚖️ **Peso ajustable** | Controla la influencia de las imágenes de referencia (0-100%) |
| 🔑 **API Key visible** | Campo de API Key en el panel izquierdo con guardado en localStorage |
| 📋 **Presets** | Cartel Cisneros (optimizado) y modo Personalizado |
| 📝 **Prompt editable** | Estructura JSON completa editable en tiempo real |
| 🖥️ **Canvas 1:1** | Lienzo cuadrado para visualización de resultados |
| 📱 **Responsive** | Funciona en desktop, tablet y móvil |
| ⬇️ **Descarga directa** | Guarda la imagen generada con un clic |

---

## 🚀 Demo en vivo

Abre el archivo `index.html` en cualquier navegador moderno:

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

Luego visita: `http://localhost:8000`

---

## 📁 Estructura del proyecto

```
📦 cisneros-image-generator/
├── 📄 index.html              # App principal (HTML/CSS/JS)
├── 📄 README.md               # Este archivo
├── 📄 README_BYOP.md          # Guía de configuración API
├── 📄 GUIA_MIDJOURNEY.md      # Guía para Midjourney
├── 📄 generate_cisneros_controlnet.py  # Script SD + ControlNet
└── 📁 output/                 # Imágenes generadas (se crea automáticamente)
```

---

## 🔧 Configuración

### 1. API Key de Pollinations

Ingresa tu API Key en el campo correspondiente del panel izquierdo:

```
🔑 API Key de Pollinations
[________________________] [👁️ Ver]
✓ API Key guardada en localStorage
```

La clave se guarda automáticamente en `localStorage` del navegador.

### 2. Alternativa: Variable de entorno

```bash
export POLLINATIONS_API_KEY="tu-api-key-aqui"
```

---

## 🎨 Estilos disponibles

| Estilo | Descripción ideal |
|--------|-------------------|
| 🎬 Fantasía Cinematográfica | Escenas épicas, iluminación dramática |
| 🖌️ Acuarela Artística | Trazos suaves, colores difuminados |
| 🌀 Surrealismo | Elementos oníricos, imposibles |
| 🤖 Arte Cyberpunk | Neón, futurismo distópico |
| ✨ Realismo Mágico | Realidad con toques fantásticos |
| 🎨 Pintura al Óleo | Textura clásica, colores ricos |
| 🇯🇵 Anime Detallado | Estilo japonés, líneas definidas |
| ✂️ Arte de Papel Recortado | Capas, sombras, textura papel |

---

## 🤖 Modelos de IA

| Modelo | Características |
|--------|-----------------|
| **Flux** | Por defecto, alta calidad general |
| **ZImage** | Estilizado, artístico |
| **Klein** | Experimental |
| **Grok-Imagine** | Interpretación creativa |
| **Nanobanana** | Artístico, colorido |
| **GPTImage** | Balance calidad/velocidad |
| **GPTImage-Large** | Máxima calidad |
| **Wan-Image** | Detalle fotográfico |
| **Qwen-Image** | Comprensión semántica |
| **GPT-Image-2** | Última generación |

---

## 🖼️ Modos de generación

### Modo Texto a Imagen (Text-to-Image)
Genera imágenes desde cero usando solo descripciones textuales.

```
Prompt: "A futuristic tourism center with holographic displays..."
→ Imagen generada
```

### Modo Imagen a Imagen (Image-to-Image)
Usa fotos de referencia para guiar la generación. **Ideal para landmarks reales.**

```
[📷 Iglesia Cisneros.jpg]     [📷 Estación.jpg]
[📷 Locomotora 45.jpg]        [📷 Locomotora 8.jpg]
         ↓
    Peso: 70%
         ↓
    [🖼️ Imagen generada fiel a las referencias]
```

**Consejo:** Sube fotos reales de los landmarks para máxima fidelidad.

---

## 🎯 Prompt optimizado para Cisneros

El preset incluye descripciones **ultra-específicas** de los landmarks:

### ⛪ Iglesia Parroquial de Cisneros
> *"Fachada triangular en A, diseño asimétrico único, color crema/beige, cruz roja frontal, aguja dorada con reloj en la cima, parece la proa de un barco"*

### 🚉 Estación del Ferrocarril
> *"Andén largo de madera, techo de metal corrugado con vigas de madera, palmeras tropicales, materiales desgastados, estación auténtica colombiana años 1920-1930"*

### 🚂 Locomotora No. 45
> *"Negra con rayas amarillas brillantes, número '45' visible, diseño Baldwin 1920s, ruedas grandes con radios, parachoques rojo"*

### 🚂 Locomotora N° 8
> *"Caldera verde, chasis negro, detalles rojos inferiores, número '8' visible, diseño 1921, accesorios dorados/latón"*

---

## 🛠️ Uso avanzado

### Personalizar el prompt JSON

```json
{
  "prompt": "Tu descripción detallada aquí...",
  "negative prompt": "Elementos a evitar...",
  "style": "realismo mágico",
  "lighting": "dramatic rim lighting at dusk",
  "mood": "epic, powerful",
  "color_palette": ["Deep silver", "midnight blue", "forest green", "amber glow"],
  "artista_references": ["Greg Rutkowski"]
}
```

### Cambiar el tema (no solo Cisneros)

1. Selecciona **"Personalizado"**
2. Borra el prompt
3. Escribe tu propio prompt
4. ¡Genera cualquier cosa!

---

## 🐍 Script adicional: Stable Diffusion + ControlNet

Para máxima fidelidad a landmarks reales, usa el script Python incluido:

```bash
# Requisitos: AUTOMATIC1111 o Forge con ControlNet
pip install requests

# Una referencia
python generate_cisneros_controlnet.py -r iglesia_cisneros.jpg -c ip-adapter

# Múltiples referencias
python generate_cisneros_controlnet.py -R iglesia.jpg estacion.jpg locomotora.jpg

# Con parámetros
python generate_cisneros_controlnet.py -r estacion.jpg -c depth -W 1024 -H 1024 -s 50
```

### Tipos de ControlNet disponibles

| Tipo | Uso ideal |
|------|-----------|
| `ip-adapter` | **Recomendado** - Mantiene estilo y contenido |
| `lineart` | Mantiene líneas y estructura |
| `depth` | Mantiene profundidad y perspectiva |
| `canny` | Mantiene bordes y contornos |
| `reference_only` | Referencia directa máxima |

---

## 🎨 Guía Midjourney

Incluida en `GUIA_MIDJOURNEY_CISNEROS.md`:

- Image Prompts (`[URL] prompt --iw 2`)
- Style Reference (`--sref URL --sw 100`)
- Character Reference (`--cref URL --cw 100`)
- Prompt optimizado listo para copiar

---

## 🌐 API utilizada

**Pollinations AI** - Generación de imágenes gratuita y de código abierto

```
POST https://gen.pollinations.ai/v1/images/generations
```

### Parámetros del body

```json
{
  "prompt": "...",
  "model": "flux",
  "n": 1,
  "size": "1024x1024",
  "quality": "medium",
  "response_format": "b64_json",
  "user": "cisneros-app",
  "image": "",        // Para image-to-image
  "safe": ""
}
```

---

## 📱 Responsive

| Dispositivo | Layout |
|-------------|--------|
| **Desktop (>900px)** | Panel izquierdo + Canvas derecho |
| **Tablet/Móvil (<900px)** | Paneles apilados verticalmente |

---

## 🎨 Paleta de colores

| Color | Hex | Uso |
|-------|-----|-----|
| Cyan | `#00D9FF` | Primario, acentos, hologramas |
| Navy | `#1B2A49` | Secundario, paneles |
| Gold | `#FFD700` | Acento, CTAs, highlights |
| Dark | `#081120` | Fondo principal |

---

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcion`)
3. Commit (`git commit -am 'Añadir nueva función'`)
4. Push (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

---

## 📄 Licencia

MIT License - Uni2 X Cisneros

```
Copyright (c) 2026 Uni2 X Cisneros

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Créditos

- **Desarrollo:** Uni2 X Cisneros
- **IA:** Pollinations AI
- **Fuentes:** Montserrat, Poppins, Inter (Google Fonts)
- **Inspiración:** Los tesoros turísticos de Cisneros, Antioquia

---

## 📞 Contacto

Para soporte o sugerencias:
- 🌐 Web: [Uni2 X Cisneros]
- 📧 Email: [contacto]
- 🐦 Twitter: [@Uni2Cisneros]

---

> *"Cisneros conecta su historia con el presente."* 🚂✨

---

<p align="center">
  <img src="https://img.shields.io/badge/Hecho%20con%20❤️%20en-Cisneros%2C%20Antioquia-00D9FF?style=for-the-badge" alt="Hecho en Cisneros">
</p>
