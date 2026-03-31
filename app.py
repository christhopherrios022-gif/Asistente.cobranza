import streamlit as st
import openai

# API KEY
openai.api_key = st.secrets["openai.api_key"]

# CONFIG
st.set_page_config(page_title="Asistente de Cobranza", layout="centered")

st.title("🤖 CloseDebtCoach - Asistente en Vivo")

# INPUT CLIENTE
st.subheader("📊 Datos del cliente")
nombre = st.text_input("Nombre")
deuda = st.text_input("Deuda")
mora = st.text_input("Días de mora")
perfil = st.selectbox("Perfil", ["alto", "medio", "bajo"])

# INPUT OBJECION
st.subheader("💬 Objeción del cliente")
objecion = st.text_area("Escribe lo que dice el cliente")

# BOTON
if st.button("Generar respuesta"):

    prompt = f"""
    Eres un experto en cobranza.

    Datos del cliente:
    Nombre: {nombre}
    Deuda: {deuda}
    Mora: {mora}
    Perfil: {perfil}

    Cliente dice: {objecion}

    Responde con:
    - 1 frase de cierre
    - 1 pregunta dirigida
    - corto y listo para llamada
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    respuesta = response["choices"][0]["message"]["content"]

    st.subheader("🗣️ Respuesta sugerida")
    st.success(respuesta)


