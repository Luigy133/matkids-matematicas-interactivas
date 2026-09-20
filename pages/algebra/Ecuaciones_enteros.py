import streamlit as st
import random
import matplotlib.pyplot as plt

# ---------- Estilos personalizados: fondo morado suave ----------
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
    /* Quitar fondo blanco alrededor de los botones */
    div[data-testid="stButton"] {
        background: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    input {
        background-color: #ffffff !important;
    }
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
    "🧮 Ecuaciones con Números Enteros"
    "</h1>",
    unsafe_allow_html=True
)

# ---------- Descripción con color legible ----------
st.markdown("""
<div style="color: #4a148c; font-size: 1.05rem; line-height: 1.6;">
Aprende a <b>resolver ecuaciones</b> con números enteros usando la recta numérica.
El objetivo es encontrar el valor de <b>x</b> que hace verdadera la igualdad:
<ul>
  <li><b>x + a = b</b> → despejas restando <i>a</i> en ambos lados</li>
  <li><b>x − a = b</b> → despejas sumando <i>a</i> en ambos lados</li>
  <li><b>a + x = b</b> → igual que el primer caso</li>
  <li><b>a − x = b</b> → ¡cuidado con el signo de x!</li>
</ul>
Cada solución la <b>visualizamos</b> en la recta numérica para que comprendas el porqué. 🎯
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

    rango = st.slider(
        "Rango de números:",
        min_value=1, max_value=20, value=10,
        help="Los números estarán entre -rango y +rango"
    )

    nivel = st.radio(
        "Dificultad:",
        ["Fácil", "Medio", "Avanzado"]
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


# ---------- Funciones ----------
def generar_ecuacion(rango, nivel):
    """Genera una ecuación del tipo x+a=b, x-a=b, a+x=b, a-x=b."""

    if nivel == "Fácil (solo positivos)":
        x = random.randint(1, rango)
        a = random.randint(1, rango)
        tipo = random.choice(['x+a=b', 'x-a=b', 'a+x=b', 'a-x=b'])
        if tipo == 'x+a=b':
            b = x + a
        elif tipo == 'x-a=b':
            b = x - a
        elif tipo == 'a+x=b':
            b = a + x
        else:
            b = a - x
        if b < 0:
            tipo = 'x+a=b'
            b = x + a

    elif nivel == "Medio (con negativos)":
        x = random.randint(-rango, rango)
        a = random.randint(-rango, rango)
        tipo = random.choice(['x+a=b', 'x-a=b', 'a+x=b', 'a-x=b'])

    else:  # Difícil
        x = random.randint(-rango, rango)
        a = random.randint(-rango, rango)
        tipo = random.choice(['x+a=b', 'x-a=b', 'a+x=b', 'a-x=b'])

    if tipo == 'x+a=b':
        b = x + a
        texto = f"x + ({a})" if a < 0 else f"x + {a}"
        texto += " = " + (f"({b})" if b < 0 else f"{b}")
    elif tipo == 'x-a=b':
        b = x - a
        texto = f"x - ({a})" if a < 0 else f"x - {a}"
        texto += " = " + (f"({b})" if b < 0 else f"{b}")
    elif tipo == 'a+x=b':
        b = a + x
        texto = f"({a}) + x" if a < 0 else f"{a} + x"
        texto += " = " + (f"({b})" if b < 0 else f"{b}")
    else:  # a-x=b
        b = a - x
        texto = f"({a}) - x" if a < 0 else f"{a} - x"
        texto += " = " + (f"({b})" if b < 0 else f"{b}")

    return {
        'x': x,
        'a': a,
        'b': b,
        'tipo': tipo,
        'texto': texto,
    }


def dibujar_recta_ecuacion(x_sol, a, b, tipo, mostrar_resultado=False):
    """Visualiza la ecuación en la recta numérica."""
    fig, ax = plt.subplots(figsize=(10, 3.2))
    fig.patch.set_facecolor('#f3e5f5')
    ax.set_facecolor('#faf0fb')

    valores = [x_sol, a, b, 0]
    min_val = min(valores) - 3
    max_val = max(valores) + 3

    ax.axhline(y=0, color='#4a148c', linewidth=1.5)
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(-0.9, 0.9)

    for v in range(int(min_val), int(max_val) + 1):
        if v == 0:
            ax.plot(v, 0, 'ko', markersize=8)
            ax.text(v, -0.18, str(v), ha='center', fontsize=10, fontweight='bold')
        else:
            ax.plot(v, 0, 'ko', markersize=4)
            ax.text(v, -0.18, str(v), ha='center', fontsize=8)

    if mostrar_resultado:
        ax.plot(x_sol, 0, 'o', color='#8e24aa', markersize=16,
                label=f'x = {x_sol}', zorder=5)
        ax.text(x_sol, 0.30, f'x = {x_sol}', ha='center',
                fontsize=11, color='#4a148c', fontweight='bold')
    else:
        ax.plot(x_sol, 0, 'o', markersize=16, color='#ce93d8',
                markerfacecolor='none', linestyle='None',
                label='¿Cuánto vale x?', zorder=5)
        ax.text(x_sol, 0.30, 'x = ?', ha='center',
                fontsize=11, color='#8e24aa', fontweight='bold')

    if a != x_sol:
        ax.plot(a, 0, 's', color='#ff9800', markersize=10,
                label=f'a = {a}', zorder=4)
        ax.text(a, -0.42, f'a = {a}', ha='center',
                fontsize=9, color='#e65100')

    if b != x_sol and b != a:
        ax.plot(b, 0, '^', color='#1976d2', markersize=10,
                label=f'b = {b}', zorder=4)
        ax.text(b, 0.55, f'b = {b}', ha='center',
                fontsize=9, color='#0d47a1')

    if mostrar_resultado:
        if tipo == 'x+a=b':
            color = '#8e24aa'
            ax.annotate('', xy=(x_sol, 0.15), xytext=(b, 0.15),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
            ax.text((x_sol + b) / 2, 0.22,
                    f'x = b − a = {b} − ({a}) = {x_sol}',
                    ha='center', fontsize=9, color=color)
        elif tipo == 'x-a=b':
            color = '#8e24aa'
            ax.annotate('', xy=(x_sol, 0.15), xytext=(b, 0.15),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
            ax.text((x_sol + b) / 2, 0.22,
                    f'x = b + a = {b} + ({a}) = {x_sol}',
                    ha='center', fontsize=9, color=color)
        elif tipo == 'a+x=b':
            color = '#8e24aa'
            ax.annotate('', xy=(x_sol, 0.15), xytext=(b, 0.15),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
            ax.text((x_sol + b) / 2, 0.22,
                    f'x = b − a = {b} − ({a}) = {x_sol}',
                    ha='center', fontsize=9, color=color)
        else:
            color = '#d32f2f'
            ax.annotate('', xy=(x_sol, 0.15), xytext=(b, 0.15),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
            ax.text((x_sol + b) / 2, 0.22,
                    f'x = a − b = {a} − ({b}) = {x_sol}',
                    ha='center', fontsize=9, color=color)

    # ✅ Cambio 4: sin título largo, solo la etiqueta del eje
    ax.set_xlabel("Recta numérica", fontsize=11, color='#4a148c')
    ax.set_yticks([])
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3, axis='x')

    plt.tight_layout()
    return fig


def nueva_ecuacion():
    """Genera una ecuación nueva y limpia el estado."""
    problema = generar_ecuacion(rango, nivel)
    st.session_state.problema_actual = problema
    st.session_state.mostrar_solucion = False


# ---------- Botón nuevo problema (centrado y más compacto) ----------
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🎲 Nueva ecuación", use_container_width=True):
        nueva_ecuacion()
        st.rerun()

# ✅ Cambio 3: separador morado elegante en lugar del recuadro blanco
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

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if mostrar:
            st.markdown(f"## **{problema['texto']}**  ✅  →  **x = {problema['x']}**")
        else:
            st.markdown(f"## **{problema['texto']}**  →  **x = ?**")

    fig = dibujar_recta_ecuacion(
        x_sol=problema['x'],
        a=problema['a'],
        b=problema['b'],
        tipo=problema['tipo'],
        mostrar_resultado=mostrar
    )
    st.pyplot(fig)
    plt.close(fig)

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
            a = problema['a']
            b = problema['b']
            x = problema['x']
            tipo = problema['tipo']

            st.markdown("### ✏️ Despeje de la incógnita")

            if tipo == 'x+a=b':
                st.write(f"**Ecuación:** x + ({a}) = ({b})" if (a < 0 or b < 0) else f"**Ecuación:** x + {a} = {b}")
                st.write(f"**Paso 1:** Restamos **{a}** en ambos lados.")
                st.write(f"x = {b} − ({a})" if a < 0 else f"x = {b} − {a}")
                st.write(f"**Paso 2:** Resolvemos → **x = {x}**")

            elif tipo == 'x-a=b':
                st.write(f"**Ecuación:** x − ({a}) = ({b})" if (a < 0 or b < 0) else f"**Ecuación:** x − {a} = {b}")
                st.write(f"**Paso 1:** Sumamos **{a}** en ambos lados.")
                st.write(f"x = {b} + ({a})" if a < 0 else f"x = {b} + {a}")
                st.write(f"**Paso 2:** Resolvemos → **x = {x}**")

            elif tipo == 'a+x=b':
                st.write(f"**Ecuación:** ({a}) + x = ({b})" if (a < 0 or b < 0) else f"**Ecuación:** {a} + x = {b}")
                st.write(f"**Paso 1:** Restamos **{a}** en ambos lados.")
                st.write(f"x = {b} − ({a})" if a < 0 else f"x = {b} − {a}")
                st.write(f"**Paso 2:** Resolvemos → **x = {x}**")

            else:  # a-x=b
                st.write(f"**Ecuación:** ({a}) − x = ({b})" if (a < 0 or b < 0) else f"**Ecuación:** {a} − x = {b}")
                st.write(f"**Paso 1:** Pasamos x al otro lado: **{a} = {b} + x**")
                st.write(f"**Paso 2:** Restamos **{b}** en ambos lados: x = {a} − ({b})" if b < 0 else f"**Paso 2:** Restamos **{b}** en ambos lados: x = {a} − {b}")
                st.write(f"**Paso 3:** Resolvemos → **x = {x}**")

            st.info("💡 **Recuerda:** resolver una ecuación es encontrar el valor de **x** que hace verdadera la igualdad. Lo que haces de un lado, lo haces del otro (propiedad de la igualdad).")

# ---------- Sección de ayuda ----------
with st.expander("📚 ¿Cómo resolver ecuaciones con enteros? (Haz clic para aprender)"):
    st.markdown("""
    ### Reglas básicas para resolver ecuaciones con números enteros

    Una **ecuación** es una igualdad donde hay un valor desconocido llamado **incógnita** (generalmente **x**).
    Resolverla significa encontrar el valor de **x** que hace verdadera la igualdad.

    ---

    #### 🔹 Tipos comunes de ecuaciones

    | Ecuación | ¿Cómo despejar? | Ejemplo |
    |----------|-----------------|---------|
    | x + a = b | Restar **a** en ambos lados → x = b − a | x + 3 = 8 → x = 8 − 3 = **5** |
    | x − a = b | Sumar **a** en ambos lados → x = b + a | x − 4 = 2 → x = 2 + 4 = **6** |
    | a + x = b | Igual que el primero → x = b − a | 7 + x = 10 → x = 10 − 7 = **3** |
    | a − x = b | x = a − b | 9 − x = 4 → x = 9 − 4 = **5** |

    ---

    #### 🔹 Con números negativos

    - `x + (−3) = 5` → **x = 5 − (−3) = 5 + 3 = 8**
    - `x − (−2) = 1` → **x = 1 + (−2) = −1**
    - `−4 + x = −10` → **x = −10 − (−4) = −10 + 4 = −6**
    - `−5 − x = 2` → **x = −5 − 2 = −7**

    ---

    #### 🔹 La regla de oro

    > **Lo que sumas o restas de un lado de la ecuación, debes hacerlo también del otro lado.**

    Así se mantiene el equilibrio de la balanza. ⚖️

    ---

    #### 🔹 Verificación

    Siempre puedes **verificar** tu solución: reemplaza **x** en la ecuación original
    y comprueba que ambos lados sean iguales.

    Ejemplo: si resolviste `x + 3 = 8` y obtuviste `x = 5`:
    `5 + 3 = 8` ✅ ¡Correcto!
    """)
