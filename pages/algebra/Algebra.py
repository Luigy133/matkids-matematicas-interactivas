import streamlit as st

# ---------- Estilos morados ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ede7f6 100%);
    }
    [data-testid="stVerticalBlock"] > div:has(.stMarkdown),
    div[data-testid="stMetric"],
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.78);
        border-radius: 12px;
        padding: 0.5rem 0.75rem;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #6a1b9a 0%, #8e24aa 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
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
    h1, h2, h3 {
        color: #4a148c !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Encabezado ----------
st.title("🧠 Sección de Álgebra")

st.markdown("""
Bienvenido a la sección de **Álgebra** de MatKids.

Aquí aprenderás a trabajar con **letras y números**, a resolver
**ecuaciones** y a entender cómo el álgebra describe situaciones
de la vida real.

> 💡 **¿Sabías qué?** El álgebra es como un idioma: las **letras (x, y, z)**
> representan números desconocidos y las **ecuaciones** son frases que
> debes descifrar. ¡Vamos a ello! 🚀
""")

st.markdown("---")

# ---------- Tarjetas de temas ----------
st.subheader("📚 Temas disponibles")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🧮 Ecuaciones con Números Enteros

    Aprende a resolver ecuaciones del tipo **x + a = b**, **x − a = b**,
    **a + x = b** y **a − x = b** usando la recta numérica como
    apoyo visual.
    """)
    st.info("👉 Selecciónala en el menú lateral: **Ecuaciones con Enteros**")

with col2:
    st.markdown("""
    ### ➕ Próximamente

    - Expresiones algebraicas
    - Monomios y polinomios
    - Productos notables
    - Factorización
    - Sistemas de ecuaciones
    """)
    st.warning("🚧 En construcción... ¡vuelve pronto!")

st.markdown("---")

# ---------- Objetivos de la sección ----------
with st.expander("🎯 ¿Qué aprenderás en Álgebra? (Haz clic aquí)"):
    st.markdown("""
    Al terminar esta sección serás capaz de:

    1. **Identificar** una ecuación y sus partes (incógnita, coeficientes, términos).
    2. **Despejar** la incógnita usando las propiedades de la igualdad.
    3. **Resolver** ecuaciones con números enteros (positivos y negativos).
    4. **Verificar** tus soluciones reemplazando el valor de **x**.
    5. **Visualizar** el significado de una ecuación en la recta numérica.

    ---

    ### 🧩 La regla de oro del álgebra

    > **Lo que haces de un lado de la ecuación, debes hacerlo del otro lado.**

    Como una balanza en equilibrio ⚖️: si quitas 3 de un platillo,
    debes quitar 3 del otro para que siga equilibrada.
    """)

# ---------- Pie ----------
st.markdown("---")
st.caption("📐 MatKids · Matemáticas Interactivas · Sección Álgebra")
