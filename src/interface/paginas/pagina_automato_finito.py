import json
import streamlit as st

from src.modulos.automato_finito import AutomatoFinito


def exibir():
    st.title("Autômato Finito")

    st.write("Carregue um AFD por JSON e execute uma cadeia.")

    exemplo_json = """
{
    "estados": ["q0", "q1", "q2"],
    "estado_inicial": "q0",
    "estados_finais": ["q2"],
    "transicoes": {
        "q0,a": "q1",
        "q1,b": "q2"
    }
}
"""

    texto_json = st.text_area("JSON do autômato:", value=exemplo_json, height=220)
    cadeia = st.text_input("Digite a cadeia:", "ab")

    if st.button("Executar Autômato"):
        try:
            dados = json.loads(texto_json)

            transicoes = {}
            for chave, destino in dados["transicoes"].items():
                estado, simbolo = chave.split(",")
                transicoes[(estado, simbolo)] = destino

            automato = AutomatoFinito(
                dados["estados"],
                dados["estado_inicial"],
                dados["estados_finais"],
                transicoes
            )

            aceita, historico, passos = automato.executar(cadeia)

            st.success("Cadeia ACEITA") if aceita else st.error("Cadeia REJEITADA")

            st.subheader("Caminho percorrido")
            st.code(" -> ".join(historico))

            st.subheader("Passo a passo")
            for passo in passos:
                st.write(passo)

        except Exception as erro:
            st.error("Erro ao carregar o JSON.")
            st.write(erro)