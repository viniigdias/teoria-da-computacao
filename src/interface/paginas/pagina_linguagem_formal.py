import streamlit as st
from src.modulos.linguagem_formal import LinguagemFormal


def exibir():
    st.title("Módulo 1 — Linguagens Formais")

    st.markdown("### Definir Alfabeto")
    entrada_alfabeto = st.text_input("Símbolos separados por vírgula", value="a, b")
    alfabeto = set(s.strip() for s in entrada_alfabeto.split(",") if s.strip())
    st.info(f"Σ = {{ {', '.join(sorted(alfabeto))} }}")

    st.markdown("---")
    st.markdown("### Validar Cadeia")
    cadeia = st.text_input("Informe uma cadeia", value="abba")

    if st.button("Analisar"):
        linguagem = LinguagemFormal(alfabeto)
        valida = linguagem.cadeia_pertence_ao_alfabeto(cadeia)
        tamanho = linguagem.tamanho_da_cadeia(cadeia)

        if valida:
            st.success(f"✅ Cadeia '{cadeia}' é válida para Σ")
        else:
            invalidos = [s for s in cadeia if s not in alfabeto]
            st.error(f"❌ Símbolos fora do alfabeto: {invalidos}")

        st.write(f"**Tamanho:** {tamanho}")

    st.markdown("---")
    st.markdown("### Concatenação")
    col1, col2 = st.columns(2)
    with col1:
        cadeia_a = st.text_input("Cadeia A", value="ab")
    with col2:
        cadeia_b = st.text_input("Cadeia B", value="ba")

    if st.button("Concatenar"):
        linguagem = LinguagemFormal(alfabeto)
        st.success(f"{cadeia_a} · {cadeia_b} = {linguagem.concatenar(cadeia_a, cadeia_b)}")

    st.markdown("---")
    st.markdown("### Σ* e Σ+")
    tamanho_maximo = st.slider("Tamanho máximo", 1, 4, 2)

    col3, col4 = st.columns(2)
    with col3:
        if st.button("Calcular Σ*"):
            linguagem = LinguagemFormal(alfabeto)
            resultado = linguagem.sigma_estrela(tamanho_maximo)
            st.markdown(f"**Σ\*** — {len(resultado)} cadeias")
            st.write(resultado)
    with col4:
        if st.button("Calcular Σ+"):
            linguagem = LinguagemFormal(alfabeto)
            resultado = linguagem.sigma_mais(tamanho_maximo)
            st.markdown(f"**Σ+** — {len(resultado)} cadeias")
            st.write(resultado)