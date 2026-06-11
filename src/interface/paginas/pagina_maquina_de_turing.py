import streamlit as st
from src.modulos.maquina_de_turing import MaquinaDeTuring

def exibir():
    st.title("Módulo 5 — Máquina de Turing")
    st.markdown("### Opção B: Soma de representação unária")
    st.info("Exemplo: Para somar 3 + 2, insira `000100`")
    
    cadeia = st.text_input("Fita Inicial", value="000100")

    if st.button("Executar MT"):
        mt = MaquinaDeTuring()
        aceita, historico, resultado = mt.somar_unario(cadeia)

        st.markdown("### Fita em Execução")
        
        for frame in historico:
            fita_str = ""
            for i, sim in enumerate(frame["fita"]):
                if i == frame["cabecote"]:
                    fita_str += f" **[{sim}]** "
                else:
                    fita_str += f" {sim} "
            
            st.write(f"**Estado:** `{frame['estado']}` | **Fita:** {fita_str}")

        st.markdown("---")
        if aceita:
            st.success(f"✅ Execução Finalizada! Resultado: **{resultado}**")
        else:
            st.error("❌ Erro na execução da fita.")