import streamlit as st

st.set_page_config(
    page_title="MatKids - Plataforma Educativa",
    page_icon="🎓",
    layout="centered"
)

# ============================================================
#  ESTILOS DE LA PÁGINA DE INICIO
#  Idea de diseño: fondo blanco neutro + cada materia presume
#  su color. La banda arcoíris une visualmente toda la plataforma.
# ============================================================
st.markdown("""
<style>
    /* Fondo neutro claro: las tarjetas de colores son las protagonistas */
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
    }

    /* ---------- BANDA ARCOÍRIS (firma visual de MatKids) ---------- */
    .banda-arcoiris {
        height: 8px;
        border-radius: 999px;
        background: linear-gradient(90deg,
            #1976d2 0%, #1976d2 20%,
            #f9a825 20%, #f9a825 40%,
            #8e24aa 40%, #8e24aa 60%,
            #ef6c00 60%, #ef6c00 80%,
            #00897b 80%, #00897b 100%);
        margin-bottom: 1.6rem;
    }

    /* ---------- TÍTULO HERO CON TEXTO DEGRADADO ---------- */
    .titulo-hero {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1976d2, #8e24aa, #ef6c00, #00897b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.2rem;
    }
    .subtitulo-hero {
        text-align: center;
        font-size: 1.15rem;
        color: #546e7a;
        margin-bottom: 1.4rem;
    }

    /* ---------- TARJETAS DE MATERIAS ---------- */
    .tarjeta {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1.4rem 1.1rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 12px rgba(38, 50, 56, 0.10);
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 240px;
        border-bottom: 6px solid #90a4ae;
    }
    .tarjeta:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 24px rgba(38, 50, 56, 0.20);
    }

    /* Círculo de color con el icono */
    .circulo-icono {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        margin: 0 auto 0.7rem auto;
        color: #ffffff;
    }

    .tarjeta h3 {
        margin: 0.1rem 0 0.5rem 0;
        font-size: 1.2rem;
        color: #263238;
    }
    .tarjeta p {
        font-size: 0.9rem;
        color: #607d8b;
        margin: 0;
    }

    /* Colores por materia */
    .c-aritmetica   { border-bottom-color: #1976d2; }
    .c-aritmetica .circulo-icono   { background-color: #1976d2; }
    .c-geometria    { border-bottom-color: #f9a825; }
    .c-geometria .circulo-icono    { background-color: #f9a825; }
    .c-algebra      { border-bottom-color: #8e24aa; }
    .c-algebra .circulo-icono      { background-color: #8e24aa; }
    .c-trigo        { border-bottom-color: #ef6c00; }
    .c-trigo .circulo-icono        { background-color: #ef6c00; }
    .c-estadistica  { border-bottom-color: #00897b; }
    .c-estadistica .circulo-icono  { background-color: #00897b; }

    /* Insignias de estado */
    .insignia {
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        margin-top: 0.7rem;
    }
    .disponible   { background-color: #e8f5e9; color: #2e7d32; }
    .proximamente { background-color: #eceff1; color: #607d8b; }

    /* Materias no listas: se ven atenuadas */
    .atenuada { opacity: 0.72; }

    /* Texto de la sección de consejo */
    .texto-seccion {
        color: #37474f;
        font-size: 1.05rem;
        font-weight: 600;
    }

    /* Alerta legible */
    div[data-testid="stNotification"] {
        background-color: #ffffff !important;
        border-radius: 10px;
        border-left: 6px solid #1976d2;
        box-shadow: 0 2px 8px rgba(38, 50, 56, 0.12);
    }
    div[data-testid="stNotification"] * { color: #37474f !important; }
</style>

<div class="banda-arcoiris"></div>

<div class="titulo-hero">🎓 MatKids</div>
<div class="subtitulo-hero">¡Aprende matemáticas jugando! 🚀<br>
Tu portal interactivo para estudiantes de educación básica en Venezuela.</div>
""", unsafe_allow_html=True)

st.markdown('<p class="texto-seccion">🧭 Explora las materias desde el menú de la izquierda o elige una tarjeta:</p>',
            unsafe_allow_html=True)

# ============================================================
#  TARJETAS DE MATERIAS
#  (Para agregar una materia nueva: copia un bloque y cambia
#   clase de color, icono, título y descripción)
# ============================================================
fila1 = st.columns(3)
fila2 = st.columns(3)

with fila1[0]:
    st.markdown("""
    <div class="tarjeta c-aritmetica">
        <div class="circulo-icono">🧮</div>
        <h3>Aritmética</h3>
        <p>Enteros, racionales y operaciones visuales en la recta numérica.</p>
        <span class="insignia disponible">✅ Disponible</span>
    </div>
    """, unsafe_allow_html=True)

with fila1[1]:
    st.markdown("""
    <div class="tarjeta c-geometria atenuada">
        <div class="circulo-icono">📐</div>
        <h3>Geometría</h3>
        <p>Perímetros, áreas, teoremas y figuras interactivas.</p>
        <span class="insignia proximamente">🔜 Próximamente</span>
    </div>
    """, unsafe_allow_html=True)

with fila1[2]:
    st.markdown("""
    <div class="tarjeta c-algebra atenuada">
        <div class="circulo-icono">🔢</div>
        <h3>Álgebra</h3>
        <p>Ecuaciones y funciones explicadas paso a paso.</p>
        <span class="insignia proximamente">🔜 Próximamente</span>
    </div>
    """, unsafe_allow_html=True)

with fila2[0]:
    st.markdown("""
    <div class="tarjeta c-trigo atenuada">
        <div class="circulo-icono">📐</div>
        <h3>Trigonometría</h3>
        <p>Relaciones trigonométricas y triángulos.</p>
        <span class="insignia proximamente">🔜 Próximamente</span>
    </div>
    """, unsafe_allow_html=True)

with fila2[1]:
    st.markdown("""
    <div class="tarjeta c-estadistica atenuada">
        <div class="circulo-icono">📊</div>
        <h3>Estadística</h3>
        <p>Gráficos, datos y juegos de probabilidad.</p>
        <span class="insignia proximamente">🔜 Próximamente</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
#  CONSEJO PARA MÓVILES + FOOTER
# ============================================================
st.info("💡 **Consejo:** En el teléfono, despliega el menú lateral con la flecha `>` arriba a la izquierda.")

st.markdown("""
<p style="text-align:center; color:#90a4ae; font-size:0.85rem; margin-top:2rem;">
    🎓 MatKids · Hecho con ❤️ para aprender jugando · Venezuela
</p>
""", unsafe_allow_html=True)
