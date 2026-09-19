import streamlit as st
import random
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Suma y Resta de Enteros",
    page_icon="🧮",
    layout="centered"
)

# ---------- Estilos personalizados: fondo azul suave ----------
st.markdown("""
<style>
    /* Fondo principal: degradado azul suave */
    .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 50%, #e1f5fe 100%);
    }

    /* Tarjetas/contenedores más legibles sobre el fondo */
    [data-testid="stVerticalBlock"] > div:has(.stMarkdown),
    div[data-testid="stMetric"],
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.75);
        border-radius: 12px;
        padding: 0.5rem 0.75rem;
    }

    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1565c0 0%, #1976d2 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Botones con estilo azul */
    div[data-testid="stButton"] > button {
        background-color: #1976d2;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 600;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #1565c0;
        color: white;
    }

    /* Inputs con fondo blanco */
    input {
        background-color: #ffffff !important;
    }

    /* Títulos en azul oscuro para buen contraste */
    h1, h2, h3 {
        color: #0d47a1 !important;
    }

    /* Texto principal: azul oscuro, siempre legible sobre el fondo */
    [data-testid="stMain"] .stMarkdown p,
    [data-testid="stMain"] .stMarkdown li,
    [data-testid="stMain"] .stMarkdown span,
    [data-testid="stMain"] label,
    [data-testid="stMain"] .stCaption,
    [data-testid="stMain"] [data-testid="stText"] {
        color: #0d3b66 !important;
    }

    /* Alertas (éxito/error/advertencia/info): fondo blanco + texto oscuro */
    div[data-testid="stNotification"] {
        background-color: #ffffff !important;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(13, 59, 102, 0.18);
    }
    div[data-testid="stNotification"] * {
        color: #16324f !important;
    }

    /* Borde lateral de color según el tipo de alerta */
    div[data-testid="stNotification"]:has([data-testid="stNotificationContentSuccess"]) {
        border-left: 6px solid #2e7d32;
    }
    div[data-testid="stNotification"]:has([data-testid="stNotificationContentError"]) {
        border-left: 6px solid #c62828;
    }
    div[data-testid="stNotification"]:has([data-testid="stNotificationContentWarning"]) {
        border-left: 6px solid #f9a825;
    }
    div[data-testid="stNotification"]:has([data-testid="stNotificationContentInfo"]) {
        border-left: 6px solid #1565c0;
    }

    /* Expander "¿Cómo funciona?": fondo blanco sólido y texto siempre visible */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border-radius: 12px;
        border: 1px solid #90caf9;
    }
    div[data-testid="stExpander"] summary,
    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] li,
    div[data-testid="stExpander"] span,
    div[data-testid="stExpander"] strong {
        color: #0d3b66 !important;
    }
    div[data-testid="stExpander"] summary {
        font-weight: 700;
        font-size: 1.05rem;
    }
    div[data-testid="stExpander"] h1,
    div[data-testid="stExpander"] h2,
    div[data-testid="stExpander"] h3 {
        color: #0d47a1 !important;
    }

    /* Campo "Tu respuesta:": fondo blanco, texto azul oscuro y borde visible */
    [data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #0d3b66 !important;
        font-weight: 700;
        font-size: 1.2rem;
        border: 2px solid #1976d2 !important;
        border-radius: 10px;
        padding: 0.5rem;
    }
    [data-testid="stNumberInput"] input::placeholder {
        color: #90a4ae !important;
        font-weight: 400;
    }
    [data-testid="stNumberInput"] input:focus {
        border-color: #0d47a1 !important;
        box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.25);
    }
    /* Etiqueta "Tu respuesta:" bien visible */
    [data-testid="stNumberInput"] label {
        color: #0d3b66 !important;
        font-weight: 700;
    }

    /* Quitar la caja blanca del divisor y dejar una línea azul elegante */
    div[data-testid="stVerticalBlock"] > div:has(> .stMarkdown > hr:only-child) {
        background-color: transparent !important;
        padding: 0 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }
    .stMarkdown hr {
        border: none !important;
        border-top: 3px solid #64b5f6 !important;
        border-radius: 2px;
        margin: 0.75rem 0;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Título y descripción
st.title("🧮 Aventura en la Recta Numérica")
st.markdown("""
Aprende a sumar y restar números enteros **visualmente**.
Cada operación es un viaje en la recta numérica:
- **Sumar** → caminas hacia la derecha ➡️
- **Restar** → caminas hacia la izquierda ⬅️
- **Números negativos** → empiezas a la izquierda del cero
""")

# Inicializar variables de sesión
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'total_intentos' not in st.session_state:
    st.session_state.total_intentos = 0
if 'problema_actual' not in st.session_state:
    st.session_state.problema_actual = None
if 'mostrar_solucion' not in st.session_state:
    st.session_state.mostrar_solucion = False

# Configuración en barra lateral
with st.sidebar:
    st.header("⚙️ Configuración")

    rango = st.slider(
        "Rango de números:",
        min_value=1, max_value=20, value=10,
        help="Los números estarán entre -rango y +rango"
    )

    nivel = st.radio(
        "Dificultad:",
        ["Fácil (solo positivos)", "Medio (con negativos)", "Difícil (mezclado)"]
    )

    st.header("📊 Tu progreso")
    st.metric("Puntos", st.session_state.puntos)
    st.metric("Intentos", st.session_state.total_intentos)
    if st.session_state.total_intentos > 0:
        precision = (st.session_state.puntos / st.session_state.total_intentos) * 100
        st.metric("Precisión", f"{precision:.1f}%")

    if st.button("🔄 Reiniciar juego"):
        st.session_state.puntos = 0
        st.session_state.total_intentos = 0
        st.session_state.problema_actual = None
        st.session_state.mostrar_solucion = False
        st.rerun()


def generar_problema(rango, nivel):
    """Genera un problema de suma/resta según el nivel"""

    if nivel == "Fácil (solo positivos)":
        num1 = random.randint(1, rango)
        num2 = random.randint(1, rango)
        operador = random.choice(['+', '-'])
        if operador == '-' and num2 > num1:
            num1, num2 = num2, num1

    elif nivel == "Medio (con negativos)":
        num1 = random.randint(1, rango)
        num2 = random.randint(-rango, -1)
        operador = random.choice(['+', '-'])

    else:  # Difícil
        num1 = random.randint(-rango, rango)
        num2 = random.randint(-rango, rango)
        operador = random.choice(['+', '-'])

    if operador == '+':
        resultado = num1 + num2
    else:
        resultado = num1 - num2

    operacion_texto = f"{num1} {operador} ({num2})" if num2 < 0 else f"{num1} {operador} {num2}"
    return num1, num2, operador, resultado, operacion_texto


def dibujar_recta_numerica(inicio, delta, num2, operador, resultado, mostrar_resultado=False):
    """Dibuja la recta numérica con el movimiento.

    delta: desplazamiento real con signo (positivo = derecha, negativo = izquierda).
    """
    fig, ax = plt.subplots(figsize=(10, 3))
    fig.patch.set_facecolor('#eaf4fc')
    ax.set_facecolor('#f4faff')

    min_val = min(-10, inicio, resultado, inicio + delta) - 2
    max_val = max(10, inicio, resultado, inicio + delta) + 2

    ax.axhline(y=0, color='#0d47a1', linewidth=1.5)
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(-0.5, 0.5)

    for x in range(int(min_val), int(max_val) + 1):
        if x == 0:
            ax.plot(x, 0, 'ko', markersize=8)
            ax.text(x, -0.12, str(x), ha='center', fontsize=10, fontweight='bold')
        else:
            ax.plot(x, 0, 'ko', markersize=4)
            ax.text(x, -0.12, str(x), ha='center', fontsize=8)

    # Punto de inicio
    ax.plot(inicio, 0, 'go', markersize=15, label='Inicio', zorder=5)
    ax.text(inicio, 0.12, f'Inicio: {inicio}', ha='center', fontsize=9, color='green')

    # Flecha según la dirección REAL del desplazamiento
    color_flecha = 'blue' if delta >= 0 else 'red'
    ax.annotate('', xy=(inicio + delta, 0.05), xytext=(inicio, 0.05),
                arrowprops=dict(arrowstyle='->', color=color_flecha, lw=3))

    # Texto del movimiento
    direccion = 'derecha ➡️' if delta >= 0 else 'izquierda ⬅️'
    texto_mov = f"{operador} ({num2})  →  {abs(delta)} pasos a la {direccion.split()[0]}"
    ax.text((inicio + resultado) / 2, 0.22, texto_mov,
            ha='center', fontsize=9, color=color_flecha)

    # Punto final
    if mostrar_resultado:
        ax.plot(resultado, 0, 'ro', markersize=15, label='Resultado', zorder=5)
        ax.text(resultado, -0.25, f'{resultado}', ha='center', fontsize=10,
                color='red', fontweight='bold')
    else:
        ax.plot(resultado, 0, 'o', markersize=15, color='orange',
                markerfacecolor='none', linestyle='None', label='¿Dónde caes?', zorder=5)
        ax.text(resultado, -0.25, '?', ha='center', fontsize=11,
                color='orange', fontweight='bold')

    ax.set_title("Visualiza tu operación en la recta numérica", fontsize=13)
    ax.set_xlabel("Recta numérica", fontsize=11)
    ax.set_yticks([])
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='x')

    plt.tight_layout()
    return fig


def nueva_operacion():
    """Genera un problema nuevo y limpia el estado."""
    num1, num2, operador, resultado, operacion_texto = generar_problema(rango, nivel)
    st.session_state.problema_actual = {
        'num1': num1, 'num2': num2, 'operador': operador,
        'resultado': resultado, 'operacion_texto': operacion_texto
    }
    st.session_state.mostrar_solucion = False


# Botón para nuevo problema
if st.button("🎲 Nuevo problema", use_container_width=True):
    nueva_operacion()
    st.rerun()

# Si hay un problema activo, mostrarlo
if st.session_state.problema_actual:
    problema = st.session_state.problema_actual
    mostrar = st.session_state.mostrar_solucion

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if mostrar:
            st.markdown(f"## **{problema['operacion_texto']} = {problema['resultado']}**")
        else:
            st.markdown(f"## **{problema['operacion_texto']} = ?**")

    # CORRECCIÓN CLAVE: el desplazamiento real es num2 para sumar y -num2 para restar
    delta = problema['num2'] if problema['operador'] == '+' else -problema['num2']

    fig = dibujar_recta_numerica(
        inicio=problema['num1'],
        delta=delta,
        num2=problema['num2'],
        operador=problema['operador'],
        resultado=problema['resultado'],
        mostrar_resultado=mostrar
    )
    st.pyplot(fig)
    plt.close(fig)

    respuesta = st.number_input(
        "Tu respuesta:",
        value=None,
        placeholder="Escribe el resultado...",
        step=1,
        key=f"resp_{problema['operacion_texto']}_{st.session_state.total_intentos}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Comprobar", use_container_width=True):
            if respuesta is None:
                st.warning("⚠️ Escribe una respuesta antes de comprobar.")
            else:
                st.session_state.total_intentos += 1
                if respuesta == problema['resultado']:
                    st.success(f"¡Correcto! 🎉 {problema['operacion_texto']} = {problema['resultado']}")
                    st.session_state.puntos += 1
                    st.session_state.mostrar_solucion = True
                    st.balloons()
                else:
                    st.error(f"¡Ups! Intenta de nuevo. La respuesta correcta es {problema['resultado']}")
                    st.session_state.mostrar_solucion = True

    with col2:
        if st.button("🔄 Otro problema", use_container_width=True):
            nueva_operacion()
            st.rerun()

    # Explicación con la lógica correcta de signos
    if mostrar or (st.session_state.total_intentos > 0 and st.session_state.problema_actual == problema):
        with st.expander("🔍 Ver explicación", expanded=True):
            pasos = abs(delta)
            direccion = "derecha ➡️" if delta >= 0 else "izquierda ⬅️"
            st.write(
                f"Desde **{problema['num1']}**, la operación **{problema['operador']} ({problema['num2']})** "
                f"te hace mover **{pasos} pasos a la {direccion}**, "
                f"así que caes en **{problema['resultado']}**."
            )
            if (problema['operador'] == '-' and problema['num2'] < 0) or \
               (problema['operador'] == '+' and problema['num2'] < 0):
                st.info("💡 Recuerda: restar un negativo es como sumar, y sumar un negativo es como restar.")

# Sección de ayuda
with st.expander("📚 ¿Cómo funciona? (Haz clic para aprender)"):
    st.markdown("""
    ### Reglas básicas de los números enteros:

    **En la recta numérica:**
    - ➡️ Ir a la **derecha** = números más grandes
    - ⬅️ Ir a la **izquierda** = números más pequeños

    **Ejemplos:**
    - `5 + 3` → empiezas en 5, te mueves 3 a la derecha → **8**
    - `5 - 3` → empiezas en 5, te mueves 3 a la izquierda → **2**
    - `-2 + 4` → empiezas en -2, te mueves 4 a la derecha → **2**
    - `2 - 5` → empiezas en 2, te mueves 5 a la izquierda → **-3**
    - `5 - (-3)` → restar un negativo = moverse a la derecha → **8**
    - `4 + (-6)` → sumar un negativo = moverse a la izquierda → **-2**

    **Consejo:** Siempre puedes usar la recta numérica para visualizar la operación.
    """)
