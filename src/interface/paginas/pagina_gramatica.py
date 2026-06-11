import streamlit as st
from src.modulos.gramatica_livre_contexto import GramaticaLivreDeContexto

def exibir():
    st.title("Módulo 3 — Gramática Livre de Contexto")

    st.markdown("### Definir Gramática")

    col1, col2 = st.columns(2)
    with col1:
        variaveis_input = st.text_input("Variáveis (separadas por vírgula)", value="S")
        simbolo_inicial = st.text_input("Símbolo inicial", value="S")
    with col2:
        terminais_input = st.text_input("Terminais (separados por vírgula)", value="a, b")

    st.markdown("### Produções Dinâmicas")
    st.caption("Insira uma produção por linha no formato: S -> aSb ou S -> λ")
    producoes_texto = st.text_area("Regras de Produção", value="S -> aSb\nS -> λ", height=120)

    cadeia = st.text_input("Cadeia a derivar", value="aaabbb")

    if st.button("Executar Derivação"):
        variaveis_set = set(v.strip() for v in variaveis_input.split(",") if v.strip())
        terminais_set = set(t.strip() for t in terminais_input.split(",") if t.strip())

        producoes = {}
        substituicoes_validas = True
        
        for linha in producoes_texto.strip().split("\n"):
            if "->" not in linha:
                continue
            esquerda, direita = linha.split("->")
            esquerda = esquerda.strip()
            
            if esquerda not in variaveis_set:
                st.error(f"❌ Erro de sintaxe: A variável '{esquerda}' não foi declarada no campo superior.")
                substituicoes_validas = False
                break
                
            opcoes = [d.strip() for d in direita.split("|") if d.strip()]
            producoes[esquerda] = opcoes

        if substituicoes_validas:
            gramatica = GramaticaLivreDeContexto(
                variaveis=variaveis_set,
                terminais=terminais_set,
                producoes=producoes,
                simbolo_inicial=simbolo_inicial.strip()
            )

            aceita, historico, arvore = gramatica.derivar(cadeia)

            st.markdown("---")
            st.markdown("### 📜 Derivação Passo a Passo")
            st.write(" → ".join([f"`{p}`" for p in historico]))

            st.markdown("### 🌳 Árvore de Derivação Simplificada")
            if aceita and arvore:
                st.markdown("| Passo | Variável Substituída | Regra Aplicada | Transformação |")
                st.markdown("| :--- | :--- | :--- | :--- |")
                for i, passo in enumerate(arvore):
                    st.markdown(f"| {i+1} | `{passo['variavel']}` | `{passo['regra']}` | `{passo['antes']}` $\Rightarrow$ `{passo['depois']}` |")
            else:
                st.caption("Nenhuma árvore gerada para cadeias rejeitadas.")

            st.markdown("---")
            if aceita:
                st.success("✅ Cadeia ACEITA pela gramática!")
            else:
                st.error("❌ Cadeia REJEITADA pela gramática.")