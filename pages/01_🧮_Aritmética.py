import streamlit as st
from tema import aplicar_tema

# Aplica los colores de Aritmética (azul)
aplicar_tema("Aritmética")

st.set_page_config(
    page_title="Aritmética - MatKids",
    page_icon="🧮",
    layout="centered"
)

# Encabezado de la materia
st.title("🧮 Aritmética")
st.markdown("""
Aquí encontrarás todos los temas de **aritmética**, organizados paso a paso.
Elige un tema para comenzar tu aventura. ⬇️
""")
st.markdown("---")

# ============================================================
#  TEMAS DE ARITMÉTICA
#  Cuando crees un tema nuevo:
#   1. Crea su archivo en pages/ (ej: 1.2_🧮_Racionales.py)
#   2. Copia un bloque de botón y ajusta nombre y ruta
# ============================================================

# --- Tema disponible: Enteros ---
st.subheader("1️⃣ Números Enteros")
st.markdown("Suma y resta de enteros con la recta numérica interactiva. 🎯")

if st.button("▶️ Ir a Enteros", use_container_width=True):
    st.switch_page("pages/1.1_🧮_Enteros.py")

st.markdown("---")

# --- Temas próximos (cuando estén listos, copia el bloque de arriba) ---
st.subheader("2️⃣ Números Racionales")
st.markdown("Fracciones y decimales (en construcción 🚧)")
st.button("🔜 Próximamente", use_container_width=True, disabled=True)

st.markdown("---")

st.subheader("3️⃣ Potenciación y Radicación")
st.markdown("Potencias y raíces paso a paso (en construcción 🚧)")
st.button("🔜 Próximamente", use_container_width=True, disabled=True)

st.markdown("---")

# Botón para volver al inicio
if st.button("🏠 Volver al inicio", use_container_width=True):
    st.switch_page("🏠_Inicio.py")
