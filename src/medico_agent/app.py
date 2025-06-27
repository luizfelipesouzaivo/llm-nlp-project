import streamlit as st
import os
from PIL import Image
from agent import Agent

st.set_page_config(page_title="Assistente Médico Virtual", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #eaf6fc;
    }
    .titulo {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #007BFF;
        margin-top: 20px;
    }
    .subtitulo {
        text-align: center;
        font-size: 16px;
        margin-bottom: 30px;
    }
    .response-box {
        background-color: #d9ecff;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .historico {
        font-size: 14px;
        color: #333;
        background-color: #f8f8f8;
        border-left: 5px solid #007BFF;
        padding: 10px;
        margin-top: 20px;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #00BFFF;
        color: white;
        padding: 12px 24px;
        border-radius: 6px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🤖🩺 Assistente Médico Virtual 🩺🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Digite sua dúvida médica e receba uma resposta segura e clara.</div>', unsafe_allow_html=True)

sugestoes = [
    "Estou com dor de cabeça, o que posso tomar?",
    "Estou com febre há dois dias, o que devo fazer?",
    "Tenho tosse seca e dor no corpo, é covid?",
    "Quais são os sintomas de dengue?",
    "Tive tontura hoje cedo, o que pode ser?"
]
st.selectbox("Sugestões de sintomas:", [""] + sugestoes, key="sugestao", on_change=lambda: st.session_state.update({"pergunta": st.session_state.sugestao}))

pergunta = st.text_area("Digite sua pergunta médica:", key="pergunta", height=120)

if "historico" not in st.session_state:
    st.session_state.historico = []

if st.button("Enviar") and pergunta.strip():
    agent = Agent()
    resposta = agent.get_tips(pergunta)
    st.markdown(f'<div class="response-box"><b>Resposta:</b><br>{resposta}</div>', unsafe_allow_html=True)
    st.session_state.historico.append((pergunta, resposta))

if st.session_state.historico:
    st.markdown("### Histórico de perguntas:")
    for i, (perg, resp) in enumerate(reversed(st.session_state.historico), 1):
        st.markdown(f"<div class='historico'><b>{i}. Pergunta:</b> {perg}<br><b>Resposta:</b> {resp}</div>", unsafe_allow_html=True)

st.markdown("""
<br><hr>
<div style="text-align: center; font-size: 12px; color: gray;">
As respostas são geradas por IA e têm caráter informativo. Consulte sempre um médico de verdade para diagnóstico e tratamento.
</div>
""", unsafe_allow_html=True)