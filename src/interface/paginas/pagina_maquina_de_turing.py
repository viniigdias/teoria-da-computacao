import streamlit as st
from src.modulos.maquina_de_turing import MaquinaDeTuring

def exibir() -> None:
    st.title("Módulo 5 — Máquina de Turing")
    st.markdown("### Opção B: Soma em Representação Unária")
    st.info("Formato esperado: Zeros, o caractere '1' como separador, e os zeros do segundo operando (Ex: `000100`).")
    
    cadeia = st.text_input("Fita Inicial", value="000100").strip()

    if st.button("Executar Máquina de Turing"):
        if "1" not in cadeia:
            st.error("❌ Entrada Inválida: A representação unária exige o caractere separador '1' (ex: '000100').")
            return

        mt = MaquinaDeTuring()
        aceita, historico, resultado = mt.somar_unario(cadeia)

        st.markdown("### Processamento da Fita")
        for frame in historico:
            fita_html = ""
            for i, sim in enumerate(frame["fita"]):
                if i == frame["cabecote"]:
                    fita_html += f"<span style='background-color:#4CAF50; color:white; padding: 2px 6px; margin: 2px; border-radius: 4px;'><b>{sim}</b></span>"
                else:
                    fita_html += f"<span style='background-color:#f0f2f6; color:black; padding: 2px 6px; margin: 2px; border-radius: 4px;'>{sim}</span>"
            
            st.markdown(f"**Estado:** `{frame['estado']}` | **Fita:** {fita_html}", unsafe_allow_html=True)

        st.markdown("---")
        if aceita:
            st.success(f"✅ Execução Finalizada! Resultado da soma unária: **{resultado}**")
        else:
            st.error("❌ Erro na execução da fita.")