import streamlit as st
import random

# ---------- Estilos personalizados: fondo morado suave ----------
st.markdown("""
<style>
    /* Fondo principal */
    .stApp {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 50%, #ede7f6 100%);
    }

    /* Tarjetas/contenedores legibles */
    [data-testid="stVerticalBlock"] > div:has(.stMarkdown),
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.78);
        border-radius: 12px;
        padding: 0.75rem 1rem;
    }

    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #6a1b9a 0%, #8e24aa 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Botones */
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

    /* ---------- FORZAR COLOR DE TEXTO EN ZONAS BLANCAS ---------- */
    .stApp p, .stApp li, .stApp span, .stApp label,
    .stApp div[data-testid="stMarkdownContainer"] {
        color: #4a148c;
    }

    /* Etiquetas de inputs */
    .stApp label,
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] p {
        color: #4a148c !important;
        font-weight: 600;
    }

    /* Texto dentro del input */
    input {
        background-color: #ffffff !important;
        color: #4a148c !important;
    }

    /* ---------- EXPANDER: contenedor y texto ---------- */
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

    /* Tablas dentro de expanders */
    div[data-testid="stExpander"] table,
    div[data-testid="stExpander"] th,
    div[data-testid="stExpander"] td {
        color: #4a148c !important;
        border-color: #8e24aa !important;
    }
    div[data-testid="stExpander"] th {
        background-color: #e1bee7 !important;
    }

    /* ---------- CORREGIR FONDOS NEGROS EN EXPANDERS Y CÓDIGO ---------- */

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

    /* Alertas */
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] div {
        color: #4a148c !important;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #4a148c !important;
    }
    div[data-testid="stMetric"] label {
        color: #4a148c !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Título centrado en una línea ----------
st.markdown(
    "<h1 style='text-align: center; font-size: 2rem; color: #4a148c; margin-bottom: 0.5rem;'>"
    "🧮 Ecuaciones de 1er Grado con Números Enteros"
    "</h1>",
    unsafe_allow_html=True
)

# ---------- Descripción ----------
st.markdown("""
<div style="
    color: #4a148c;
    font-size: 1.05rem;
    line-height: 1.75;
    text-align: justify;
    background-color: rgba(255, 255, 255, 0.85);
    padding: 1.25rem 1.75rem;
    border-radius: 14px;
    margin: 1rem 0 1.5rem 0;
    box-shadow: 0 2px 6px rgba(142, 36, 170, 0.12);
">
Aprende a <b>resolver ecuaciones en ℤ</b> (Números Enteros) Paso a Paso.
Una ecuación es una igualdad algebraica en la que aparecen letras (incógnitas) con valor
desconocido.
• El grado de una ecuación viene dado por el exponente mayor de la incógnita. En este tema
trabajamos con ecuaciones lineales (de grado 1) con una incógnita.
• Solucionar una ecuación es encontrar el valor o valores de las incógnitas que transforman la
ecuación en una identidad.🎯 

<ul style="margin-top: 0.6rem; margin-bottom: 0.6rem;">
  <li><b>Fácil</b>: la incógnita aparece sola → 
  <code>x + a = b</code>, <code>x − a = b</code>, <code>a + x = b</code>, <code>a − x = b</code></li>
  <li><b>Medio</b>: la incógnita tiene coeficiente → 
  <code>ax + b = c</code>, <code>ax − b = c</code>, <code>b + ax = c</code>, <code>b − ax = c</code></li>
  <li><b>Avanzado</b>: la incógnita aparece en ambos lados → 
  <code>ax + b = cx + d</code> y todas sus variantes de signos</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- Inicializar variables de sesión ----------
if 'puntos' not in st.session_state:
    st.session_state.puntos = 0
if 'total_intentos' not in st.session_state:
    st.session_state.total_intentos = 0
if 'problema_actual' not in st.session_state:
    st.session_state.problema_actual = None
if 'mostrar_solucion' not in st.session_state:
    st.session_state.mostrar_solucion = False


# ---------- Configuración en barra lateral ----------
with st.sidebar:
    st.header("⚙️ Configuración")

    nivel = st.radio(
        "Nivel:",
        ["Fácil", "Medio", "Avanzado"]
    )

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
# GENERADOR DE ECUACIONES (X primero, solución siempre entera)
# ============================================================

def generar_ecuacion(rango, nivel):
    """
    Genera una ecuación con solución entera garantizada.
    Se genera X primero y se construye la ecuación a partir de X.
    """

    # ========== NIVEL FÁCIL ==========
    if nivel == "Fácil":
        x = random.randint(-rango, rango)
        a = random.randint(-rango, rango)
        tipo = random.choice(['x+a=b', 'x-a=b', 'a+x=b', 'a-x=b'])

        if tipo == 'x+a=b':
            b = x + a
        elif tipo == 'x-a=b':
            b = x - a
        elif tipo == 'a+x=b':
            b = a + x
        else:  # a-x=b
            b = a - x

        return {'x': x, 'a': a, 'b': b, 'tipo': tipo, 'nivel': nivel}

    # ========== NIVEL MEDIO ==========
    elif nivel == "Medio":
        x = random.randint(-rango, rango)
        # Coeficiente a ≠ 0, con signo libre
        a = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        b = random.randint(-rango, rango)
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

    # ========== NIVEL AVANZADO ==========
    else:
        x = random.randint(-rango, rango)
        a = random.choice([i for i in range(-rango, rango + 1) if i != 0])
        # c ≠ 0 y c ≠ a (evita degeneración: ax + b = ax + d)
        c = random.choice([i for i in range(-rango, rango + 1) if i != 0 and i != a])
        b = random.randint(-rango, rango)
        # d se calcula para que la ecuación cierre con el X elegido
        d = (a - c) * x + b

        tipo = random.choice(['aX+b=cX+d', 'aX-b=cX+d', 'aX+b=cX-d', 'aX-b=cX-d'])

        return {'x': x, 'a': a, 'b': b, 'c': c, 'd': d, 'tipo': tipo, 'nivel': nivel}


# ============================================================
# FORMATEO DEL TEXTO DE LA ECUACIÓN (Opción C de paréntesis)
# ============================================================

def fmt_var(coef, primero=True):
    """Formatea un término con x.
    3, True   → '3x'
    3, False  → ' + 3x'
    -2, True  → '-2x'
    -2, False → ' - 2x'
    1, True   → 'x'
    1, False  → ' + x'
    -1, True  → '-x'
    -1, False → ' - x'
    """
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


def fmt_const(n, primero=True):
    """Formatea un término constante.
    primero=True:  5 → '5';  -3 → '-3'
    primero=False: 5 → ' + 5';  -3 → ' + (-3)'
    """
    if primero:
        return f"{n}"
    if n >= 0:
        return f" + {n}"
    else:
        return f" + ({n})"


def formatear_ecuacion(p):
    """Construye el texto de la ecuación según el nivel y tipo."""
    nivel = p['nivel']
    tipo = p['tipo']

    # ========== FÁCIL ==========
    if nivel == "Fácil":
        a = p['a']
        b = p['b']
        if tipo == 'x+a=b':
            return f"x + {a} = {b}" if a >= 0 else f"x + ({a}) = {b}"
        elif tipo == 'x-a=b':
            return f"x - {a} = {b}" if a >= 0 else f"x - ({a}) = {b}"
        elif tipo == 'a+x=b':
            return f"{a} + x = {b}"
        else:  # a-x=b
            return f"{a} - x = {b}"

    # ========== MEDIO ==========
    elif nivel == "Medio":
        a = p['a']       # coeficiente de x
        b = p['b']       # término constante
        c = p['c']       # resultado

        if tipo == 'aX+b=c':
            # ax + b = c
            izq = fmt_var(a, primero=True)
            izq += f" + {b}" if b >= 0 else f" + ({b})"
            return f"{izq} = {c}"
        elif tipo == 'aX-b=c':
            # ax - b = c
            izq = fmt_var(a, primero=True)
            izq += f" - {b}" if b >= 0 else f" - ({b})"
            return f"{izq} = {c}"
        elif tipo == 'b+aX=c':
            # b + ax = c
            der = fmt_var(a, primero=False)   # " + 3x" o " - 3x"
            if b >= 0:
                return f"{b}{der} = {c}"
            else:
                return f"({b}){der} = {c}"
        else:  # b-aX=c
            # b - ax = c
            if a >= 0:
                return f"{b} - {a}x = {c}"
            else:
                return f"{b} - ({a})x = {c}"

    # ========== AVANZADO ==========
    else:
        a = p['a']
        b = p['b']
        c = p['c']
        d = p['d']

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
# EXPLICACIÓN PASO A PASO
# ============================================================

def fmt_num(n):
    """Devuelve el número con paréntesis si es negativo: 5 → '5', -3 → '(-3)'"""
    return f"({n})" if n < 0 else f"{n}"


def generar_explicacion(p):
    """Devuelve una lista de pasos (strings markdown) según el tipo."""
    nivel = p['nivel']
    tipo = p['tipo']
    x = p['x']
    pasos = []

    # ========== FÁCIL ==========
    if nivel == "Fácil":
        a = p['a']
        b = p['b']

        if tipo == 'x+a=b':
            pasos.append(f"**Ecuación:** x + {fmt_num(a)} = {b}" if a < 0 else f"**Ecuación:** x + {a} = {b}")
            pasos.append(f"**Paso 1:** Restamos **{fmt_num(a)}** en ambos lados.")
            pasos.append(f"x = {b} - {fmt_num(a)}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        elif tipo == 'x-a=b':
            pasos.append(f"**Ecuación:** x - {fmt_num(a)} = {b}" if a < 0 else f"**Ecuación:** x - {a} = {b}")
            pasos.append(f"**Paso 1:** Sumamos **{fmt_num(a)}** en ambos lados.")
            pasos.append(f"x = {b} + {fmt_num(a)}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        elif tipo == 'a+x=b':
            pasos.append(f"**Ecuación:** {a} + x = {b}")
            pasos.append(f"**Paso 1:** Restamos **{a}** en ambos lados.")
            pasos.append(f"x = {b} - {a}")
            pasos.append(f"**Paso 2:** Resolvemos → **x = {x}**")
        else:  # a-x=b
            pasos.append(f"**Ecuación:** {a} - x = {b}")
            pasos.append(f"**Paso 1:** Pasamos x al otro lado: **{a} = {b} + x**")
            pasos.append(f"**Paso 2:** Restamos **{b}** en ambos lados: x = {a} - {b}")
            pasos.append(f"**Paso 3:** Resolvemos → **x = {x}**")

    # ========== MEDIO ==========
    elif nivel == "Medio":
        a = p['a']
        b = p['b']
        c = p['c']

        pasos.append(f"**Ecuación:** {formatear_ecuacion(p)}")

        if tipo in ('aX+b=c', 'aX-b=c'):
            # Aislamos el término con x
            if tipo == 'aX+b=c':
                pasos.append(f"**Paso 1:** Restamos {fmt_num(b)} en ambos lados.")
                pasos.append(f"{a}x = {c} - {fmt_num(b)}")
                pasos.append(f"{a}x = {c - b}")
            else:  # aX-b=c
                pasos.append(f"**Paso 1:** Sumamos {fmt_num(b)} en ambos lados.")
                pasos.append(f"{a}x = {c} + {fmt_num(b)}")
                pasos.append(f"{a}x = {c + b}")
            pasos.append(f"**Paso 2:** Dividimos ambos lados entre {fmt_num(a)}.")
            pasos.append(f"x = {c - b} ÷ {fmt_num(a)}")
            pasos.append(f"**x = {x}**")

        elif tipo == 'b+aX=c':
            pasos.append(f"**Paso 1:** Restamos {fmt_num(b)} en ambos lados.")
            pasos.append(f"{a}x = {c} - {fmt_num(b)}")
            pasos.append(f"{a}x = {c - b}")
            pasos.append(f"**Paso 2:** Dividimos ambos lados entre {fmt_num(a)}.")
            pasos.append(f"x = {c - b} ÷ {fmt_num(a)}")
            pasos.append(f"**x = {x}**")

        else:  # b-aX=c
            pasos.append(f"**Paso 1:** Pasamos el término con x al otro lado.")
            pasos.append(f"{fmt_num(b)} = {c} + {a}x" if a >= 0 else f"{fmt_num(b)} = {c} + ({a})x")
            pasos.append(f"**Paso 2:** Restamos {fmt_num(c)} en ambos lados.")
            pasos.append(f"{fmt_num(b)} - {fmt_num(c)} = {a}x" if a >= 0 else f"{fmt_num(b)} - {fmt_num(c)} = ({a})x")
            pasos.append(f"**Paso 3:** Dividimos ambos lados entre {fmt_num(a)}.")
            pasos.append(f"x = {b - c} ÷ {fmt_num(a)}")
            pasos.append(f"**x = {x}**")

    # ========== AVANZADO ==========
    else:
        a = p['a']
        b = p['b']
        c = p['c']
        d = p['d']

        pasos.append(f"**Ecuación:** {formatear_ecuacion(p)}")
        pasos.append(f"**Paso 1:** Agrupamos los términos con x en un lado y los números en el otro.")
        pasos.append(f"{a}x - ({c})x = {d} - ({b})" if (c < 0 or b < 0) else f"{a}x - {c}x = {d} - {b}")
        pasos.append(f"**Paso 2:** Simplificamos ambos lados.")
        pasos.append(f"({a - c})x = {d - b}")
        pasos.append(f"**Paso 3:** Dividimos ambos lados entre {fmt_num(a - c)}.")
        pasos.append(f"x = {d - b} ÷ {fmt_num(a - c)}")
        pasos.append(f"**x = {x}**")

    return pasos


# ============================================================
# LÓGICA DE LA APP
# ============================================================

def nueva_ecuacion():
    """Genera una ecuación nueva y limpia el estado."""
    problema = generar_ecuacion(rango, nivel)
    problema['texto'] = formatear_ecuacion(problema)
    st.session_state.problema_actual = problema
    st.session_state.mostrar_solucion = False


# ---------- Botón nuevo problema ----------
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🎲 Nueva ecuación", use_container_width=True):
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

# ---------- Mostrar problema activo ----------
if st.session_state.problema_actual:
    problema = st.session_state.problema_actual
    mostrar = st.session_state.mostrar_solucion

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if mostrar:
            st.markdown(f"## **{problema['texto']}**  ✅  →  **x = {problema['x']}**")
        else:
            st.markdown(f"## **{problema['texto']}**  →  **x = ?**")

    respuesta = st.number_input(
        "Tu respuesta (valor de x):",
        value=None,
        placeholder="Escribe el valor de x...",
        step=1,
        key=f"resp_{problema['texto']}_{st.session_state.total_intentos}"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Comprobar", use_container_width=True):
            if respuesta is None:
                st.warning("⚠️ Escribe un valor para x antes de comprobar.")
            else:
                st.session_state.total_intentos += 1
                if respuesta == problema['x']:
                    st.success(f"¡Correcto! 🎉 x = {problema['x']} hace verdadera la ecuación.")
                    st.session_state.puntos += 1
                    st.session_state.mostrar_solucion = True
                    st.balloons()
                else:
                    st.error(f"¡Ups! Intenta de nuevo. La respuesta correcta es x = {problema['x']}")
                    st.session_state.mostrar_solucion = True

    with col2:
        if st.button("🔄 Otra ecuación", use_container_width=True):
            nueva_ecuacion()
            st.rerun()

    # ---------- Explicación paso a paso ----------
    if mostrar:
        with st.expander("🔍 Ver explicación paso a paso", expanded=True):
            st.markdown(f"### ✏️ Despeje de la incógnita — Nivel {problema['nivel']}")
            for paso in generar_explicacion(problema):
                st.markdown(paso)

            st.info("💡 **Recuerda:** resolver una ecuación es encontrar el valor de **x** que hace verdadera la igualdad. Lo que haces de un lado, lo haces del otro (propiedad de la igualdad).")


# ============================================================
# AYUDA
# ============================================================

with st.expander("📚 ¿Cómo resolver ecuaciones con enteros? (Haz clic para aprender)"):
    st.markdown("""
    <div style="color: #4a148c; line-height: 1.7;">

    <h3 style="color: #4a148c !important;">Reglas básicas para resolver ecuaciones en ℤ</h3>

    Una <b>ecuación</b> es una igualdad donde hay un valor desconocido llamado <b>incógnita</b> (generalmente <b>x</b>).
    Resolverla significa encontrar el valor de <b>x</b> que hace verdadera la igualdad.
    En ℤ, <b>todas las soluciones son enteras</b>.

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">🔹 Nivel Fácil — la incógnita aparece sola</h4>

    <table style="width: 100%; border-collapse: collapse; color: #4a148c;">
      <tr style="background-color: #e1bee7;">
        <th style="padding: 8px; border: 1px solid #8e24aa; text-align: left;">Ecuación</th>
        <th style="padding: 8px; border: 1px solid #8e24aa; text-align: left;">¿Cómo despejar?</th>
        <th style="padding: 8px; border: 1px solid #8e24aa; text-align: left;">Ejemplo</th>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">x + a = b</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">Restar <b>a</b> en ambos lados</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">x + 3 = 8 → x = 8 − 3 = <b>5</b></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">x − a = b</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">Sumar <b>a</b> en ambos lados</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">x − 4 = 2 → x = 2 + 4 = <b>6</b></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">a + x = b</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">Restar <b>a</b> en ambos lados</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">7 + x = 10 → x = 10 − 7 = <b>3</b></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ce93d8;">a − x = b</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">x = a − b</td>
        <td style="padding: 8px; border: 1px solid #ce93d8;">9 − x = 4 → x = 9 − 4 = <b>5</b></td>
      </tr>
    </table>

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">🔹 Nivel Medio — la incógnita tiene coeficiente</h4>

    Primero <b>aísla</b> el término con x y luego <b>divide</b> entre el coeficiente:

    <ul>
      <li><code>3x + 5 = 20</code> → <code>3x = 20 − 5 = 15</code> → <code>x = 15 ÷ 3 = 5</code></li>
      <li><code>−2x − 3 = 9</code> → <code>−2x = 9 + 3 = 12</code> → <code>x = 12 ÷ (−2) = −6</code></li>
      <li><code>7 + 4x = −1</code> → <code>4x = −1 − 7 = −8</code> → <code>x = −8 ÷ 4 = −2</code></li>
      <li><code>5 − 3x = −4</code> → <code>5 = −4 + 3x</code> → <code>9 = 3x</code> → <code>x = 3</code></li>
    </ul>

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">🔹 Nivel Avanzado — la incógnita en ambos lados</h4>

    <b>Paso 1:</b> agrupa las x en un lado y los números en el otro.<br>
    <b>Paso 2:</b> simplifica ambos lados.<br>
    <b>Paso 3:</b> divide entre el coeficiente de x.<br><br>

    Ejemplo: 
    → <code>3x + 5 = −2x − 10</code><br>
    → <code>3x + 2x = −10 − 5</code><br>
    → <code>5x = −15</code><br>
    → <code>x = −15 ÷ 5 = −3</code>

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">🔹 La regla de oro</h4>
    <blockquote style="border-left: 4px solid #8e24aa; padding-left: 12px; color: #4a148c;">
      <b>Lo que sumas o restas de un lado de la ecuación, debes hacerlo también del otro lado.</b><br>
      Así se mantiene el equilibrio de la balanza. ⚖️
    </blockquote>

    <hr style="border: none; height: 1px; background: #ce93d8; margin: 1rem 0;">

    <h4 style="color: #4a148c !important;">🔹 Verificación</h4>
    Reemplaza <b>x</b> en la ecuación original y comprueba que ambos lados sean iguales.<br><br>
    Ejemplo: si resolviste <code>x + 3 = 8</code> y obtuviste <code>x = 5</code>:<br>
    <code>5 + 3 = 8</code> ✅ ¡Correcto!

    </div>
    """, unsafe_allow_html=True)
