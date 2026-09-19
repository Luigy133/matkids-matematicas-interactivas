import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Suma y Resta de Enteros", 
    page_icon="🧮",
    layout="centered"
)

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
    else:
        num1 = random.randint(-rango, rango)
        num2 = random.randint(-rango, rango)
        operador = random.choice(['+', '-'])
    
    if operador == '+':
        resultado = num1 + num2
        operacion_texto = f"{num1} + {num2}"
    else:
        resultado = num1 - num2
        operacion_texto = f"{num1} - {num2}"
    
    return num1, num2, operador, resultado, operacion_texto

def dibujar_recta_numerica(inicio, paso, resultado, num1, num2, operador):
    fig, ax = plt.subplots(figsize=(10, 3))
    min_val = min(-10, inicio, resultado) - 2
    max_val = max(10, inicio, resultado) + 2
    
    ax.axhline(y=0, color='black', linewidth=1)
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(-0.5, 0.5)
    
    for x in range(int(min_val), int(max_val) + 1):
        if x == 0:
            ax.plot(x, 0, 'ko', markersize=8)
            ax.text(x, -0.1, str(x), ha='center', fontsize=10, fontweight='bold')
        else:
            ax.plot(x, 0, 'ko', markersize=4)
            ax.text(x, -0.1, str(x), ha='center', fontsize=8)
    
    ax.plot(inicio, 0, 'go', markersize=15, label='Inicio', zorder=5)
    ax.text(inicio, 0.1, f'Inicio: {inicio}', ha='center', fontsize=9, color='green')
    
    if operador == '+':
        ax.arrow(inicio, 0.05, paso, 0, head_width=0.1, head_length=0.3, fc='blue', ec='blue', length_includes_head=True, label=f'Sumar {paso}')
    else:
        ax.arrow(inicio, 0.05, -paso, 0, head_width=0.1, head_length=0.3, fc='red', ec='red', length_includes_head=True, label=f'Restar {paso}')
    
    ax.plot(resultado, 0, 'ro', markersize=15, label='Resultado', zorder=5)
    ax.text(resultado, -0.2, f'¿{resultado}?', ha='center', fontsize=9, color='red')
    
    ax.text(0, 0.3, f"{num1} {operador} {paso} = ?", ha='center', fontsize=14, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow"))
    ax.set_title(f"Operación: {num1} {operador} {paso}", fontsize=14)
    ax.set_xlabel("Recta numérica", fontsize=12)
    ax.set_yticks([])
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    return fig

if st.button("🎲 Nuevo problema", use_container_width=True):
    num1, num2, operador, resultado, operacion_texto = generar_problema(rango, nivel)
    st.session_state.problema_actual = {
        'num1': num1,
        'num2': num2,
        'operador': operador,
        'resultado': resultado,
        'operacion_texto': operacion_texto
    }

if st.session_state.problema_actual:
    problema = st.session_state.problema_actual
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"## **{problema['operacion_texto']} = ?**")
    
    fig = dibujar_recta_numerica(problema['num1'], abs(problema['num2']), problema['resultado'], problema['num1'], abs(problema['num2']), problema['operador'])
    st.pyplot(fig)
    plt.close(fig)
    
    respuesta = st.number_input("Tu respuesta:", value=None, placeholder="Escribe el resultado...", step=1)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Comprobar", use_container_width=True):
            st.session_state.total_intentos += 1
            if respuesta == problema['resultado']:
                st.success(f"¡Correcto! 🎉 {problema['operacion_texto']} = {problema['resultado']}")
                st.session_state.puntos += 1
                st.balloons()
            else:
                st.error(f"¡Ups! Intenta de nuevo. La respuesta correcta es {problema['resultado']}")
                with st.expander("🔍 Ver explicación"):
                    if problema['operador'] == '+':
                        st.write(f"Desde {problema['num1']}, sumamos {problema['num2']} → nos movemos {problema['num2']} pasos a la derecha → {problema['resultado']}")
                    else:
                        st.write(f"Desde {problema['num1']}, restamos {problema['num2']} → nos movemos {problema['num2']} pasos a la izquierda → {problema['resultado']}")
    
    with col2:
        if st.button("🔄 Nuevo problema", use_container_width=True):
            num1, num2, operador, resultado, operacion_texto = generar_problema(rango, nivel)
            st.session_state.problema_actual = {'num1': num1, 'num2': num2, 'operador': operador, 'resultado': resultado, 'operacion_texto': operacion_texto}
            st.rerun()

with st.expander("📚 ¿Cómo funciona? (Haz clic para aprender)"):
    st.markdown("""
    ### Reglas básicas de los números enteros:
    - ➡️ **Sumar** te mueve a la **derecha**
    - ⬅️ **Restar** te mueve a la **izquierda**
    """)
