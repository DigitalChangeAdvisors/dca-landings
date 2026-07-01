# Landings DCA — Arquitectura y Estado

> Las reglas de marca, sistema visual, tono, skills y flujo de producción están en `../CLAUDE.md` (raíz del workspace). Este archivo contiene solo lo específico de las landing pages comerciales.

## ⚠️ Gate Obligatorio — Pre-audit ANTES de implementar (canónico 2026-06-05)

TODA implementación, ajuste fino o nueva landing — incluyendo iteraciones sobre las 11 landings existentes — debe pasar por auditoría de dos skills **ANTES** de escribir código:

1. `/behavioral-economics-c-level` — valida que el mecanismo BE es correcto para el arquetipo y la etapa del visitante
2. `/ui-ux-pro-max` — valida que el patrón de interacción, layout y motion son apropiados para C-Level

**Sin dictamen de ambas skills, no hay implementación.**

Incidente que motivó la regla: S2 /returnai scrollytelling de 260vh — trampa UX de alta gravedad implementada sin audit previo (2026-06-05).

## Arquitectura de CTAs en Landing Pages — Canónico (2026-06-09)

Toda landing page de DCA debe tener exactamente **3 CTAs** que apunten a la misma URL del instrumento:

| Posición | Elemento | Comportamiento |
|----------|----------|----------------|
| 1 | Header sticky | Siempre visible durante el scroll — acceso inmediato para visitante listo |
| 2 | Hero (primer pantallazo) | Sin scroll requerido — captura al visitante con intención alta |
| 3 | Bloque CTA final (fondo carbón) | Cierre de conversión para visitante que necesitó contexto completo |

**Regla crítica:** Los CTAs 1 y 2 (header + hero) deben apuntar **directamente a la URL del instrumento**, NO a un anchor `#id` que haga scroll. El anchor de sección solo se usa para navegación interna sin intención de conversión.

**Anti-patrón detectado (2026-06-09):** Header y hero con `href="#iniciar"` — esto hace scroll hasta el bloque CTA en lugar de llevar al test directamente. Visitante con intención alta tiene que bajar hasta el final de la página para acceder al test. Se corrigió en ART landing.

**URL canónica del AI Return Test:** `https://tally.so/r/Np6e5W` — Tally form, `target="_blank" rel="noopener"` en todos los CTAs.

**Rationale BE:** El visitante C-Level que llega desde LinkedIn o referido ya está en etapa de acción — no necesita leer 10 bloques para hacer clic. El visitor de intención media scrollea de todas formas y llega al bloque CTA final. Los 3 CTAs capturan ambos arquetipos sin fricción.

---

## Principios de Diseño para Landings

- **Un solo CTA por landing** — la landing no informa, convierte.
- **Sin menú de navegación completo** — solo logo + botón CTA o flujo de captura.
- **Coherencia visual total** con el website: mismas fuentes, misma paleta, mismo motion system.
- **Progressive disclosure:** problema → metodología → evidencia → CTA. En ese orden exacto.
- **Archivo HTML autocontenido** — CSS embebido en `<style>` dentro del `<head>`.

## Escalera de Valor ReturnAI

| Nivel | Producto | Precio | Objetivo de Conversión |
|-------|----------|--------|------------------------|
| 1 | AI Return Test (ART) | Gratuito | C-Level completa test, deja contacto, agenda asesoría |
| 2 | Novela ReturnAI | $19.97 ebook / $29.97 impreso | C-Level compra, se convierte en lead calificado |
| 3 | AI Return Assessment (ARA) | $5,000 | C-Level agenda llamada de diagnóstico |

## Inventario de Landings

| Nombre | Archivo | Objetivo | Estado |
|--------|---------|----------|--------|
| AI Return Test | `art/index.html` | Captura top-of-funnel — test gratuito | ✅ Producida |
| Novela ReturnAI | `novela-returnai-landing.html` | Venta directa $19.97–$29.97 | ✅ Producida |
| ARA — Entrada directa | `ara/index.html` | ARA v0 template base | ✅ Producida |
| ARA — Barco Sin Timón | `ara/barco-sin-timon/index.html` | Arquetipo 01 | ✅ Producida |
| ARA — Feudos Digitales | `ara/feudos-digitales/index.html` | Arquetipo 02 | ✅ Producida |
| ARA — Síndrome del Paralítico | `ara/sindrome-del-paralitico/index.html` | Arquetipo 03 | ✅ Producida |
| ARA — Trampa Burocrática | `ara/trampa-burocratica/index.html` | Arquetipo 04 | ✅ Producida |
| ARA — Teatro de Entrenamiento | `ara/teatro-de-entrenamiento/index.html` | Arquetipo 05 | ✅ Producida |
| ARA — Amenaza de Tormenta | `ara/amenaza-de-tormenta/index.html` | Arquetipo 06 | ✅ Producida |
| ARA — Tormenta Perfecta | `ara/tormenta-perfecta/index.html` | Arquetipo 07 | ✅ Producida |

## Arquitectura de los 11 Bloques (ARA)

Secuencia exacta — no reordenar:

| # | Bloque | Función estratégica |
|---|--------|---------------------|
| B1 | Hero / Contexto de llegada | Naming del arquetipo + CTA atajo secundario |
| B2 | Tres entregables del Assessment | Granularidad de qué obtiene exactamente |
| B3 | Testimoniales con datos verificables | Social proof cuantitativo |
| B4 | Proceso paso a paso · 5 etapas | Reducción de incertidumbre + línea ARIA |
| B5 | Para quién es / Para quién no es | Calificación bidireccional self-selection |
| B6 | Anclaje económico | Justificabilidad ante CFO (pérdida vs $5K) |
| B7 | CTA principal · fondo carbón · botón dorado | Conversión principal con Risk Reversal |
| B8 | Credibilidad del ejecutor · Cesar Lozano | Authority de la firma y del facilitador |
| B9 | Refuerzo Loss Aversion + segundo CTA | Recuperación post-CTA principal |
| B10 | Conectores descendentes · Novela + ART | Self-selection a niveles inferiores |
| B11 | Tagline institucional DCA | Cierre de marca antes del footer |

**Regla:** B7 es el único bloque con fondo carbón en el cuerpo.

## Los 7 Arquetipos ARA

| # | Nombre canónico | Patología dominante |
|---|---|---|
| 01 | El Barco Sin Timón | Falta de Claridad en Contribución de Valor + Liderazgo Desconectado |
| 02 | Feudos Digitales | Silos Culturales + Brecha Generacional |
| 03 | El Síndrome del Paralítico | Creencias Limitantes + Síndrome del Impostor Digital + Miedo al Desplazamiento |
| 04 | La Trampa Burocrática | Fricción de Governance + Falta de Claridad Estratégica + Silos |
| 05 | Teatro de Entrenamiento | Capacitación Inadecuada como amplificador central |
| 06 | Amenaza de Tormenta | 2-3 obstáculos en crisis + 2+ en escalada |
| 07 | La Tormenta Perfecta | 4+ obstáculos críticos simultáneos en ciclos viciosos |

**Personalización:**
- **Alta** (copy distinto por arquetipo): B1, B5, B6, B7, B9
- **Media** (solo titular): B2, B3, B4, B8, B10
- **Sin personalización** (verbatim idéntico): Header, Footer, tarjetas B2, testimoniales B3, etapas B4, métricas B6, botones B7/B9, tarjetas B10, Tagline B11

## Textos Verbatim Obligatorios (ARA)

```
CTA atajo B1:
  Botón:   "Agendar mi sesión de análisis"
  Soporte: "30 minutos · Sin costo · Sin compromiso de avanzar"

CTA principal B7:
  Botón:   "Agendar mi sesión de análisis de resultados"
  Soporte: "30 minutos con un especialista en rentabilización de la IA · Sin costo · Sin compromiso de contratar"

Conector B10 → Novela:  "Conocer la Novela ReturnAI"
Conector B10 → ART:     "Completar el AI Return Test"

Tagline B11: "De la adopción de la IA al Retorno que sí importa." — eslogan canónico único Brand Book DCA 2026 (actualizado 2026-06-30; reemplaza "De la inversión en IA al retorno documentado."). Usa "adopción" como MEDIO/camino hacia el retorno, válido.

Línea ARIA B4 (verbatim):
  "El Assessment aplica el Modelo ARIA para diagnosticar los obstáculos específicos de su organización.
   Cuando los resultados lo justifican, la Solución ReturnAI —6 sprints, 14 herramientas propietarias,
   120 días— convierte ese diagnóstico en retorno documentado."

Footer:
  "© 2026 Digital Change Advisors LLC · Todos los derechos reservados · Modelo ARIA es marca registrada
   de Digital Change Advisors"
```

## Testimoniales Canónicos (Verbatim · Idénticos en todas las versiones)

1. **Julián Hurtado** · CEO · Susuerte S.A.
2. **Rubén Darío Cañas A.** · CEO · Subocol
3. **Diego Parra** · Gerente de TI · SUMMA — Grupo Argos

## Datos Canónicos Invariables

- **10 obstáculos** humanos y organizacionales (medidos por el ART)
- **6 sprints** del Modelo ARIA
- **14 herramientas propietarias** del Modelo ARIA
- **Adopción superior al 70%**
- **ROI documentado en 120 días**
- **Hasta 20 líderes** en la sesión presencial del Assessment
- **Plan de intervención 30-60-90 días**
- **70+ organizaciones** atendidas · **17 países**
- Precio ART: **Gratuito** · Precio Novela ebook: **$19.97** · impreso: **$29.97** · Precio ARA: **$5,000**

## Anti-Patrones de Diseño (Fallo Automático de Auditoría)

- Pop-ups · Countdown timers · "Solo quedan X cupos" · Chatbot flotante
- Banners de oferta limitada · Stock photos en hero · Fotos circulares de testimoniales
- Más de un bloque con fondo carbón en el cuerpo · Fondo teal sólido como sección
- Gradientes en backgrounds · Marcellus en itálica
- Sticky bars de CTA · Videos de YouTube embebidos
- Tipografías distintas a Marcellus y Montserrat

## Reglas de Producción HTML

- Archivo HTML completo, autocontenido, CSS embebido en `<style>` en el `<head>`
- Marcellus solo para H1 y H2. Montserrat para todo lo demás.
- Responsive: mobile-first
- Carga de fuentes: `font-display: swap`
- Botones CTA principal: `min-height: 52px` · Outline: `min-height: 48px`
- Contenedor de texto: máx. `720px` · Layout general: máx. `1100px`
- Padding entre secciones: `80px` desktop / `48px` móvil
- Fotografías de testimoniales: `border-radius: 8px` (nunca circulares)
- Stack vertical en móvil (nunca carruseles)
- Formulario: máximo 5 campos
- **⚠️ OBLIGATORIO — Script de propagación UTM (antes del `</body>`):** Ver sección siguiente.

## Script Canónico de Propagación UTM — OBLIGATORIO en toda landing

**Regla:** Toda landing que contenga enlaces a Tally (o cualquier formulario externo) **debe incluir este script como último elemento antes del `</body>`**. Sin él, los parámetros UTM que llegan desde LinkedIn u otras fuentes se pierden y no se registran en las respuestas del formulario.

```html
<script>
  (function() {
    var params = new URLSearchParams(window.location.search);
    if (!params.toString()) return;
    var tallyLinks = document.querySelectorAll('a[href*="tally.so"]');
    tallyLinks.forEach(function(link) {
      var url = new URL(link.href);
      params.forEach(function(value, key) {
        url.searchParams.set(key, value);
      });
      link.href = url.toString();
    });
  })();
</script>
```

**Selector por tipo de landing:**
- **ART / Novela** → `a[href*="tally.so"]` (CTAs apuntan a Tally)
- **ARA** → `a[href*="tidycal.com"]` (CTAs apuntan a TidyCal)
Cambiar el selector en el script según el destino del formulario de conversión de la landing.

**Comportamiento:**
- Sin UTMs en la URL de la landing → `return` inmediato, sin tocar ningún enlace.
- Con UTMs → se propagan a todos los CTAs de Tally antes de que el usuario haga clic.
- Parámetros existentes en la URL del botón se preservan; los de la landing los sobrescriben con `set()`.
- Ningún otro enlace de la página es afectado.

**Estructura UTM recomendada por landing:**

| Landing | `utm_source` | `utm_medium` | `utm_campaign` |
|---------|-------------|-------------|----------------|
| ART (ai-return-test) | `art-landing` | `header-cta` / `hero-cta` / `final-cta` | `returnai-[mes]` |
| ARA Barco Sin Timón | `ara-barco` | idem | idem |
| ARA Feudos Digitales | `ara-feudos` | idem | idem |
| (cada arquetipo) | `ara-[slug]` | idem | idem |

**Verificación al crear una landing nueva:**
1. Buscar `tally.so` en el HTML — confirmar que todos los enlaces están presentes.
2. Confirmar que el script está justo antes de `</body>` (última línea del body).
3. Prueba manual: cargar la landing con `?utm_source=test&utm_medium=prueba` y hacer hover sobre un botón CTA — la URL del `href` debe mostrar los parámetros inyectados.

## Repositorio de Despliegue

- **Dev (monorepo):** `DCA-ReturnAI/dca-presencia-digital-dev` — carpeta `landings/`
- **Producción:** `DCA-ReturnAI/dca-landings` — GitHub Pages activo: `https://dca-returnai.github.io/dca-landings/`
- **Deploy canónico** (ejecutar desde `Presencia Digital DCA/`):
  ```bash
  git subtree split --prefix=landings -b deploy-tmp-landings && \
  GIT_ASKPASS=/tmp/git_askpass.sh GIT_TERMINAL_PROMPT=0 \
  git -c credential.helper= push production-landings deploy-tmp-landings:main --force && \
  git branch -D deploy-tmp-landings
  ```
- ⚠️ NUNCA usar `git push production-landings main` directo — sube el directorio padre completo y rompe GitHub Pages.

## Estado del Proyecto

### Fases completadas
- ✅ Fase 1 — Estrategia
- ✅ Fase 2 — Matriz de personalización 7 arquetipos
- ✅ Fase 3 — Producción HTML (10 páginas: ART, Novela, ARA v0 + 7 arquetipos)
- ✅ Fase 4 — Auditoría y validación de consistencia (sin hallazgos bloqueantes)
- ✅ Fase 5 — Integración al monorepo `dca-presencia-digital-dev`

### QA + Fine-tuning ARA — CERRADO DEFINITIVO (2026-06-09)
- ✅ 8 archivos ARA auditados y corregidos (v0 template + 7 arquetipos)
- ✅ CTAs (3 por landing) → TidyCal directo; eliminado anti-patrón `href="#cta-principal"`
- ✅ B7: formulario HTML removido en todos; reemplazado por `btn-gold` → TidyCal
- ✅ CSS token `--dca-platinum` corregido: `#dfe3e1` → `#f3f3f3` (Platino Tech canónico)
- ✅ H1 pirámide invertida implementada en todos (`<span class="line">`, L1 ≥ L2 ≥ L3)
- ✅ `scroll-padding-top: 72px` en `html` en todos (nav sticky no tapa anclas)
- ✅ B8 credencial: "LADA" → "LARIA", "247+" → "250+"
- ✅ Gradientes eliminados en `testimonial-photo-placeholder`
- ✅ Voz de marca: "su organización" → "tu organización" en todo el copy
- ✅ B10 rutas relativas corregidas (`../novela-returnai-landing.html` desde v0; `../../` desde arquetipos)
- ✅ UTM script de propagación integrado en todos (selector `a[href*="tidycal.com"]`)
- ✅ Desplegado en producción: `https://dca-returnai.github.io/dca-landings/ara/`

### Ajuste estructural S1 hero ARA (2026-06-10)
- ✅ 7 íconos integrados: `landings/images/ara-icon-[slug].png` (210×210px, en repo)
- ✅ Hero restructurado en 8 landings. Orden nuevo:
  - **Fila 1** (arquetipos): `div.hero-identity` — `img` 210×210 + `h1.hero-archetype-name`
  - **Fila 2**: `h2.hero-title` centrado ancho completo (el antiguo H1 descriptivo)
  - **Fila 3**: `div.hero-video-placeholder` 16:9 (label "Video próximamente")
  - **Fila 4**: `div.hero-grid` doble columna — copy + métricas (sin cambios)
  - **v0**: sin fila de identidad; `h1.hero-title` centrado reemplaza al H1 anterior
- ✅ Lógica BE: H1 arquetipo activa confirmación de identidad antes de la propuesta de valor

### Migración a CSS compartido + script de propagación (2026-06-10)
- ✅ `landings/ara/ara-styles.css` — ~24K de CSS extraído de inline a archivo compartido
- ✅ 8 HTMLs actualizados: `<style>` inline → `<link rel="stylesheet" href="[../]ara-styles.css">`
  - v0: `href="ara-styles.css"` · Arquetipos: `href="../ara-styles.css"`
- ✅ `landings/ara/propagate.py` — script de propagación HTML del v0 a los 7 espejos

**Workflow canónico de fine-tuning ARA (desde 2026-06-10):**
```
Cambio de CSS       → editar ara-styles.css → deploy → 8 landings actualizadas
Cambio HTML común   → editar ara/index.html → python3 propagate.py → deploy
Cambio de arquetipo → editar solo ese archivo → deploy
```

**Secciones comunes** (propagadas por script): `entregables · testimoniales · proceso · cta-principal · credibilidad · conectores · tagline`
**Secciones únicas** (preservadas por archivo): `hero · para-quien · anclaje · refuerzo`

### Hero — Foto editorial del arquetipo (CANÓNICO 2026-06-29)
- ✅ Los 7 arquetipos reemplazaron `.hero-video-placeholder` por `<figure class="hero-video"><img class="hero-video__img">` con foto editorial DCA (creada con IA, estándar de marca). Montado en **ambos despliegues**: `landings/ara/<slug>/` (dca-landings) y `website/<slug>/` (dominio).
- ✅ Imágenes: `<picture>` con `images/foto_<arquetipo>.webp` (WebP q80, 1920px, ~76–132 KB) + fallback `.jpg` (q72). Hero pasó de PNG ~4 MB a ~90 KB. Masters PNG en `_image-masters/` (top-level, fuera de los subtrees de deploy; conversión con cwebp 1.5.0).
- ✅ La foto es el **poster del futuro video**: cuando exista, entra como `<video poster="esa-imagen">` sin re-layout.
- ✅ CSS `.hero-video` + `.hero-video::after` en `ara-styles.css` (ambos repos): overlay `teal 10% / carbón 20%` + `saturate(0.85)`. **Requisito BE, no solo visual:** convierte la escena-problema (p. ej. Amenaza, dashboard rojo en caída) en espejo de identidad sereno; sin overlay picaría aversión a la pérdida como protagonista, prohibido en etapa Solución. Gate UI/UX + BE aprobado.
- ✅ **ara/v0 (overview):** montada `foto_ara_overview.jpg` (sesión del AI Return Assessment en acción con heatmap IUG en pantalla — solución, no patología; generada con Gemini Nano Banana 2). Swap hecho en `website/ara/` y `landings/ara/`. **Ya no queda ningún `.hero-video-placeholder` en el proyecto.**

### Bug corregido — CSS de slugs integrados al dominio (2026-06-29)
- ✅ Los 7 slugs de arquetipo en `website/<slug>/` referenciaban `../ara-styles.css` (inexistente) → **renderizaban sin estilos en el dominio**. Causa: la integración aplanó la estructura `ara/<slug>/` (2 niveles) a `<slug>/` (1 nivel) sin ajustar la ruta relativa. Corregido a `../ara/ara-styles.css`. (Las imágenes `../images/` sí resolvían bien.)

### Pendiente
- ⏳ Fine-tuning visual ARA (iniciar por v0, luego propagate.py)
- ⏳ Generar e insertar imagen de ara/v0 (Gemini) + videos personalizados cuando estén en producción
### Fine-tuning Novela ReturnAI — CERRADO DEFINITIVO (2026-06-17)

**Archivo:** `landings/novela-returnai-landing.html` (no `novela/index.html` — versión anterior)
**Producción:** `https://dca-returnai.github.io/dca-landings/novela-returnai-landing.html`

#### B1 Hero — CERRADO (2026-06-16)
- ✅ Eyebrow: "Modelo ARIA · Novela Ejecutiva · Digital Change Advisors"
- ✅ H1: $8.2M (corregido desde $3.2M — cifra canónica del caso Adalid Puentes en la novela)
- ✅ CTA: 2 botones diferenciados — Impreso $29.97 (primario teal) + Ebook $19.97 (outline), side-by-side desktop
- ✅ Orden precio: Impreso primero — ancla BE al formato premium
- ✅ CTAs placeholder: `#amazon-impreso` / `#amazon-ebook` — activar con URLs reales cuando existan
- ✅ Imagen: `object-fit: contain; height: 100%; width: auto` — proporciones naturales a la altura del contenido
- ✅ Grid hero desktop: `align-items: stretch` — columnas igualan altura del contenido izquierdo
- ✅ Desplegado en producción

#### B2 El Espejo — CERRADO (2026-06-16)
- ✅ Opción A elegida: caso alineado a la novela (Adalid Puentes / Seguros Continental)
- ✅ Inversión: $3.2M → $8.2M (canónico de la novela)
- ✅ Footer tarjeta: "Gestora de inversiones · Sector financiero" → "Seguros Continental · Sector asegurador"
- ✅ 4ta estadística: "11%→70% · Tasa de adopción real" — CSS `.caso-stat-num--sm` (22px para que quepa)
- ✅ P3 umbral: "más de 6 meses" → "más de 12 meses"
- ✅ Blockquote: atribuido a César Lozano, CEO · Digital Change Advisors — clase `.pull-attribution`
- ✅ Alt imagen hero: actualizado al caso Adalid Puentes / Seguros Continental
- ✅ BE copy (H2, P1, P2, P3): identificación → promesa de valor; Diagnóstico → Solución; Modelo ARIA instalado en body; cierre-espejo → value delivery (10 obstáculos, secuencia exacta)
- ✅ Desplegado en producción

#### B3 Primer Capítulo — CERRADO (2026-06-16)
- ✅ Corrección total de nomenclatura — 6 elementos corregidos de "preludio" a "primer capítulo":
  H2 · fragment label · panel tag · panel title · panel timestamp · aria-label cierre
- ✅ Panel content: texto del preludio → **Capítulo 1 completo** ("El ultimátum de hierro")
  4 escenas con timestamps, diálogos Ricardo/Laura, lista 10 obstáculos, flashbacks `* * *`, bitácora digital
- ✅ CSS nuevos en panel: `.preludio-panel__epigraph` · `.preludio-panel__divider` · `.preludio-panel__divider-text` · `.preludio-panel__note` · `.preludio-panel__bitacora` · `.btn-preludio-ebook`
- ✅ Panel CTA: 2 botones Amazon (Impreso $29.97 oro + Ebook $19.97 outline); enlace ART eliminado
- ✅ Párrafo estático (izq): reemplazado por identificación situacional — "47 minutos de reunión" / bridge C-Level → Adalid (BE: identificación situacional + curiosity gap)
- ✅ H2: "comprar" → "comprar el libro" (precisión de objeto)
- ✅ Fragmento derecho (columna): validado sin cambio — mecanismo Zeigarnik + resonancia emocional funcionando; sin duplicación con homepage (modal del homepage es copy comercial, no prosa narrativa)
- ✅ Desplegado en producción

#### B4 La Tesis de la Novela — CERRADO (2026-06-16)
- ✅ Tarjetas: `border-left: 3px solid var(--dca-gold)` + `padding-left: 26px` — "bloques especiales" canónico brand book
- ✅ Números: teal `rgba(46,139,118,0.15)` → `0.28` — marcadores secuenciales visibles; no compiten con el borde dorado
- ✅ Párrafo intro: opacidad `0.68` → `0.82` — la frase de diferenciación competitiva merece más peso visual
- ✅ Connector: `font-style: italic` eliminado — copy de nivel brand book no va en cursiva
- ✅ Intro copy: "no estaba en la plataforma" → "nunca estuvo en la plataforma" (permanencia + indictment más fuerte)
- ✅ Q2: "su empresa" → "tu empresa" (voz de marca canónica)
- ✅ Q1 desc: cierre con curiosity gap activo — "los verás antes de que él mismo sepa nombrarlos"
- ✅ Connector reescrito (BE): prueba social primero → reencuadre quiasmático al final
  - Antes: "La ficción es el vehículo. La metodología es real. / 70+ empresas intervenidas..."
  - Después: "La metodología que documenta la novela opera hoy en 70+ organizaciones. / **La ficción es el formato. La evidencia es real.**"
- ✅ Copy Q1 desc (2026-06-17): "en la gestora" → "en Seguros Continental" — corrige mezcla de casos; "gestora" pertenece al caso real NDA, no a la novela
- ✅ Desplegado en producción

#### Sistema de Motion B1–B4 — CERRADO (2026-06-16)
- ✅ B1 Hero — CSS keyframe page-load (sin scroll): eyebrow 60ms → H1 160ms → chapeau 300ms → CTAs 430ms · portada `dca-cover-in` scale 0.97→1 @ 190ms
- ✅ B2–B4 — `IntersectionObserver` threshold 0.12, one-shot, stagger via `setTimeout`
  - B2: caso-card + 4 caso-stats stagger 80ms + espejo-content 100ms + espejo-pull 300ms
  - B3: preludio-content 0ms + preludio-fragment 150ms
  - B4: revela-intro 0ms + 4 revela-cards stagger 100ms + revela-connector al final
- ✅ B4 card hover: `translateY(-4px)` + box-shadow, spring `cubic-bezier(0.34,1.56,0.64,1)` 300ms
- ✅ B2 métricas: count-up eliminado en sesión posterior; reemplazado por reveal doble etapa (ver B2 ajuste animación)
- ✅ `@media (prefers-reduced-motion: reduce)` desactiva todo el sistema
- ✅ Clase `.sr` + `.sr-in` como sistema scroll-reveal reutilizable para bloques futuros

#### B2 Ajuste animación cifras — CERRADO (2026-06-16)
- ✅ Count-up eliminado de `.caso-stat-num` — atributos `data-count` removidos del HTML; función `revealStat` eliminada del JS
- ✅ Reemplazado por reveal doble etapa: `.caso-stat` hace translate+fade (`.sr`→`.sr-in`); `.caso-stat-num` hace fade independiente con `opacity: 0→1` + `transition: opacity 0.5s ease 0.25s` (demora 250ms respecto al contenedor)
- ✅ `.caso-stat.sr-in .caso-stat-num { opacity: 1 }` — el número "cristaliza" en oro después de que la fila se estabiliza
- ✅ `prefers-reduced-motion`: `.caso-stat-num { opacity: 1 !important; transition: none !important }` en el bloque canónico

#### B5 La Metodología es Verificable — CERRADO (2026-06-16)
- ✅ H2: `<span class="line">` agregado + regla `.metodo-intro h2 .line { display: block }` en CSS — pirámide L1≥L2 garantizada
- ✅ P1: cifras eliminadas (duplicaban las tarjetas métricas — violación "no repetición"); reemplazado por "El Modelo ARIA fue construido para que el retorno sea medible, no estimado. Cada componente tiene un output específico en el P&L — no en métricas de actividad."
- ✅ P2 (referencia ART): eliminado — fork de conversión antes del CTA del libro; el puente hacia ART queda en B10
- ✅ Pull quote: reescrita desde equivalencia validada + efecto halo — "El Modelo ARIA es la base de ReturnAI — la solución que Adalid implementa en la novela para documentar sus resultados. Lo que él vive en 120 días es exactamente lo que el Modelo produce en campo."
- ✅ Footer: "Sheridan, Wyoming, EE.UU." → "Firma registrada en EE.UU. · Operaciones en España, USA y Latam"
- ✅ Métrica `100%` / "Con garantía contractual" → `6` / "Sprints en secuencia invariante" (Opción B — más precisa y narrativa)
- ✅ Hover delay fix: `transition-delay: 0ms` en `.metric-item:hover` — respuesta inmediata al cursor

#### B6 CTA Primario — CERRADO (2026-06-16)
- ✅ H2 L1: "La historia de Adalid." → "La historia es de Adalid." — efecto dotación más directo (posesivo verbal, no genitivo)
- ✅ H2 L2: "La metodología que puedes aplicar." → "La solución es tuya." — efecto dotación + pirámide L1(26)≥L2(21) corregida
- ✅ Orden CTAs: Ebook/Impreso → **Impreso primero** (izquierda/primario) + Ebook segundo (derecha/secundario) — consistente con B1 Hero, ancla precio alto primero
- ✅ Jerarquía visual: clase `.cta-libro-option--primary` (gold sólido) · `.cta-libro-option--secondary` (borde gold, fondo transparente sobre carbón, texto gold)
- ✅ Sub-label Impreso: "Envío Amazon" → "El libro · Amazon Prime" — frame de objeto tangible, no proceso logístico
- ✅ Placeholders actualizados: `href="#amazon-link"` (ambos) → `href="#amazon-impreso"` / `href="#amazon-ebook"` — consistentes con B1 Hero

#### B7 Para quién es / Para quién no es — CERRADO (2026-06-16)
- ✅ H2: "ReturnAI no es para todos los lectores" → "ReturnAI es una lectura de directivo, no de entusiasta." — apertura desde identidad positiva, sin fricción negativa pre-calificación
- ✅ Subtítulo: "...reconozca a Adalid como un espejo, no como un caso ajeno." → "...reconozca en Adalid su propio diagnóstico." — elimina cláusula defensiva; "su propio diagnóstico" más específico y ejecutivo que "un espejo"
- ✅ Ítem 3 "Para quién es": sin prerequisito ART — "quiere ver el Modelo ARIA aplicado a un caso completo antes de comprometerse con una intervención" (visitante sin ART previo puede identificarse)
- ✅ Ítem 4 "Para quién es": referencia a Alejandro Ríos eliminada (solo funcionaba para un canal) → calificador universal: "Directivo que ya entiende que el problema no es la IA — es la organización — y quiere ver cómo se resuelve en 120 días"
- ✅ "Para quién no es" ítem 3: conservado sin cambio — mecanismo de aversión a pérdida invertida funciona perfectamente

**Regla B7 Novela:** H2 siempre desde identidad positiva — nunca abrir con "no es para todos" u otra negación antes de que el visitante se haya auto-identificado en el "sí".

#### B8 ART Conector — CERRADO (2026-06-16)
- ✅ H2: "¿Ya leíste la novela? / El AI Return Test es tu siguiente paso." → "Lo que Adalid aplicó en el Capítulo 3. / Gratuito. 25 minutos." — elimina prerequisito de lectura; funciona para Perfil A (ya leyó) y Perfil B (aún no compró)
- ✅ Body primera oración (versión final 2026-06-17): "El instrumento que Adalid usó en el Capítulo 3 para establecer su línea base y alcanzar el retorno." — elimina redundancia con eyebrow; ancla narrativo al capítulo + destino (retorno)
- ✅ Bloque gris footer-connectors eliminado: las dos tarjetas (ART duplicado + ARA $5,000) generaban sobrecarga de elección y fork de precio abrupto ($29.97 → $5,000)
- ✅ Fondo: teal 4% → **teal 100% `#2e8b76`** — cierre visual fuerte de la landing; excepción aprobada al anti-patrón "fondo teal sólido como sección"
- ✅ Colores sobre teal 100%: eyebrow `rgba(255,255,255,0.72)` · H2 `#ffffff` (4.6:1 WCAG AA) · body `rgba(255,255,255,0.90)` · soporte `rgba(255,255,255,0.60)` · barra acento oro sin cambio
- ✅ Botón CTA: gold sólido → **blanco `#ffffff` con texto teal** — máximo contraste sobre fondo teal; espacio blanco del brand vive dentro del botón

**Excepción canónica al anti-patrón (2026-06-16):** "Fondo teal sólido como sección" está prohibido en el cuerpo de páginas. Excepción aprobada: bloque de cierre final de landing cuando es el último elemento antes del footer y su función es diferenciada del CTA de conversión principal (B6/carbón). Condiciones: un solo bloque por landing, fondo teal sólido solo en posición de cierre.

#### Pendiente externo — Novela
- ⏳ Amazon URLs: `href="#amazon-impreso"` / `href="#amazon-ebook"` en B1 Hero, B3 panel y B6 CTA → activar con URLs reales de Amazon cuando el libro esté listado (acción externa, no bloquea el cierre del fine-tuning)

### Fine-tuning ART — CERRADO DEFINITIVO (2026-06-09)
- ✅ Repo `dca-landings` creado y remote `production-landings` configurado
- ✅ Header/Footer corregidos: logo v2.2 canónico integrado
- ✅ Auditoría completa UX + BE ejecutada (ambas skills) — hallazgos en `project_art_landing_audit.md`
- ✅ Restructura de 8 → 10 bloques implementada (B6, B8, B9 nuevos; B8 Reactivación eliminado)
- ✅ 3 CTAs con arquitectura canónica: header + hero + B10, todos directamente a Tally URL
- ✅ Script UTM propagation integrado (justo antes de `</body>`, línea 2399)
- ✅ Todos los términos prohibidos corregidos (LADA→LARIA, 247+→250+, adopción como fin)
- ✅ Desplegado en producción: `https://dca-returnai.github.io/dca-landings/ai-return-test-landing.html`

---

## Fine-Tuning ART Landing — Orden Canónico y Decisiones (2026-06-08)

> Auditoría ejecutada por `/ui-ux-pro-max` + `/behavioral-economics-c-level` en sesión 34011bfd.  
> Archivo: `landings/ai-return-test-landing.html` · Staging: `https://dca-returnai.github.io/dca-landings/ai-return-test-landing.html`

### Nueva Secuencia Canónica (10 bloques + Header + Footer)

| Pos | Bloque | Origen | Acción | Mecanismo BE |
|-----|--------|--------|--------|--------------|
| Header | Header | ✅ ya corregido | Mantener | — |
| 1 | B1 Hero | B1 original | Ajustar | Aversión a pérdida + curiosity gap |
| 2 | B2 Credibilidad ARIA | B5 original | **Reubicar** + ajustar urgente | Autoridad intelectual |
| 3 | B3 El Entregable | B3 original | Ajustar | Reciprocidad + reducción incertidumbre |
| 4 | B4 Marco 10 Obstáculos | B2 original | **Reubicar** + ajustar | Curiosity gap + reconocimiento |
| 5 | B5 Mecánica del Test | B4 original | Ajustar | Autoridad del instrumento |
| 6 | B6 Caso Ancla Financiero | **NUEVO** | Crear | Anclaje económico |
| 7 | B7 Testimoniales | B6 original | Ajustar | Prueba social |
| 8 | B8 Para quién es / no es | **NUEVO** | Crear | Exclusividad + calificación |
| 9 | B9 Diferenciación vs. Vendors | **NUEVO** | Crear | Reencuadre competitivo |
| 10 | B10 CTA Principal | B7 original | Ajustar | Conversión + efecto dotación |
| — | B8 Reactivación (original) | B8 original | **ELIMINAR** | — |
| Footer | Footer | ✅ ya corregido | Mantener | — |

### Reglas canónicas ART Landing (fijadas por auditoría)

- **H2 CTA canónico:** "Diagnóstico ejecutivo — 30 minutos. / El número que llevarás a tu próxima reunión de Junta." (pirámide invertida, 2 `<span class="line">`)
- **Soporte botón canónico:** "Resultado inmediado · Confidencial · Sin compromiso" (orden de jerarquía C-Level: resultado primero)
- **PROHIBIDO en ART:** "Sin honorarios y sin agenda comercial" → activa señal de alarma en C-Level. Reemplazar siempre por frame positivo de valor.
- **Nota ARA interna:** ELIMINADA del bloque Entregable — no introducir $5,000 antes de que el CEO decida hacer el test gratuito.
- **CTA prematuro en B3:** ELIMINADO — no hay CTAs en el cuerpo de la landing hasta el B10.
- **B8 Reactivación:** ELIMINADO definitivamente — tercer CTA viola regla de CTA único; aversión a pérdida repetida señala desesperación.
- **Fotos de testimoniales:** rectangulares `border-radius: 8px` — NUNCA circulares ni iniciales (anti-patrón explícito del CLAUDE.md).
- **Dato LADA:** PROHIBIDO en toda la landing — reemplazar siempre por "Comunidad LARIA".
- **"17 países" como presencia de firma:** PROHIBIDO — si se menciona comunidad, agregar framing: "Comunidad Skool".
- **withholding note en B4:** debe ABRIR el bloque (no cerrarlo) — activa curiosity gap antes de mostrar los 10 obstáculos.
- **Pull quote anclaje B5:** borde izquierdo oro 4px (no neutro) · canónico del website.
- **B6 Caso Ancla:** fondo platino `#f3f3f3` · números en oro · borde oro en tarjeta · flujo $3.2M → IUG 19%→67% → $891K P&L · atribución: "Gestora de inversiones" (sin nombre de cliente).
- **B9 Diferenciación:** tabla 2 cols, fondo platino, borde oro en columna DCA — versión condensada de la tabla del website `/returnai`.

### Datos Canónicos para la Landing ART (invariables)

- 10 obstáculos humanos y organizacionales
- Índice de Urgencia Global (IUG) — nombre propio del instrumento
- 9 dimensiones de análisis
- 7 arquetipos de resultado
- 30 minutos de aplicación
- 5 minutos al reporte en correo
- 10 páginas del reporte ejecutivo
- 70+ organizaciones acompañadas (NO "17 países")
- 250+ líderes en la Comunidad LARIA (nunca LADA)
- Caso ancla: gestora de inversiones · $3.2M → $891K en P&L · 120 días
- CTA botón verbatim: "Iniciar mi diagnóstico"
- CTA soporte verbatim: "Resultado inmediato · Confidencial · Sin compromiso"

### Deploy ART Landing

```bash
cd "/Users/cesarlozano/Documents/Presencia Digital DCA"
git add landings/ai-return-test-landing.html
git commit -m "landing/art: [descripción del cambio]"
git subtree split --prefix=landings -b deploy-tmp-landings
GIT_ASKPASS=/tmp/git_askpass_landings.sh GIT_TERMINAL_PROMPT=0 git -c credential.helper= push production-landings deploy-tmp-landings:main --force
git branch -D deploy-tmp-landings
```
