import streamlit as st

from src.modulos.complexidade_computacional import ComplexidadeComputacional


def exibir():
    st.title("Complexidade Computacional")

    st.write("Análise assintótica dos algoritmos implementados.")

    complexidade = ComplexidadeComputacional()
    dados = complexidade.listar()

    modulo = st.selectbox("Escolha o módulo:", list(dados.keys()))
    info = dados[modulo]

    st.subheader(modulo)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Melhor caso", info["melhor_caso"])

    with col2:
        st.metric("Caso médio", info["caso_medio"])

    with col3:
        st.metric("Pior caso", info["pior_caso"])

    st.subheader("Explicação")

    explicacoes = {
        "Linguagem Formal":
            "Percorre a cadeia para verificar se os símbolos pertencem ao alfabeto.",

        "Autômato Finito":
            "Lê a cadeia uma vez, mudando de estado a cada símbolo.",

        "Gramática Livre de Contexto":
            "Realiza derivações usando as produções da gramática até gerar ou rejeitar a cadeia.",

        "Autômato com Pilha":
            "Percorre a cadeia uma vez, empilhando os a's e desempilhando para os b's.",

        "Máquina de Turing":
            "Percorre a fita procurando o separador e remove esse símbolo para formar a soma unária."
    }

    st.write(explicacoes[modulo])

    st.subheader("Notações")

    st.write("**$O()$**: pior caso")
    st.write("**$\Omega()$**: melhor caso")
    st.write("**$\Theta()$**: caso médio")