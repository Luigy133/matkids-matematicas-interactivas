import streamlit as st
import random

# ============================================================
#  ESTILOS (iguales que tenías: fondo morado suave)
# ============================================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ede7f6 100%);
    }
    [data-testid="stVerticalBlock"] > div:has(.stMarkdown),
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.78);
        border-radius: 12px;
        padding: 0.75rem 1rem;
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
    div[data-testid="stButton"] {
        background: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    .stApp p, .stApp li, .stApp span, .stApp label,
    .stApp div[data-testid="stMarkdownContainer"] {
        color: #4a148c;
    }
    .stApp label,
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] p {
        color: #4a148c !important;
        font-weight: 600;
    }
    input {
        background-color: #ffffff !important;
        color: #4a148c !important;
    }
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.85) !important;
        border-radius: 12px;
        padding: 0.25rem 0.5rem;
        border: 1px solid #ce93d8 !important;
    }
    div[data-testid="stExpander"] summary,
    div[data-testid="stExpander"] summary *,
    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] li,
    div[data-testid="stExpander"] span,
    div[data-testid="stExpander"] h1,
    div[data-testid="stExpander"] h2,
    div[data-testid="stExpander"] h3,
    div[data-testid="stExpander"] h4,
    div[data-testid="stExpander"] strong,
    div[data-testid="stExpander"] em,
    div[data-testid="stExpander"] blockquote {
        color: #4a148c !important;
    }
    div[data-testid="stExpander"] table,
    div[data-testid="stExpander"] th,
    div[data-testid="stExpander"] td {
        color: #4a148c !important;
        border-color: #8e24aa !important;
    }
    div[data-testid="stExpander"] th {
        background-color: #e1bee7 !important;
    }
    div[data-testid="stExpander"] summary,
    div[data-testid="stExpander"] summary:hover,
    div[data-testid="stExpander"] details[open] summary,
    div[data-testid="stExpander"] details summary:focus {
        background-color: #f3e5f5 !important;
        color: #4a148c !important;
        border-radius: 10px !important;
    }
    div[data-testid="stExpander"] details,
    div[data-testid="stExpander"] details[open] {
        background-color: #faf0fb !important;
    }
    div[data-testid="stExpander"] code,
    .stApp code {
        background-color: #ede7f6 !important;
        color: #6a1b9a !important;
        padding: 2px 6px !important;
        border-radius: 6px !important;
        border: 1px solid #ce93d8 !important;
    }
    div[data-testid="stExpander"] pre,
    .stApp pre {
        background-color: #ede7f6 !important;
        color: #4a148c !important;
        border-radius: 8px !important;
        padding: 0.5rem 0.75rem !important;
    }
    div[data-testid="stExpander"] > details > div {
        background-color: #faf0fb !important;
    }
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] div {
        color: #4a148c !important;
    }
    h1, h2, h3 {
        color: #4a148c !important;
    }
    div[data-testid="stMetric"] label {
        color: #4a148c !important;
    }

    /* ---------- Tarjetas de niveles ---------- */
    .nivel-card {
        background-color: #ffffff;
        border-radius: 14px;
        padding: 1rem 1rem;
        text-align: center;
        box-shadow: 0 3px 10px rgba(142, 36, 170, 0.12);
        border-top: 6px solid #8e24aa;
        margin-bottom: 1rem;
        height: 100%;
    }
    .nivel-card h4 { margin: 0.3rem 0; font-size: 1.1rem; }
    .nivel-card p { font-size: 0.9rem; margin: 0.25rem 0; }
    .nivel-facil    { border-top-color: #43a047; }
    .nivel-facil h4    { color: #2e7d32 !important; }
    .nivel-medio    { border-top-color: #f9a825; }
    .nivel-medio h4    { color: #ef6c00 !important; }
    .nivel-avanzado { border-top-color: #e53935; }
    .nivel-avanzado h4 { color: #c62828 !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================
#  1. TÍTULO CENTRADO
# ============================================================
st.markdown(
    "<h1 style='text-align: center; font-size: 2rem; color: #4a148c; margin-bottom: 0.5rem;'>"
    "🧮 Ecuaciones de 1er Grado con Números Enteros"
    "</h1>",
    unsafe_allow_html=True
)

# ============================================================
#  2. TARJETA DE EXPLICACIÓN (solo teoría)
# ============================================================
st.markdown("""
<div style="
    color: #4a148c;
    font-size: 1.05rem;
    line-height: 1.75;
    background-color: rgba(255, 255, 255, 0.85);
    padding: 1.25rem 1.75rem;
    border-radius: 14px;
    margin: 1rem 0 1.5rem 0;
    box-shadow: 0 2px 6px rgba(142, 36, 170, 0.12);
">
<b>Aprende a resolver ecuaciones en ℤ</b> (Números Enteros) paso a paso. 🎯
<ul style="margin: 0.6rem 0 0.2rem 0; padding-left: 1.4rem;">
  <li>Una <b>ecuación</b> es una igualdad algebraica en la que aparecen letras
  (<b>incógnitas</b>) con valor desconocido.</li>
  <li>El <b>grado</b> de una ecuación viene dado por el exponente mayor de la incógnita.
  En este tema trabajamos con ecuaciones <b>lineales (de grado 1)</b> con una incógnita.</li>
  <li><b>Solucionar</b> una ecuación es encontrar el valor de la incógnita que transforma
  la ecuación en una identidad.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ============================================================
#  3. TARJETAS DE LOS 3 NIVELES
# ============================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="nivel-card nivel-facil">
        <div style="font-size:2rem;">🟢</div>
        <h4>Fácil</h4>
        <p>La incógnita aparece sola:</p>
        <p><code>x + a = b</code></p>
        <p>Ejemplo: <code>x + 3 = 8</code> → <b>x = 5</b></p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="nivel-card nivel-medio">
        <div style="font-size:2rem;">🟡</div>
        <h4>Medio</h4>
        <p>La incógnita tiene coeficiente:</p>
        <p><code>ax + b = c</code></p>
        <p>Ejemplo: <code>3x + 5 = 20</code> → <b>x = 5</b></p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="nivel-card nivel-avanzado">
        <div style="font-size:2rem;">🔴</div>
        <h4>Avanzado</h4>
        <p>La incógnita está en ambos lados:</p>
        <p><code>ax + b = cx + d</code></p>
        <p>Ejemplo: <code>3x + 5 = −2x − 10</code> → <b>x = −3</b></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; color:#4a148c; font-weight:600; margin: 0.5rem 0 1rem 0;">
📌 Selecciona un <b>nivel</b> y un <b>modo</b> en el menú lateral, y pulsa
<b>«Generar Ecuación»</b> para comenzar.
</div>
""", unsafe_allow_html=True)

# ============================================================
#  VARIABLES DE SESIÓN
# ============================================================
for clave, valor in [('puntos', 0), ('total_intentos', 0), ('problema_actual', None),
                     ('mostrar_solucion', False), ('contador', 0)]:
    if clave not in st.session_state:
        st.session_state[clave] = valor

# ============================================================
#  BARRA LATERAL
# ============================================================
with st.sidebar:
    st.header("⚙️ Configuración")

    modo = st.radio("Modo de práctica:", ["🪜 Modo Guiado", "⚡ Modo Reto"], key="modo_sel")

    # Si cambia el modo, limpiar el problema activo
    if st.session_state.get("modo_prev") != modo:
        st.session_state.modo_prev = modo
        st.session_state.problema_actual = None

    nivel = st.radio("Nivel:", ["Fácil", "Medio", "Avanzado"], key="nivel_sel")

    # Si cambia el nivel, limpiar el problema activo
    if st.session_state.get("nivel_prev") != nivel:
        st.session_state.nivel_prev = nivel
        st.session_state.problema_actual = None

    rango = st.slider(
        "Rango de números:",
        min_value=1, max_value=50, value=10,
        help="Los números estarán entre -rango y +rango"
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

# ============================================================
#  FUNCIONES AUXILIARES DE FORMATEO
# ============================================================

def fmt_num(n):
    """Número con paréntesis si es negativo: 5 → '5', -3 → '(-3)'"""
    return f"({n})" if n < 0 else f"{n}"


def ax_str(c):
    """Término con x para mostrar: 3 → '3x', -2 → '(-2)x', 1 → 'x', -1 → '-x'"""
    if c == 1:
        return "x"
    if c == -1:
        return "-x"
    return f"({c})x" if c < 0 else f"{c}x"


# ============================================================
#  GENERADOR DE ECUACIONES (solución entera garantizada)
# ============================================================

def generar_ecuacion(rango, nivel):
    """Genera la ecuación construyendo X primero."""

    if nivel == "Fácil":
        x = random.randint(-rango, rango)
        a = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        tipo = random.choice(['x+a=b', 'x-a=b', 'a+x=b', 'a-x=b'])

        if tipo == 'x+a=b':
            b = x + a
        elif tipo == 'x-a=b':
            b = x - a
        elif tipo == 'a+x=b':
            b = a + x
        else:  # a-x=b  (evitamos b = 0 para que las opciones tengan sentido)
            if a - x == 0:
                x += 1
            b = a - x

        return {'x': x, 'a': a, 'b': b, 'tipo': tipo, 'nivel': nivel}

    elif nivel == "Medio":
        x = random.randint(-rango, rango)
        a = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        b = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        tipo = random.choice(['aX+b=c', 'aX-b=c', 'b+aX=c', 'b-aX=c'])

        if tipo == 'aX+b=c':
            c = a * x + b
        elif tipo == 'aX-b=c':
            c = a * x - b
        elif tipo == 'b+aX=c':
            c = b + a * x
        else:  # b-aX=c
            c = b - a * x

        return {'x': x, 'a': a, 'b': b, 'c': c, 'tipo': tipo, 'nivel': nivel}

    else:  # Avanzado
        x = random.randint(-rango, rango)
        a = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        c = random.choice([i for i in range(-rango, rango + 1) if i != 0 and i != a])
        b = random.choice([i for i in range(-rango, rango + 1) if i != 0])

        tipo = random.choice(['aX+b=cX+d', 'aX-b=cX+d', 'aX+b=cX-d', 'aX-b=cX-d'])

        # CORRECCIÓN: d depende del tipo para que la ecuación sea verdadera
        if tipo == 'aX+b=cX+d':
            d = (a - c) * x + b      # ax + b = cx + d
        elif tipo == 'aX-b=cX+d':
            d = (a - c) * x - b      # ax − b = cx + d
        elif tipo == 'aX+b=cX-d':
            d = -(a - c) * x - b     # ax + b = cx − d
        else:  # aX-b=cX-d
            d = -(a - c) * x + b     # ax − b = cx − d

        return {'x': x, 'a': a, 'b': b, 'c': c, 'd': d, 'tipo': tipo, 'nivel': nivel}


# ============================================================
#  FORMATEO DEL TEXTO DE LA ECUACIÓN
# ============================================================

def fmt_var(coef, primero=True):
    if coef == 0:
        return ""
    signo = ""
    if not primero:
        signo = " + " if coef > 0 else " - "
        coef = abs(coef)
    else:
        if coef < 0:
            signo = "-"
            coef = abs(coef)
    cuerpo = "x" if coef == 1 else f"{coef}x"
    return f"{signo}{cuerpo}"


def formatear_ecuacion(p):
    nivel = p['nivel']
    tipo = p['tipo']

    if nivel == "Fácil":
        a = p['a']
        b = p['b']
        if tipo == 'x+a=b':
            return f"x + {a} = {b}" if a >= 0 else f"x + ({a}) = {b}"
        elif tipo == 'x-a=b':
            return f"x - {a} = {b}" if a >= 0 else f"x - ({a}) = {b}"
        elif tipo == 'a+x=b':
            return f"{a} + x = {b}"
        else:
            return f"{a} - x = {b}"

    elif nivel == "Medio":
        a, b, c = p['a'], p['b'], p['c']

        if tipo == 'aX+b=c':
            izq = fmt_var(a, primero=True)
            izq += f" + {b}" if b >= 0 else f" + ({b})"
            return f"{izq} = {c}"
        elif tipo == 'aX-b=c':
            izq = fmt_var(a, primero=True)
            izq += f" - {b}" if b >= 0 else f" - ({b})"
            return f"{izq} = {c}"
        elif tipo == 'b+aX=c':
            der = fmt_var(a, primero=False)
            if b >= 0:
                return f"{b}{der} = {c}"
            else:
                return f"({b}){der} = {c}"
        else:  # b-aX=c
            if a >= 0:
                return f"{b} - {a}x = {c}"
            else:
                return f"{b} - ({a})x = {c}"

    else:  # Avanzado
        a, b, c, d = p['a'], p['b'], p['c'], p['d']

        if tipo == 'aX+b=cX+d':
            izq = fmt_var(a, primero=True)
            izq += f" + {b}" if b >= 0 else f" + ({b})"
            der = fmt_var(c, primero=True)
            der += f" + {d}" if d >= 0 else f" + ({d})"
            return f"{izq} = {der}"
        elif tipo == 'aX-b=cX+d':
            izq = fmt_var(a, primero=True)
            izq += f" - {b}" if b >= 0 else f" - ({b})"
            der = fmt_var(c, primero=True)
            der += f" + {d}" if d >= 0 else f" + ({d})"
            return f"{izq} = {der}"
        elif tipo == 'aX+b=cX-d':
            izq = fmt_var(a, primero=True)
            izq += f" + {b}" if b >= 0 else f" + ({b})"
            der = fmt_var(c, primero=True)
            der += f" - {d}" if d >= 0 else f" - ({d})"
            return f"{izq} = {der}"
        else:  # aX-b=cX-d
            izq = fmt_var(a, primero=True)
            izq += f" - {b}" if b >= 0 else f" - ({b})"
            der = fmt_var(c, primero=True)
            der += f" - {d}" if d >= 0 else f" - ({d})"
            return f"{izq} = {der}"


# ============================================================
#  CONSTRUCTOR DE PASOS GUIADOS
# ============================================================

def paso_opcion(pregunta, correcta, distractores, pista, resuelto_texto):
    """Crea un paso de opción múltiple con 3 opciones mezcladas."""
    opciones = [correcta] + distractores
    random.shuffle(opciones)
    return {
        'tipo': 'opcion',
        'pregunta': pregunta,
        'opciones': opciones,
        'respuesta': correcta,
        'pista': pista,
        'resuelto_texto': resuelto_texto,
    }


def paso_numero(pregunta, respuesta, pista, resuelto_texto):
    """Crea un paso de respuesta numérica."""
    return {
        'tipo': 'numero',
        'pregunta': pregunta,
        'respuesta': respuesta,
        'pista': pista,
        'resuelto_texto': resuelto_texto,
    }


def construir_pasos(p):
    """Construye la lista de pasos guiados según nivel y tipo."""
    pasos = []
    nivel = p['nivel']
    tipo = p['tipo']
    x = p['x']

    # ==================== NIVEL FÁCIL ====================
    if nivel == "Fácil":
        a = p['a']
        b = p['b']

        if tipo == 'x+a=b':
            pasos.append(paso_opcion(
                "¿Qué operación debes hacer en **ambos lados** para dejar la x sola?",
                f"Restar {fmt_num(a)}",
                [f"Sumar {fmt_num(a)}", f"Dividir entre {fmt_num(a)}"],
                "Lo que está SUMANDO pasa al otro lado RESTANDO.",
                f"x + {fmt_num(a)} = {b}  →  x = {b} − {fmt_num(a)}"))
            pasos.append(paso_numero(
                "Aplica la operación. ¿Cuánto vale **x**?",
                x,
                f"{b} − {fmt_num(a)} = ?  ¡Cuidado con los signos!",
                f"**x = {x}**"))

        elif tipo == 'x-a=b':
            pasos.append(paso_opcion(
                "¿Qué operación debes hacer en **ambos lados** para dejar la x sola?",
                f"Sumar {fmt_num(a)}",
                [f"Restar {fmt_num(a)}", f"Dividir entre {fmt_num(a)}"],
                "Lo que está RESTANDO pasa al otro lado SUMANDO.",
                f"x − {fmt_num(a)} = {b}  →  x = {b} + {fmt_num(a)}"))
            pasos.append(paso_numero(
                "Aplica la operación. ¿Cuánto vale **x**?",
                x,
                f"{b} + {fmt_num(a)} = ?  ¡Cuidado con los signos!",
                f"**x = {x}**"))

        elif tipo == 'a+x=b':
            pasos.append(paso_opcion(
                "¿Qué operación debes hacer en **ambos lados** para dejar la x sola?",
                f"Restar {fmt_num(a)}",
                [f"Sumar {fmt_num(a)}", f"Dividir entre {fmt_num(a)}"],
                "El número que acompaña a la x (aunque esté antes) pasa RESTANDO.",
                f"{a} + x = {b}  →  x = {b} − {fmt_num(a)}"))
            pasos.append(paso_numero(
                "Aplica la operación. ¿Cuánto vale **x**?",
                x,
                f"{b} − {fmt_num(a)} = ?  ¡Cuidado con los signos!",
                f"**x = {x}**"))

        else:  # a-x=b  (caso especial: 3 pasos)
            pasos.append(paso_opcion(
                "La x está **restando**. ¿Qué hacemos primero?",
                "Sumar x en ambos lados",
                [f"Restar {fmt_num(a)} en ambos lados", f"Dividir entre {fmt_num(a)}"],
                "Cuando la x está restando, pásala al otro lado SUMANDO.",
                f"{a} − x = {b}  →  {fmt_num(a)} = {b} + x"))
            pasos.append(paso_opcion(
                f"Ahora tenemos {fmt_num(a)} = {b} + x. ¿Qué operación despeja la x?",
                f"Restar {fmt_num(b)}",
                [f"Sumar {fmt_num(b)}", f"Dividir entre {fmt_num(b)}"],
                "El número que acompaña a la x pasa RESTANDO.",
                f"x = {fmt_num(a)} − {fmt_num(b)}"))
            pasos.append(paso_numero(
                "¿Cuánto vale **x**?",
                x,
                f"x = {a} − {fmt_num(b)} = ?  ¡Cuidado con los signos!",
                f"**x = {x}**"))

    # ==================== NIVEL MEDIO ====================
    elif nivel == "Medio":
        a, b, c = p['a'], p['b'], p['c']
        ax = ax_str(a)

        if tipo in ('aX+b=c', 'aX-b=c', 'b+aX=c'):
            if tipo == 'aX-b=c':
                oper1 = f"Sumar {fmt_num(b)}"
                distr1 = [f"Restar {fmt_num(b)}", f"Dividir entre {fmt_num(a)}"]
                pista1 = "Primero aisla el término con x: lo que está RESTANDO pasa SUMANDO."
                val_ax = c + b
                signo = "+"
                exp2 = f"{fmt_num(c)} + {fmt_num(b)} = ?"
            else:
                oper1 = f"Restar {fmt_num(b)}"
                distr1 = [f"Sumar {fmt_num(b)}", f"Dividir entre {fmt_num(a)}"]
                pista1 = "Primero aisla el término con x: lo que está SUMANDO pasa RESTANDO."
                val_ax = c - b
                signo = "−"
                exp2 = f"{fmt_num(c)} − {fmt_num(b)} = ?"

            pasos.append(paso_opcion(
                "¿Qué operación haces **primero** para aislar el término con x?",
                oper1, distr1, pista1,
                f"{formatear_ecuacion(p)}  →  {ax} = {fmt_num(c)} {signo} {fmt_num(b)}"))
            pasos.append(paso_numero(
                f"Aplica la operación. Completa: **{ax} = ___**",
                val_ax, exp2,
                f"**{ax} = {val_ax}**"))
            pasos.append(paso_opcion(
                "El término con x está aislado. ¿Qué operación sigue?",
                f"Dividir entre {fmt_num(a)}",
                [f"Multiplicar por {fmt_num(a)}", f"Restar {fmt_num(a)}"],
                "Lo que MULTIPLICA a la x pasa DIVIDIENDO a todo el miembro.",
                f"{ax} = {val_ax}  →  x = {val_ax} ÷ {fmt_num(a)}"))
            pasos.append(paso_numero(
                "¿Cuál es el valor de **x**?",
                x,
                f"x = {val_ax} ÷ {fmt_num(a)} = ?  Recuerda la regla de signos.",
                f"**x = {x}**"))

        else:  # b-aX=c  (caso especial)
            pasos.append(paso_opcion(
                "La x está **restando** y tiene coeficiente. ¿Qué hacemos primero?",
                f"Sumar {ax_str(a)} en ambos lados",
                [f"Restar {fmt_num(b)} en ambos lados", f"Dividir entre {fmt_num(a)}"],
                "Cuando la x está restando, pásala al otro lado SUMANDO.",
                f"{fmt_num(b)} = {fmt_num(c)} + {ax_str(a)}"))
            pasos.append(paso_opcion(
                f"Ahora: {fmt_num(b)} = {fmt_num(c)} + {ax_str(a)}. ¿Qué operación sigue?",
                f"Restar {fmt_num(c)}",
                [f"Sumar {fmt_num(c)}", f"Dividir entre {fmt_num(a)}"],
                "El número solo pasa al otro lado RESTANDO.",
                f"{ax_str(a)} = {b - c}"))
            pasos.append(paso_opcion(
                "¿Cómo despejas la **x**?",
                f"Dividir entre {fmt_num(a)}",
                [f"Multiplicar por {fmt_num(a)}", f"Restar {fmt_num(a)}"],
                "Lo que multiplica a la x pasa DIVIDIENDO.",
                f"x = {b - c} ÷ {fmt_num(a)}"))
            pasos.append(paso_numero(
                "¿Cuánto vale **x**?",
                x,
                f"x = {b - c} ÷ {fmt_num(a)} = ?  Recuerda la regla de signos.",
                f"**x = {x}**"))

    # ==================== NIVEL AVANZADO ====================
    else:
        a, b, c, d = p['a'], p['b'], p['c'], p['d']
        coef = a - c

        # Según la variante, la constante izquierda se mueve restando o sumando,
        # y el valor base derecho es d o -d
        if tipo in ('aX+b=cX+d', 'aX+b=cX-d'):
            oper3 = f"Restar {fmt_num(b)}"
            opp3 = f"Sumar {fmt_num(b)}"
            signo_exp = "−"
        else:
            oper3 = f"Sumar {fmt_num(b)}"
            opp3 = f"Restar {fmt_num(b)}"
            signo_exp = "+"

        right_base = d if tipo in ('aX+b=cX+d', 'aX-b=cX+d') else -d
        right_final = right_base - b if signo_exp == "−" else right_base + b

        pasos.append(paso_opcion(
            "¿Qué haces para **agrupar las x** en el lado izquierdo?",
            f"Restar {ax_str(c)} en ambos lados",
            [f"Sumar {ax_str(c)} en ambos lados", f"Restar {fmt_num(b)} en ambos lados"],
            "Junta las x de un lado: lo que suma pasa RESTANDO.",
            f"{ax_str(a)} − {ax_str(c)} = ..."))
        pasos.append(paso_numero(
            "Simplifica el lado izquierdo. ¿De cuánto queda el coeficiente de x? "
            "(escribe solo el número)",
            coef,
            f"{a} − {fmt_num(c)} = ?",
            f"**{ax_str(coef)}** = ... (falta mover el número)"))
        pasos.append(paso_opcion(
            f"¿Qué haces con el **{fmt_num(b)}** para dejar solo las x a la izquierda?",
            oper3,
            [opp3, f"Dividir entre {fmt_num(coef)}"],
            "El número pasa al otro lado con la operación contraria.",
            f"{ax_str(coef)} = {fmt_num(right_base)} {signo_exp} {fmt_num(b)}"))
        pasos.append(paso_numero(
            f"Aplica la operación. Completa: **{ax_str(coef)} = ___**",
            right_final,
            f"{fmt_num(right_base)} {signo_exp} {fmt_num(b)} = ?",
            f"**{coef}x = {right_final}**"))
        pasos.append(paso_opcion(
            "¿Cómo despejas la **x**?",
            f"Dividir entre {fmt_num(coef)}",
            [f"Multiplicar por {fmt_num(coef)}", f"Restar {fmt_num(coef)}"],
            "Lo que multiplica a la x pasa DIVIDIENDO.",
            f"x = {right_final} ÷ {fmt_num(coef)}"))
        pasos.append(paso_numero(
            "¿Cuál es el valor de **x**?",
            x,
            f"x = {right_final} ÷ {fmt_num(coef)} = ?  Recuerda la regla de signos.",
            f"**x = {x}**"))

    return pasos


# ============================================================
#  EXPLICACIÓN COMPLETA (resumen final)
# ============================================================

def generar_explicacion(p):
    nivel = p['nivel']
    tipo = p['tipo']
    x = p['x']
    pasos = []

    if nivel == "Fácil":
        a = p['a']
        b = p['b']
        if tipo == 'x+a=b':
            pasos.append(f"**Ecuación:** x + {fmt_num(a)} = {b}")
            pasos.append(f"**Paso 1:** Restamos **{fmt_num(a)}** en ambos lados → x = {b} − {fmt_num(a)}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        elif tipo == 'x-a=b':
            pasos.append(f"**Ecuación:** x − {fmt_num(a)} = {b}")
            pasos.append(f"**Paso 1:** Sumamos **{fmt_num(a)}** en ambos lados → x = {b} + {fmt_num(a)}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        elif tipo == 'a+x=b':
            pasos.append(f"**Ecuación:** {a} + x = {b}")
            pasos.append(f"**Paso 1:** Restamos **{a}** en ambos lados → x = {b} − {fmt_num(a)}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        else:
            pasos.append(f"**Ecuación:** {a} − x = {b}")
            pasos.append(f"**Paso 1:** Sumamos **x** en ambos lados → {fmt_num(a)} = {b} + x")
            pasos.append(f"**Paso 2:** Restamos **{b}** en ambos lados → x = {fmt_num(a)} − {fmt_num(b)}")
            pasos.append(f"**Paso 3:** Resolvemos → **x = {x}**")

    elif nivel == "Medio":
        a, b, c = p['a'], p['b'], p['c']
        pasos.append(f"**Ecuación:** {formatear_ecuacion(p)}")

        if tipo in ('aX+b=c', 'aX-b=c', 'b+aX=c'):
            if tipo == 'aX-b=c':
                pasos.append(f"**Paso 1:** Sumamos {fmt_num(b)} en ambos lados → {ax_str(a)} = {c + b}")
                val = c + b
            else:
                pasos.append(f"**Paso 1:** Restamos {fmt_num(b)} en ambos lados → {ax_str(a)} = {c - b}")
                val = c - b
            pasos.append(f"**Paso 2:** Dividimos entre {fmt_num(a)} → x = {val} ÷ {fmt_num(a)}")
            pasos.append(f"**x = {x}**")
        else:  # b-aX=c
            pasos.append(f"**Paso 1:** Sumamos {ax_str(a)} en ambos lados → {fmt_num(b)} = {fmt_num(c)} + {ax_str(a)}")
            pasos.append(f"**Paso 2:** Restamos {fmt_num(c)} → {ax_str(a)} = {b - c}")
            pasos.append(f"**Paso 3:** Dividimos entre {fmt_num(a)} → x = {b - c} ÷ {fmt_num(a)}")
            pasos.append(f"**x = {x}**")

    else:  # Avanzado
        a, b, c, d = p['a'], p['b'], p['c'], p['d']
        coef = a - c
        pasos.append(f"**Ecuación:** {formatear_ecuacion(p)}")
        pasos.append(f"**Paso 1:** Restamos {ax_str(c)} en ambos lados → {ax_str(a)} − {ax_str(c)} = ...")
        pasos.append(f"**Paso 2:** Simplificamos → {ax_str(coef)}")
        pasos.append(f"**Paso 3:** Movemos el número al otro lado y simplificamos → "
                     f"{ax_str(coef)} = {coef * x}")
        pasos.append(f"**Paso 4:** Dividimos entre {fmt_num(coef)} → x = {coef * x} ÷ {fmt_num(coef)}")
        pasos.append(f"**x = {x}**")

    return pasos


# ============================================================
#  LÓGICA DE LA APP
# ============================================================

def nueva_ecuacion():
    """Genera una ecuación nueva con sus pasos guiados."""
    p = generar_ecuacion(rango, nivel)
    p['texto'] = formatear_ecuacion(p)
    p['pasos'] = construir_pasos(p)
    p['paso_actual'] = 0
    p['fallos_paso'] = 0
    p['todo_primera'] = True
    p['ver_pista'] = False
    p['bonus_ganado'] = False
    p['celebrar'] = False
    st.session_state.contador += 1
    p['key'] = st.session_state.contador
    st.session_state.problema_actual = p
    st.session_state.mostrar_solucion = False


# ---------- Botón generar ----------
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    if st.button("🎲 Generar Ecuación", use_container_width=True):
        nueva_ecuacion()
        st.rerun()

# Separador morado elegante
st.markdown("""
<hr style="
    border: none;
    height: 3px;
    background: linear-gradient(90deg, transparent 0%, #8e24aa 50%, transparent 100%);
    margin: 1.5rem 0;
    border-radius: 2px;
">
""", unsafe_allow_html=True)

# ============================================================
#  ZONA DE EJERCICIO
# ============================================================
if st.session_state.problema_actual is not None:
    problema = st.session_state.problema_actual

    if modo == "🪜 Modo Guiado":
        # ==================== MODO GUIADO ====================
        if not st.session_state.mostrar_solucion:
            n = len(problema['pasos'])
            i = problema['paso_actual']

            # Ecuación grande
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.markdown(f"## **{problema['texto']}**  →  **x = ?**")

            # Progreso
            st.progress(i / n)
            st.markdown(f"🪜 **Paso {i + 1} de {n}**")

            # Pasos ya resueltos
            for j in range(i):
                st.markdown(f"✅ {problema['pasos'][j]['resuelto_texto']}")

            paso = problema['pasos'][i]
            st.markdown(f"**{paso['pregunta']}**")

            if paso['tipo'] == 'opcion':
                entrada = st.radio(
                    "Elige una opción:",
                    paso['opciones'],
                    key=f"op_{problema['key']}_{i}",
                    index=None
                )
            else:
                entrada = st.number_input(
                    "Tu respuesta:",
                    value=None,
                    step=1,
                    key=f"num_{problema['key']}_{i}"
                )

            c1, c2 = st.columns(2)
            with c1:
                boton_check = st.button("✅ Comprobar", use_container_width=True)
            with c2:
                boton_pista = st.button("💡 Pista", use_container_width=True)

            if boton_pista:
                problema['ver_pista'] = True
            if problema['ver_pista']:
                st.info("💡 " + paso['pista'])

            if boton_check:
                if entrada is None:
                    st.warning("⚠️ Selecciona o escribe tu respuesta.")
                else:
                    st.session_state.total_intentos += 1
                    if entrada == paso['respuesta']:
                        if problema['fallos_paso'] > 0:
                            problema['todo_primera'] = False
                        problema['paso_actual'] += 1
                        problema['fallos_paso'] = 0
                        problema['ver_pista'] = False
                        if problema['paso_actual'] == n:
                            # ¡Ecuación completada!
                            st.session_state.puntos += 1
                            if problema['todo_primera']:
                                st.session_state.puntos += 1
                                problema['bonus_ganado'] = True
                            st.session_state.mostrar_solucion = True
                            problema['celebrar'] = True
                        st.rerun()
                    else:
                        problema['fallos_paso'] += 1
                        st.error("❌ ¡Casi! Revisa la operación e inténtalo de nuevo.")
                        if problema['fallos_paso'] >= 2:
                            problema['ver_pista'] = True
                        st.rerun()

        else:
            # ==================== COMPLETADA ====================
            if problema.get('celebrar'):
                st.balloons()
                problema['celebrar'] = False

            if problema['bonus_ganado']:
                st.success(f"🎉 ¡Ecuación resuelta! **x = {problema['x']}** "
                           f"· ⭐ ¡Todo a la primera! **+2 puntos**")
            else:
                st.success(f"🎉 ¡Ecuación resuelta! **x = {problema['x']}** · +1 punto")

            with st.expander("📖 Ver resumen de la solución", expanded=True):
                for linea in generar_explicacion(problema):
                    st.markdown(linea)
                st.info("💡 **Recuerda:** lo que haces de un lado de la ecuación, "
                        "debes hacerlo del otro (propiedad de la igualdad).")

            if st.button("🎲 Otra ecuación", use_container_width=True):
                nueva_ecuacion()
                st.rerun()

    else:
        # ==================== MODO RETO ====================
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(f"## **{problema['texto']}**  →  **x = ?**")

        respuesta = st.number_input(
            "Tu respuesta (valor de x):",
            value=None,
            placeholder="Escribe el valor de x...",
            step=1,
            key=f"resp_{problema['key']}"
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Comprobar", use_container_width=True):
                if respuesta is None:
                    st.warning("⚠️ Escribe un valor para x antes de comprobar.")
                else:
                    st.session_state.total_intentos += 1
                    if respuesta == problema['x']:
                        st.success(f"¡Correcto! 🎉 x = {problema['x']}")
                        st.session_state.puntos += 1
                        st.balloons()
                    else:
                        st.error(f"La respuesta correcta es x = {problema['x']}.")
                        st.info("💡 ¿Quieres repasar el procedimiento? Cambia al "
                                "**🪜 Modo Guiado** en el menú lateral.")
        with col2:
            if st.button("🔄 Otra ecuación", use_container_width=True):
                nueva_ecuacion()
                st.rerun()

# ============================================================
#  AYUDA: REGLAS DE TRANSPOSICIÓN
# ============================================================
with st.expander("📚 Reglas de transposición (Haz clic para aprender)"):
    st.markdown("""
    <div style="color: #4a148c; line-height: 1.7;">

    <h3 style="color: #4a148c !important;">🔀 Cómo pasar un término al otro lado</h3>

    <table style="width: 100%; border-collapse: collapse; color: #4a148c;">
      <tr style="background-color: #e1bee7;">
        <th style="padding: 8px; border: 1px solid #8e24aa; text-align: left;">Regla</th>
        <th style="padding: 8px; border: 1px solid #8e24aa; text-align: left;">Ejemplo</th>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          a) Cuando un término está <b>SUMANDO</b> en un miembro, pasa al otro miembro <b>RESTANDO</b>.
        </td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          <code>5x + 3 = 2x</code> → <code>5x = 2x − 3</code>
        </td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          b) Cuando un término está <b>RESTANDO</b> en un miembro, pasa al otro miembro <b>SUMANDO</b>.
        </td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          <code>5x = 2x − 3</code> → <code>5x − 2x = −3</code>
        </td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          c) Cuando un término está <b>MULTIPLICANDO</b> en un miembro, pasa al otro miembro
          <b>DIVIDIENDO</b> a todo el miembro.
        </td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          <code>5x = 10</code> → <code>x = 10 / 5</code>
        </td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          d) Cuando un término está <b>DIVIDIENDO</b> en un miembro, pasa al otro miembro
          <b>MULTIPLICANDO</b> a todo el miembro.
        </td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">
          <code>x / 4 = 3</code> → <code>x = 4 · 3 = 12</code>
        </td>
      </tr>
    </table>

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">⚖️ La regla de oro</h4>
    <blockquote style="border-left: 4px solid #8e24aa; padding-left: 12px; color: #4a148c;">
      <b>Lo que sumas, restas, multiplicas o divides de un lado de la ecuación,
      debes hacerlo también del otro lado.</b> Así se mantiene el equilibrio. ⚖️
    </blockquote>

    <h4 style="color: #4a148c !important;">✔️ Verifica tu respuesta</h4>
    Reemplaza <b>x</b> en la ecuación original y comprueba que ambos lados sean iguales.<br>
    Ejemplo: si resolviste <code>x + 3 = 8</code> y obtuviste <code>x = 5</code>:
    <code>5 + 3 = 8</code> ✅ ¡Correcto!

    </div>
    """, unsafe_allow_html=True)
