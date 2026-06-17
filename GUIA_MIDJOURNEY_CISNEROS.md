# Guía Midjourney - Referencias de Imagen para Cisneros

## 🎯 Concepto clave: Image Prompts + Style References

Midjourney permite usar imágenes como referencia directa en el prompt, lo que garantiza fidelidad a landmarks reales.

---

## 📋 Métodos disponibles en Midjourney

### 1. Image Prompts (IP) - Referencia directa

**Sintaxis:**
```
[URL imagen 1] [URL imagen 2] [URL imagen 3] tu prompt descriptivo --ar 1:1 --v 6
```

**Ejemplo para Cisneros:**
```
https://upload.wikimedia.org/wikipedia/commons/c/cc/Iglesia_Cisneros.jpg 
https://example.com/estacion_cisneros.jpg 
https://example.com/locomotora_45.jpg 
A premium immersive digital tourism experience poster for Cisneros, Colombia. 
Modern holographic display center, cyan and gold holograms, seven floating panels 
showing the EXACT landmarks from the reference images. Four diverse tourists in awe. 
Cinematic lighting, photorealistic 8K --ar 1:1 --v 6.1 --s 250 --q 2
```

**Peso de la imagen:**
```
[URL imagen]::2 tu prompt::1   # Imagen pesa 2x más que el texto
```

---

### 2. Style Reference (SREF) - Referencia de estilo

**Sintaxis:**
```
--sref [URL imagen de estilo]
```

**Ejemplo:**
```
/imagine prompt: A futuristic tourism poster for Cisneros... 
--sref https://example.com/estilo_apple_keynote.jpg 
--sw 100  # Style weight: 0-1000
```

---

### 3. Character Reference (CREF) - Para personas consistentes

**Sintaxis:**
```
--cref [URL persona] --cw 0-100
```

---

### 4. Combinación óptima para Cisneros

```
[URL Iglesia Cisneros]::1.5 [URL Estación]::1.5 [URL Locomotora 45]::1.2 
[URL Locomotora 8]::1.2 [URL Trapiche]::1.0 [URL Balneario]::1.0

A premium immersive digital tourism experience poster. Seven holographic floating 
panels in a modern Apple Store-style experience center. Each panel shows the EXACT 
landmark from the reference images above: triangular cream church with red cross 
and golden clock spire, rustic wooden railway station with corrugated metal roof, 
black locomotive 45 with yellow stripes, green locomotive 8 with black chassis, 
traditional panela processing with copper cauldrons, crystal clear natural pools. 

Cyan holograms (#00D9FF), navy panels (#1B2A49), gold accents (#FFD700). 
Four diverse tourists: young Asian man, American adult, Russian woman, African woman, 
all expressing fascination. Title "Los tesoros turísticos de Cisneros" at top. 
Brand "Uni2 X Cisneros" at bottom. Cinematic volumetric lighting, photorealistic, 
8K detail, contemporary technology aesthetic --ar 1:1 --v 6.1 --s 750 --q 2 --no blurry text, 
deformed faces, generic church, generic station, cartoonish, low quality
```

---

## 🔧 Parámetros clave para Midjourney

| Parámetro | Valor recomendado | Descripción |
|-----------|-------------------|-------------|
| `--ar 1:1` | Obligatorio | Relación de aspecto cuadrada |
| `--v 6.1` | Recomendado | Versión más reciente, mejor comprensión |
| `--s 250-750` | 500 | Stylize: creatividad vs fidelidad al prompt |
| `--q 2` | 2 | Calidad máxima |
| `--no` | Lista larga | Elementos a excluir |
| `--iw 2` | 1.5-2 | Image weight: peso de las imágenes de referencia |
| `--sw 100` | 50-100 | Style weight: peso del estilo de referencia |
| `--tile` | No usar | Para patrones repetitivos |
| `--seed` | Tu número | Para reproducibilidad |

---

## 📸 URLs de referencia recomendadas

### Imágenes reales de Cisneros (subir a Discord/imgur primero):

```
# Iglesia Parroquial (fachada triangular)
https://i.imgur.com/TU_IGLESIA_CISNEROS.jpg

# Estación del Ferrocarril (andén de madera)
https://i.imgur.com/TU_ESTACION_CISNEROS.jpg

# Locomotora 45 (negra con amarillo)
https://i.imgur.com/TU_LOCO45_CISNEROS.jpg

# Locomotora N° 8 (verde y negra)
https://i.imgur.com/TU_LOCO8_CISNEROS.jpg

# Trapiche Panelero (calderas de cobre)
https://i.imgur.com/TU_TRAPICHE_CISNEROS.jpg

# Balnearios Naturales (piscinas cristalinas)
https://i.imgur.com/TU_BALNEARIO_CISNEROS.jpg
```

> ⚠️ **Importante:** Midjourney solo acepta URLs públicas. Sube tus fotos a:
> - Imgur
> - Discord (copiar link de imagen)
> - Cloudinary
> - Tu propio hosting

---

## 🎨 Prompt optimizado para Midjourney v6.1

```
[URL1] [URL2] [URL3] [URL4] [URL5] [URL6]

A premium immersive digital tourism experience poster for Cisneros, Antioquia, Colombia. 
Modern Apple Store-style experience center with holographic projections. Seven floating 
holographic panels, each displaying the EXACT landmark from the reference images above:

1. TRIANGULAR cream church with RED CROSS, golden clock spire, asymmetrical A-frame facade
2. Rustic wooden railway station with corrugated metal roof, tropical palm trees, 1920s Colombian
3. Black steam locomotive #45 with bright YELLOW stripes, Baldwin 1920s design
4. Green steam locomotive #8 with black chassis, red details, 1921 design
5. Colorful tourist train in linear park, blue and yellow car, tropical vegetation
6. Crystal clear natural swimming pools, waterfalls, Colombian Andes forest
7. Traditional sugar cane mills, copper cauldrons with golden panela, wooden trapiche

Cyan holograms (#00D9FF), navy panels (#1B2A49), gold accents (#FFD700). 
Four diverse tourists in foreground: young Asian man, American adult, Russian woman, 
African woman, expressing awe and cultural pride. Cinematic volumetric lighting, 
LED glow, luminous particles, photorealistic 8K, contemporary technology aesthetic, 
NOT dated sci-fi. Title "Los tesoros turísticos de Cisneros" at top. 
Brand "Uni2 X Cisneros" with slogan at bottom --ar 1:1 --v 6.1 --s 500 --q 2 
--iw 1.5 --no blurry text, deformed faces, generic church, generic station, 
cartoonish, low quality, pixelated, watermark, Gothic cathedral, modern glass church, 
subway station, diesel train, electric train, CRT screens, 1980s aesthetic
```

---

## 🔄 Workflow recomendado

### Paso 1: Preparar imágenes de referencia
1. Sube 5-6 fotos reales de Cisneros a Imgur/Discord
2. Copia las URLs directas (terminan en .jpg o .png)

### Paso 2: Generar imagen base
```
[URLs] prompt básico --ar 1:1 --v 6.1 --iw 2 --s 250
```

### Paso 3: Refinar con variaciones
```
V1 (Variación sutil) o V2 (Variación fuerte)
```

### Paso 4: Upscale final
```
U1, U2, U3, U4 (según la mejor variación)
```

### Paso 5: Ajustar con Remix
```
/settings → Remix Mode ON
```

---

## 💡 Trucos avanzados

### 1. Múltiples pesos de imagen
```
[URL iglesia]::2 [URL estación]::2 [URL locomotora]::1.5 prompt... --iw 1
```

### 2. Referencia de estilo separada
```
prompt... --sref https://apple-keynote-style.jpg --sw 200
```

### 3. Regiones específicas (Inpainting)
```
Vary (Region) → selecciona área → ajusta prompt
```

### 4. Panorámico para más paneles
```
--ar 16:9  # Para mostrar más paneles holográficos
```

---

## 🛠️ Herramientas complementarias

| Herramienta | Uso | URL |
|-------------|-----|-----|
| **Midjourney** | Generación principal | discord.com |
| **InsightFace** | Consistencia de rostros | discord.gg/insightface |
| **Panolapse** | Animación de paneles | panolapse.com |
| **Leonardo AI** | Alternativa con ControlNet | leonardo.ai |
| **Fooocus** | Stable Diffusion simplificado | fooocus.com |

---

## 📚 Recursos

- **Midjourney Docs:** docs.midjourney.com
- **Prompting Guide:** promptingguide.ai
- **Community Showcase:** midjourney.com/showcase
- **Cisneros Referencias:** Las imágenes de búsqueda que encontramos anteriormente

---

## ⚡ Ejemplo completo listo para copiar

```
https://i.imgur.com/iglesia_cisneros_frontal.jpg 
https://i.imgur.com/estacion_cisneros_anden.jpg 
https://i.imgur.com/loco45_cisneros.jpg 
https://i.imgur.com/loco8_cisneros.jpg 
https://i.imgur.com/trapiche_cisneros.jpg 
https://i.imgur.com/balneario_cisneros.jpg 

A premium immersive digital tourism experience poster for Cisneros, Antioquia, Colombia. 
Modern Apple Store-style experience center with holographic projections. Seven floating 
holographic panels display the EXACT landmarks from the reference images. Cyan holograms, 
navy panels, gold accents. Four diverse tourists in awe. Cinematic lighting, 
photorealistic 8K. Title "Los tesoros turísticos de Cisneros". Brand "Uni2 X Cisneros" 
--ar 1:1 --v 6.1 --s 500 --q 2 --iw 1.5 --no blurry text, deformed faces, generic church, 
generic station, cartoonish, low quality
```

> Reemplaza las URLs de imgur con las URLs reales de tus fotos de Cisneros.
