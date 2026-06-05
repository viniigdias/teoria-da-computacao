import streamlit as st
from src.modulos.gramatica_livre_contexto import GramaticaLivreDeContexto


def exibir():
    st.title("Módulo 3 — Gramática Livre de Contexto")

    st.markdown("### Definir Gramática")

    col1, col2 = st.columns(2)
    with col1:
        variaveis = st.text_input("Variáveis (separadas por vírgula)", value="S")
        simbolo_inicial = st.text_input("Símbolo inicial", value="S")
    with col2:
        terminais = st.text_input("Terminais (separados por vírgula)", value="a, b")

    st.markdown("### Produções")
    st.caption("Uma produção por linha no formato:  S -> aSb  ou  S -> λ")
    producoes_texto = st.text_area("Produções", value="S -> aSb\nS -> λ", height=120)

    cadeia = st.text_input("Cadeia a derivar", value="aaabbb")

    if st.button("Derivar"):
        variaveis_set = set(v.strip() for v in variaveis.split(","))
        terminais_set = set(t.strip() for t in terminais.split(","))

        producoes = {}
        for linha in producoes_texto.strip().split("\n"):
            if "->" not in linha:
                continue
            esquerda, direita = linha.split("->")
            esquerda = esquerda.strip()
            opcoes = [d.strip().replace("λ", "") for d in direita.split("|")]
            producoes[esquerda] = opcoes

        gramatica = GramaticaLivreDeContexto(
            variaveis=variaveis_set,
            terminais=terminais_set,
            producoes=producoes,
            simbolo_inicial=simbolo_inicial.strip()
        )

        aceita, historico = gramatica.derivar(cadeia)

        st.markdown("### Derivação passo a passo")
        for i, passo in enumerate(historico):
            st.write(f"**Passo {i}:** `{passo if passo else 'λ (vazio)'}`")

        if aceita:
            st.success("✅ Cadeia ACEITA pela gramática")
        else:
            st.error("❌ Cadeia REJEITADA pela gramática")