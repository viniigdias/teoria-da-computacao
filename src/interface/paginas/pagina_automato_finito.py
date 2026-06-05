import streamlit as st
import json
from src.modulos.automato_finito import AutomatoFinito


def exibir():
    st.title("Modulo 2 — Autômato Finito")

    st.markdown("### Carregar Autômato via JSON")

    exemplo = {
        "estados": ["q0", "q1", "q2"],
        "estado_inicial": "q0",
        "estados_finais": ["q2"],
        "transicoes": {
            "q0,a": "q1",
            "q1,b": "q2"
        }
    }

    json_entrada = st.text_area(
        "Cole o JSON do autômato",
        value=json.dumps(exemplo, indent=2),
        height=220
    )

    cadeia = st.text_input("Cadeia de entrada", value="ab")

    if st.button("Executar"):
        try:
            dados = json.loads(json_entrada)

            transicoes = {
                tuple(chave.split(",")): destino
                for chave, destino in dados["transicoes"].items()
            }

            automato = AutomatoFinito(
                estados=dados["estados"],
                estado_inicial=dados["estado_inicial"],
                estados_finais=dados["estados_finais"],
                transicoes=transicoes
            )

            aceita, historico = automato.executar(cadeia)

            st.markdown("### Resultado")
            st.write(" → ".join(historico))

            if aceita:
                st.success("✅ ACEITA")
            else:
                st.error("❌ REJEITA")

        except Exception as erro:
            st.error(f"Erro no JSON: {erro}")

    st.markdown("---")
    st.markdown("### Como montar o JSON")
    st.markdown("""
    - **estados**: lista de todos os estados  
    - **estado_inicial**: estado de entrada  
    - **estados_finais**: lista de estados de aceitação  
    - **transicoes**: `"estado,simbolo": "proximo_estado"`
    """)