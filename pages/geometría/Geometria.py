import streamlit as st

st.set_page_config(
    page_title="Geometría",
    page_icon="📐",
    layout="centered"
)

# ---------- Estilos morados (coherentes con tus páginas) ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ede7f6 100%);
    }
    h1, h2, h3 {
        color: #4a148c !important;
    }
    div[data-testid="stButton"] > button {
        background-color: #8e24aa;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 600;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #6a1b9a;
        color: white;
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
st.subheader("📚 Temas disponibles")

# Enlaces a las páginas internas (usa rutas relativas al archivo pages/)
st.page_link("pages/geometria/Ecuaciones_enteros.py", label="🧮 Ecuaciones con Enteros", icon="🧮")
