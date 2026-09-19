import streamlit as st
from tema import aplicar_tema

# Aplica los colores de Aritmética (azul)
aplicar_tema("Aritmética")

st.title("🧮 Aritmética")
st.markdown("""
Aquí encontrarás todos los temas de **aritmética**, organizados paso a paso.
Elige un tema para comenzar tu aventura. ⬇️
""")
st.markdown("---")

# ============================================================
#  TEMAS DE ARITMÉTICA
#  Cuando crees un tema nuevo:
#   1. Crea su archivo .py en esta misma carpeta (pages/aritmetica/)
#   2. Agrégalo también en matkids.py para que aparezca en el menú
#   3. Copia un bloque de botón aquí abajo
# ============================================================

# --- Tema disponible: Enteros ---
st.subheader("1️⃣ Números Enteros")
st.markdown("Suma y resta de enteros con la recta numérica interactiva. 🎯")

if st.button("▶️ Ir a Enteros", use_container_width=True):
    st.switch_page("pages/aritmetica/Enteros.py")

st.markdown("---")

# --- Temas próximos ---
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
    st.switch_page("Inicio.py")
