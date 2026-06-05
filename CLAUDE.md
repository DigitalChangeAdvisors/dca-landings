# Landings DCA — Arquitectura y Estado

> Las reglas de marca, sistema visual, tono, skills y flujo de producción están en `../CLAUDE.md` (raíz del workspace). Este archivo contiene solo lo específico de las landing pages comerciales.

## ⚠️ Gate Obligatorio — Pre-audit ANTES de implementar (canónico 2026-06-05)

TODA implementación, ajuste fino o nueva landing — incluyendo iteraciones sobre las 11 landings existentes — debe pasar por auditoría de dos skills **ANTES** de escribir código:

1. `/behavioral-economics-c-level` — valida que el mecanismo BE es correcto para el arquetipo y la etapa del visitante
2. `/ui-ux-pro-max` — valida que el patrón de interacción, layout y motion son apropiados para C-Level

**Sin dictamen de ambas skills, no hay implementación.**

Incidente que motivó la regla: S2 /returnai scrollytelling de 260vh — trampa UX de alta gravedad implementada sin audit previo (2026-06-05).

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

Tagline B11: "Donde la adopción tecnológica encuentra el KPI que importa."

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

## Repositorio de Despliegue

- **Dev (monorepo):** `DCA-ReturnAI/dca-presencia-digital-dev` — carpeta `landings/`
- **Producción:** `DCA-ReturnAI/dca-landings` (por crear cuando haya landings listas)
- **Deploy landings:** `git subtree push --prefix=landings production-landings main`

## Estado del Proyecto

### Fases completadas
- ✅ Fase 1 — Estrategia
- ✅ Fase 2 — Matriz de personalización 7 arquetipos
- ✅ Fase 3 — Producción HTML (10 páginas: ART, Novela, ARA v0 + 7 arquetipos)
- ✅ Fase 4 — Auditoría y validación de consistencia (sin hallazgos bloqueantes)
- ✅ Fase 5 — Integración al monorepo `dca-presencia-digital-dev`

### Pendiente
- ⏳ QA visual en navegador — iniciar con `ara/barco-sin-timon/`
- ⏳ Configurar remote `production-landings` y crear repo `dca-landings`
- ⏳ Iteración ART y Novela ReturnAI (si aplica)
