import streamlit as st

from src.modulos.gramatica_livre_contexto import GramaticaLivreDeContexto


def exibir():
    st.title("Gramática Livre de Contexto")

    st.write("Gramática utilizada:")
    st.code("S -> aSb\nS -> λ")

    cadeia = st.text_input("Digite a cadeia:", "aaabbb")

    variaveis = ["S"]
    terminais = ["a", "b"]
    producoes = {
        "S": ["aSb", "λ"]
    }

    if st.button("Executar Gramática"):
        glc = GramaticaLivreDeContexto(
            variaveis,
            terminais,
            producoes,
            "S"
        )

        aceita, historico, arvore = glc.derivar(cadeia)

        st.success("Cadeia ACEITA") if aceita else st.error("Cadeia REJEITADA")

        st.subheader("Derivação passo a passo")
        st.code(" -> ".join(historico))

        st.subheader("Árvore de derivação simplificada")

        for passo in arvore:
            st.write(
                f"{passo['antes']} ⇒ {passo['depois']} "
                f"usando {passo['variavel']} -> {passo['regra']}"
            )

            if "motivo" in passo:
                st.caption(passo["motivo"])