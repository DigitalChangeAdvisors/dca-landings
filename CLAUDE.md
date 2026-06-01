# Landings DCA — Arquitectura y Estado

> Las reglas de marca, sistema visual, tono, skills y flujo de producción están en `../CLAUDE.md` (raíz del workspace). Este archivo contiene solo lo específico de las landing pages comerciales.

## Propósito de las Landings

Las landing pages son páginas de conversión de un solo objetivo, independientes del website principal. Cada landing apunta a un segmento específico o a un producto de la escalera de valor. Coexisten con el website bajo el mismo branding pero tienen estructura propia (sin nav completa — solo logo + CTA).

## Principios de Diseño para Landings

- **Un solo CTA por landing** — la landing no informa, convierte.
- **Sin menú de navegación completo** — solo logo + botón CTA o flujo de captura.
- **Coherencia visual total** con el website: mismas fuentes, misma paleta, mismo motion system.
- **Progressive disclosure:** problema → metodología → evidencia → CTA. En ese orden exacto.

## Inventario de Landings

*(A completar cuando se definan las landings a construir desde el iMac)*

| Nombre | Archivo | Objetivo | Estado |
|--------|---------|----------|--------|
| — | — | — | ⏳ Por definir |

## Repositorio de Despliegue

- **Dev (monorepo):** `DCA-ReturnAI/dca-presencia-digital-dev` — carpeta `landings/`
- **Producción:** `DCA-ReturnAI/dca-landings` (por crear cuando haya landings listas)
- **Deploy landings:** `git subtree push --prefix=landings production-landings main`

## Próximo Paso

Traer los archivos de landings del iMac a esta carpeta y actualizar el inventario.
