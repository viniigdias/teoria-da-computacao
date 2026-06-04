import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
from src.interface.paginas import pagina_linguagem_formal
from src.interface.paginas import pagina_automato_finito
from src.interface.paginas import pagina_gramatica
from src.interface.paginas import pagina_automato_com_pilha
from src.interface.paginas import pagina_maquina_de_turing
from src.interface.paginas import pagina_complexidade

st.set_page_config(
    page_title="Simulador — Teoria da Computação",
    page_icon="🖥️",
    layout="wide"
)

paginas = {
    "Linguagens Formais":          pagina_linguagem_formal,
    "Autômato Finito":             pagina_automato_finito,
    "Gramática Livre de Contexto": pagina_gramatica,
    "Autômato com Pilha":          pagina_automato_com_pilha,
    "Máquina de Turing":           pagina_maquina_de_turing,
    "Complexidade Computacional":  pagina_complexidade,
}

st.sidebar.title("🖥️ Teoria da Computação")
st.sidebar.markdown("Simulador de Modelos Computacionais")
st.sidebar.markdown("---")

selecao = st.sidebar.radio("Módulos", list(paginas.keys()))
paginas[selecao].exibir()