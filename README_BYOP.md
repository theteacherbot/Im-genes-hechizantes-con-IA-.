# README_BYOP - Bring Your Own Prompt

## Configuración de API Key

Para usar esta aplicación con la API de Pollinations, necesitas configurar tu API key.

### Método 1: LocalStorage (Recomendado para desarrollo)

Abre la consola del navegador (F12) y ejecuta:

```javascript
localStorage.setItem('POLLINATIONS_API_KEY', 'tu-api-key-aqui');
```

### Método 2: Variable de entorno (Para producción)

Crea un archivo `.env` en la raíz del proyecto:

```
POLLINATIONS_API_KEY=tu-api-key-aqui
```

### Método 3: Configuración manual en código

Edita el archivo `index.html` y reemplaza la línea:

```javascript
const API_KEY = localStorage.getItem('POLLINATIONS_API_KEY') || '';
```

Por:

```javascript
const API_KEY = 'tu-api-key-aqui';
```

⚠️ **NO compartas tu API key en repositorios públicos.**

---

## Modos de Generación

### 1. Texto a Imagen (Text-to-Image)

Genera imágenes desde cero usando solo el prompt descriptivo.

**Uso:**
1. Selecciona modo "Texto a Imagen"
2. Elige estilo, animal y modelo
3. Edita el prompt si deseas
4. Haz clic en "Generar Imagen"

### 2. Imagen a Imagen (Image-to-Image)

Genera imágenes usando fotos de referencia como guía visual. **Ideal para obtener resultados fieles a landmarks reales.**

**Uso:**
1. Selecciona modo "Imagen a Imagen"
2. Arrastra o haz clic para subir hasta 5 imágenes de referencia
   - Recomendado: Iglesia de Cisneros, Estación del Ferrocarril, Locomotoras, etc.
3. Ajusta el "Peso de la referencia" (0-100%)
   - 70% = buen balance entre fidelidad y creatividad
   - 90%+ = muy fiel a las referencias
   - 30% = inspiración leve
4. Elige estilo y modelo
5. Haz clic en "Generar Imagen"

---

## Estructura del Prompt

El prompt sigue esta estructura JSON:

```json
{
  "prompt": "Descripción detallada de la imagen...",
  "negative prompt": "Elementos a evitar...",
  "style": "[estilo seleccionado]",
  "lighting": "dramatic rim lighting at dusk",
  "mood": "epic, powerful",
  "color_palette": ["Deep silver", "midnight blue", "forest green", "amber glow"],
  "artista_references": ["[pintor]"]
}
```

### Prompt optimizado para Cisneros

El prompt incluye descripciones **extremadamente específicas** de los landmarks reales:

**Iglesia Parroquial de Cisneros:**
- Fachada triangular en forma de A (A-frame)
- Diseño asimétrico único
- Color crema/beige con cruz roja frontal
- Aguja dorada con reloj en la cima
- Parece la proa de un barco o una tienda de campaña
- Escaleras de concreto amplias

**Estación del Ferrocarril:**
- Andén largo de madera
- Techo de metal corrugado con vigas de madera
- Vegetación tropical y palmeras
- Edificio vintage con arcos grandes
- Materiales de madera y metal desgastados
- Estación auténtica colombiana de los años 1920-1930

**Locomotoras:**
- No. 45: Negra con rayas amarillas/doradas, diseño Baldwin 1920s
- N° 8: Caldera verde, chasis negro, detalles rojos, diseño 1921

---

## Modelos disponibles

- `flux` - Modelo por defecto, alta calidad
- `zimage` - Modelo alternativo
- `klein` - Modelo experimental
- `grok-imagine` - Modelo Grok
- `nanobanana` - Modelo artístico
- `gptimage` - Modelo GPT
- `gptimage-large` - Modelo GPT grande
- `wan-image` - Modelo Wan
- `qwen-image` - Modelo Qwen
- `gpt-image-2` - Modelo GPT-2

## Estilos disponibles

- Fantasía Cinematográfica
- Acuarela Artística
- Surrealismo
- Arte Cyberpunk
- Realismo Mágico
- Pintura al Óleo
- Anime Detallado
- Arte de Papel Recortado

---

## Uso de la API

### Endpoint

```
POST https://gen.pollinations.ai/v1/images/generations
```

### Headers

```
Content-Type: application/json
Authorization: Bearer {API_KEY}
```

### Body - Texto a Imagen

```json
{
  "prompt": "...",
  "model": "flux",
  "n": 1,
  "size": "1024x1024",
  "quality": "medium",
  "response_format": "b64_json",
  "user": "",
  "image": "",
  "safe": ""
}
```

### Body - Imagen a Imagen

```json
{
  "prompt": "...",
  "model": "flux",
  "n": 1,
  "size": "1024x1024",
  "quality": "medium",
  "response_format": "b64_json",
  "user": "cisneros-app",
  "image": "data:image/png;base64,...",
  "image_weight": 0.7,
  "additional_images": ["data:image/png;base64,..."],
  "safe": ""
}
```

### Respuesta

La API devuelve la imagen en formato base64:

```json
{
  "data": [
    {
      "b64_json": "...base64..."
    }
  ]
}
```

---

## Fallback

Si no hay API key configurada, la app usa la URL de generación directa:

```
https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024
```

---

## Consejos para mejores resultados

### Para landmarks fieles a la realidad:

1. **Usa Image-to-Image** con fotos reales de referencia
2. **Sube múltiples ángulos** del mismo lugar (frente, lateral, detalles)
3. **Ajusta el peso** según necesidad:
   - 70-80% = Fiel pero con estilo artístico
   - 90%+ = Réplica casi exacta
4. **Describe detalles únicos** en el prompt (colores exactos, materiales, formas)

### Fotos de referencia recomendadas:

- **Iglesia:** Foto frontal mostrando forma triangular y cruz roja
- **Estación:** Foto del andén con techo de metal y vigas de madera
- **Locomotoras:** Fotos de perfil mostrando números y colores
- **Trapiches:** Fotos del proceso de panela con calderas de cobre

---

## Desarrollo local

Para ejecutar la app localmente:

```bash
# Con Python
python -m http.server 8000

# Con Node.js
npx serve .

# Con PHP
php -S localhost:8000
```

Luego abre: http://localhost:8000

---

## Licencia

MIT License - Uni2 X Cisneros
