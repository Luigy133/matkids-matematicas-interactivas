"""
matkids.py — Punto de entrada de MatKids
-----------------------------------------
Aquí se define TODO el menú lateral. Para agregar una página nueva:
1. Crea su archivo .py en la carpeta correspondiente dentro de pages/
2. Agrega UNA línea en la lista de abajo con su nombre y título

Ejecutar la app:
    streamlit run matkids.py
"""

import streamlit as st

# Configuración general (ya no va en las páginas individuales)
st.set_page_config(
    page_title="MatKids - Matemáticas Interactivas",
    page_icon="🎓",
    layout="centered"
)

# ============================================================
#  MENÚ LATERAL CON SECCIONES PLEGABLES
#  Cada clave del diccionario es un grupo plegable en el menú.
#  "default=True" marca cuál página se muestra al abrir la app.
# ============================================================
pg = st.navigation({
    "🏠 Inicio": [
        st.Page("Inicio.py", title="Página de inicio", default=True),
    ],
    "🧮 Aritmética": [
        st.Page("pages/aritmetica/Aritmetica.py", title="Portada", icon="🧮"),
        st.Page("pages/aritmetica/Enteros.py", title="Enteros", icon="1️⃣"),
        # Cuando crees Racionales.py, descomenta la siguiente línea:
        # st.Page("pages/aritmetica/Racionales.py", title="Racionales", icon="2️⃣"),
    ],
    # Plantilla para el futuro — copia y adapta:
    # "📐 Geometría": [
    #     st.Page("pages/geometria/Geometria.py", title="Portada", icon="📐"),
    # ],
})

# Ejecuta la página seleccionada
pg.run()
