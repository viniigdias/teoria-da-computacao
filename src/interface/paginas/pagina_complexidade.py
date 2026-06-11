import streamlit as st
from src.modulos.complexidade_computacional import ComplexidadeComputacional

def exibir() -> None:
    st.title("Complexidade Computacional")
    st.write("Análise assintótica formal dos algoritmos implementados no simulador.")

    complexidade = ComplexidadeComputacional()
    dados = complexidade.listar()

    modulo = st.selectbox("Escolha o módulo para inspecionar:", list(dados.keys()))
    info = dados[modulo]

    st.subheader(f"Módulo: {modulo}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Melhor Caso", info["melhor_caso"])
    with col2:
        st.metric("Caso Médio", info["caso_medio"])
    with col3:
        st.metric("Pior Caso", info["pior_caso"])

    st.subheader("Análise e Justificativa Teórica")
    st.info(info["justificativa"])

    st.markdown("---")
    st.subheader("Definições Formais das Notações Assintóticas")
    st.markdown("""
    - **O( )**: Limite superior assintótico. A função cresce *no máximo* a esta taxa (cota superior).
    - **Ω( )**: Limite inferior assintótico. A função cresce *pelo menos* a esta taxa (cota inferior).
    - **Θ( )**: Limite assintótico justo (*tight bound*). A função cresce *exatamente* nesta taxa (quando as cotas superior e inferior coincidem).
    
    *Nota:* É um erro comum associar 'O' apenas ao pior caso e 'Θ' ao caso médio. Qualquer cenário (melhor, médio ou pior) pode ser descrito usando qualquer uma das três notações, desde que a análise respeite o limite matemático imposto.
    """)