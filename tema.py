"""
tema.py - Sistema de colores de MatKids
---------------------------------------
Cada materia tiene su propia identidad visual. Para aplicarla en cualquier
página de tema, solo agrega estas DOS líneas al inicio del archivo:

    from tema import aplicar_tema
    aplicar_tema("Aritmética")   # <- cambia el nombre según la materia

Materias disponibles:
    "Aritmética", "Geometría", "Álgebra", "Trigonometría", "Estadística"
"""

import streamlit as st

# ============================================================
#  PALETA DE COLORES POR MATERIA
#  (Si quieres cambiar un color, edita solo los códigos de aquí
#   y TODO el sitio se actualiza automáticamente)
# ============================================================
TEMAS = {
    "Aritmética": {
        "primario": "#1976d2",   # botones, bordes
        "claro":    "#e3f2fd",   # fondo degradado claro
        "oscuro":   "#0d47a1",   # títulos
        "texto":    "#0d3b66",   # párrafos
    },
    "Geometría": {
        "primario": "#f9a825",
        "claro":    "#fff8e1",
        "oscuro":   "#e65100",
        "texto":    "#5d4037",
    },
    "Álgebra": {
        "primario": "#8e24aa",
        "claro":    "#f3e5f5",
        "oscuro":   "#6a1b9a",
        "texto":    "#4a148c",
    },
    "Trigonometría": {
        "primario": "#ef6c00",
        "claro":    "#fff3e0",
        "oscuro":   "#e65100",
        "texto":    "#5d4037",
    },
    "Estadística": {
        "primario": "#00897b",
        "claro":    "#e0f2f1",
        "oscuro":   "#00695c",
        "texto":    "#004d40",
    },
}


def aplicar_tema(materia):
    """Aplica el color de la materia a la página actual."""
    if materia not in TEMAS:
        raise ValueError(f"Materia no registrada: {materia}. Opciones: {list(TEMAS)}")

    t = TEMAS[materia]

    plantilla = """
    <style>
        /* Fondo con degradado suave del color de la materia */
        .stApp {
            background: linear-gradient(135deg, __CLARO__ 0%, #ffffff 60%);
        }

        /* Títulos y texto */
        h1, h2, h3 { color: __OSCURO__ !important; }
        [data-testid="stMain"] .stMarkdown p,
        [data-testid="stMain"] .stMarkdown li,
        [data-testid="stMain"] .stMarkdown span,
        [data-testid="stMain"] label {
            color: __TEXTO__ !important;
        }

        /* Botones del color de la materia */
        div[data-testid="stButton"] > button {
            background-color: __PRIMARIO__ !important;
            color: #ffffff !important;
            border-radius: 10px;
            border: none;
            font-weight: 600;
        }
        div[data-testid="stButton"] > button:hover {
            filter: brightness(0.88);
            color: #ffffff !important;
        }

        /* Barra lateral con el color de la materia */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, __OSCURO__ 0%, __PRIMARIO__ 100%);
        }
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* Alertas legibles */
        div[data-testid="stNotification"] {
            background-color: #ffffff !important;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
        }
        div[data-testid="stNotification"] * { color: #333333 !important; }

        /* Expanders y campos de entrada */
        div[data-testid="stExpander"] {
            background-color: #ffffff !important;
            border: 1px solid __PRIMARIO__ !important;
            border-radius: 12px;
        }
        div[data-testid="stExpander"] * {
            color: __TEXTO__ !important;
        }
        input {
            background-color: #ffffff !important;
            color: __TEXTO__ !important;
            border: 2px solid __PRIMARIO__ !important;
            border-radius: 10px !important;
        }
    </style>
    """

    css = (plantilla
           .replace("__PRIMARIO__", t["primario"])
           .replace("__CLARO__", t["claro"])
           .replace("__OSCURO__", t["oscuro"])
           .replace("__TEXTO__", t["texto"]))

    st.markdown(css, unsafe_allow_html=True)
