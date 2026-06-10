#!/usr/bin/env python3
"""
ARA Landings — Script de Propagación de Estructura HTML
========================================================
Uso: python3 propagate.py

Qué hace:
  Lee ara/index.html (v0 master) y propaga los bloques comunes
  a los 7 archivos de arquetipos, preservando el contenido único
  de cada uno.

Bloques COMUNES (se toman del v0 y se propagan):
  - <head> completo (meta tags, fonts, link CSS)
  - Header nav
  - B2 Entregables
  - B3 Testimoniales
  - B4 Proceso (5 etapas)
  - B7 CTA principal (estructura, no copy del H2)
  - B8 Credibilidad César Lozano
  - B10 Conectores
  - B11 Tagline
  - Footer
  - Scripts (UTM, etc.)

Bloques ÚNICOS por arquetipo (se preservan intactos):
  - B1 Hero completo (sección #hero)
  - B5 Para quién es / no es (sección #para-quien)
  - B6 Anclaje económico (sección #anclaje)
  - B9 Loss Aversion + segundo CTA (sección #refuerzo)

Cuándo ejecutar:
  - Después de hacer cambios estructurales en v0 que quieras
    propagar a los 7 espejos.
  - NO es necesario para cambios de CSS (esos se aplican
    automáticamente vía ara-styles.css).
"""

import re
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))

ARCHETYPES = [
    'barco-sin-timon',
    'feudos-digitales',
    'sindrome-del-paralitico',
    'trampa-burocratica',
    'teatro-de-entrenamiento',
    'amenaza-de-tormenta',
    'tormenta-perfecta',
]

# IDs de secciones únicas por arquetipo — se preservan intactos
UNIQUE_SECTIONS = ['hero', 'para-quien', 'anclaje', 'refuerzo']


def extract_section(html, section_id):
    """Extrae el bloque <section id="ID">...</section> completo."""
    pattern = rf'(<section id="{section_id}"[^>]*>.*?</section>)'
    m = re.search(pattern, html, re.DOTALL)
    return m.group(1) if m else None


def replace_section(html, section_id, new_content):
    """Reemplaza el bloque <section id="ID"> con new_content."""
    pattern = rf'<section id="{section_id}"[^>]*>.*?</section>'
    return re.sub(pattern, new_content, html, count=1, flags=re.DOTALL)


def extract_head(html):
    """Extrae el bloque <head>...</head>."""
    m = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
    return m.group(1) if m else None


def replace_head(html, new_head):
    return re.sub(r'<head>.*?</head>', new_head, html, count=1, flags=re.DOTALL)


def extract_header(html):
    """Extrae el <header>...</header>."""
    m = re.search(r'(<header[^>]*>.*?</header>)', html, re.DOTALL)
    return m.group(1) if m else None


def replace_header(html, new_header):
    return re.sub(r'<header[^>]*>.*?</header>', new_header, html,
                  count=1, flags=re.DOTALL)


def extract_footer(html):
    """Extrae el <footer>...</footer>."""
    m = re.search(r'(<footer[^>]*>.*?</footer>)', html, re.DOTALL)
    return m.group(1) if m else None


def replace_footer(html, new_footer):
    return re.sub(r'<footer[^>]*>.*?</footer>', new_footer, html,
                  count=1, flags=re.DOTALL)


def extract_scripts(html):
    """Extrae todos los <script> antes de </body>."""
    m = re.search(r'((?:<script>.*?</script>\s*)+)</body>', html, re.DOTALL)
    return m.group(1).strip() if m else None


def replace_scripts(html, new_scripts):
    return re.sub(r'(?:<script>.*?</script>\s*)+</body>',
                  new_scripts + '\n</body>', html, count=1, flags=re.DOTALL)


def main():
    v0_path = os.path.join(BASE, 'index.html')
    if not os.path.exists(v0_path):
        print("ERROR: no se encontró ara/index.html"); sys.exit(1)

    master = open(v0_path, encoding='utf-8').read()

    # Extraer bloques comunes del master
    master_head    = extract_head(master)
    master_header  = extract_header(master)
    master_footer  = extract_footer(master)
    master_scripts = extract_scripts(master)

    # Secciones comunes (todo menos las únicas)
    all_section_ids = re.findall(r'<section id="([^"]+)"', master)
    common_ids = [s for s in all_section_ids if s not in UNIQUE_SECTIONS]

    master_common_sections = {}
    for sid in common_ids:
        sec = extract_section(master, sid)
        if sec:
            master_common_sections[sid] = sec

    print(f"Master cargado. Secciones comunes: {common_ids}")
    print(f"Secciones únicas preservadas: {UNIQUE_SECTIONS}\n")

    # Propagar a cada arquetipo
    for slug in ARCHETYPES:
        path = os.path.join(BASE, slug, 'index.html')
        if not os.path.exists(path):
            print(f"⚠️  No encontrado: {slug}"); continue

        html = open(path, encoding='utf-8').read()

        # Preservar secciones únicas
        unique_content = {}
        for sid in UNIQUE_SECTIONS:
            sec = extract_section(html, sid)
            if sec:
                unique_content[sid] = sec

        # Aplicar head, header, footer, scripts del master
        if master_head:
            # Restaurar el link CSS relativo correcto para arquetipos
            arch_head = master_head.replace(
                'href="ara-styles.css"',
                'href="../ara-styles.css"'
            )
            html = replace_head(html, arch_head)

        if master_header:
            html = replace_header(html, master_header)

        if master_footer:
            html = replace_footer(html, master_footer)

        if master_scripts:
            html = replace_scripts(html, master_scripts)

        # Aplicar secciones comunes
        for sid, content in master_common_sections.items():
            html = replace_section(html, sid, content)

        # Restaurar secciones únicas del arquetipo
        for sid, content in unique_content.items():
            html = replace_section(html, sid, content)

        open(path, 'w', encoding='utf-8').write(html)
        print(f"✅  {slug}")

    print("\n🎯 Propagación completada.")


if __name__ == '__main__':
    main()
