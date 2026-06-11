import streamlit as st
from src.modulos.automato_com_pilha import AutomatoComPilha

def exibir() -> None:
    st.title("Módulo 4 — Autômato com Pilha")
    st.markdown("### Linguagem Mínima: L = {aⁿbⁿ | n ≥ 1}")
    
    cadeia = st.text_input("Cadeia de entrada", value="aabb").strip()

    if st.button("Executar Autômato"):
        if not cadeia:
            st.warning("⚠️ Insira uma cadeia válida.")
            return

        ap = AutomatoComPilha()
        aceita, historico = ap.executar(cadeia)

        st.markdown("### Rastreamento da Pilha")
        st.markdown("| Leitura | Estado | Conteúdo da Pilha |")
        st.markdown("| :--- | :--- | :--- |")
        for passo in historico:
            pilha_str = f"[{', '.join(passo['pilha'])}]"
            st.markdown(f"| `{passo['leitura']}` | `{passo['estado']}` | `{pilha_str}` |")

        st.markdown("---")
        if aceita:
            st.success("✅ CADEIA ACEITA")
        else:
            st.error("❌ CADEIA REJEITADA")