import streamlit as st
import json
from src.modulos.automato_finito import AutomatoFinito

def exibir() -> None:
    st.title("Módulo 2 — Autômato Finito")
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

    json_entrada = st.text_area("Cole o JSON do autômato", value=json.dumps(exemplo, indent=2), height=220)
    cadeia = st.text_input("Cadeia de entrada", value="ab").strip()

    if st.button("Executar"):
        try:
            dados = json.loads(json_entrada)
            transicoes = {}
            for chave, destino in dados["transicoes"].items():
                partes = chave.split(",")
                if len(partes) != 2:
                    raise ValueError(f"A chave de transição '{chave}' deve conter exatamente uma vírgula separando o estado do símbolo (ex: 'q0,a').")
                transicoes[tuple(partes)] = destino

            automato = AutomatoFinito(
                estados=dados["estados"],
                estado_inicial=dados["estado_inicial"],
                estados_finais=dados["estados_finais"],
                transicoes=transicoes
            )

            aceita, historico, passos = automato.executar(cadeia)

            st.markdown("### Resultado do Processamento")
            st.write(" → ".join([f"`{e}`" for e in historico]))

            if aceita:
                st.success("✅ ACEITA")
            else:
                st.error("❌ REJEITA")

        except json.JSONDecodeError as e:
            st.error(f"❌ JSON Inválido: {e.msg} (Linha {e.lineno}, Coluna {e.colno})")
        except (KeyError, ValueError) as e:
            st.error(f"❌ Erro de Estrutura Teórica no JSON: {e}")
        except Exception as e:
            st.error(f"❌ Erro inesperado: {e}")