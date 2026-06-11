import streamlit as st
from src.modulos.automato_com_pilha import AutomatoComPilha

def exibir():
    st.title("Módulo 4 — Autômato com Pilha")
    st.markdown("### Linguagem: L = {aⁿbⁿ | n ≥ 1}")
    
    cadeia = st.text_input("Cadeia de entrada (ex: aabb)", value="aabb")

    if st.button("Executar"):
        ap = AutomatoComPilha()
        aceita, historico = ap.executar(cadeia)

        st.markdown("### Execução Passo a Passo")
        
        st.markdown("| Leitura | Estado | Pilha |")
        st.markdown("| :--- | :--- | :--- |")
        for passo in historico:
            pilha_str = f"[{', '.join(passo['pilha'])}]"
            st.markdown(f"| `{passo['leitura']}` | `{passo['estado']}` | `{pilha_str}` |")

        st.markdown("---")
        if aceita:
            st.success("✅ ACEITA - A cadeia pertence à linguagem.")
        else:
            st.error("❌ REJEITADA - A cadeia não pertence à linguagem ou a pilha não esvaziou.")