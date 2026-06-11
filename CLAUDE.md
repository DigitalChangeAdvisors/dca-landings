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
| Novela ReturnAI | `novela/index.html` | Venta directa $19.97–$29.97 | ✅ Producida |
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

Tagline B11: "De la inversión en IA al retorno que importa." — eslogan canónico Brand Book DCA 2026 (actualizado 2026-06-11; reemplaza "Donde la adopción tecnológica…" que usaba "adopción" como fin, término prohibido)

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

### Pendiente
- ⏳ Fine-tuning visual ARA (iniciar por v0, luego propagate.py)
- ⏳ Insertar videos cuando estén en producción (reemplazar `div.hero-video-placeholder` por iframe/video)
- ⏳ Iteración Novela ReturnAI (si aplica)

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
