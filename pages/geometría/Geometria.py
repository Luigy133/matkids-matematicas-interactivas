import streamlit as st

st.set_page_config(
    page_title="Geometría",
    page_icon="📐",
    layout="centered"
)

# ---------- Estilos morados ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ede7f6 100%);
    }
    h1, h2, h3 {
        color: #4a148c !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📐 Sección de Geometría")
st.markdown("""
Bienvenido a la sección de **Geometría**.

Aquí encontrarás temas como:
- Ecuaciones con números enteros aplicadas a geometría
- Figuras y cuerpos geométricos
- Perímetros, áreas y volúmenes
- El plano cartesiano
""")

st.markdown("---")
st.info("👈 Usa el menú lateral para navegar entre los temas de esta sección.")
