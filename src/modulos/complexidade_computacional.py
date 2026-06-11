class ComplexidadeComputacional:

    def __init__(self) -> None:
        self.algoritmos = {
            "Linguagem Formal": {
                "melhor_caso": "Ω(1)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)",
                "justificativa": "Percorre a cadeia linearmente uma única vez para verificar se cada símbolo individual pertence ao alfabeto determinado."
            },

            "Autômato Finito": {
                "melhor_caso": "Ω(1)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)",
                "justificativa": "Processa a cadeia símbolo por símbolo de forma estritamente linear, efetuando exatamente uma transição de estado por caractere consumido."
            },

            "Gramática Livre de Contexto": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "O(|P|^n)",
                "pior_caso": "O(|P|^n)",
                "justificativa": "A exploração via Busca em Largura (BFS) sobre formas sentenciais gera crescimento exponencial O(|P|^n). Para evitar explosão combinatorial ou loops infinitos, aplicamos uma heurística de poda que encerra ramos cujo comprimento ultrapassa o tamanho da cadeia alvo + 4."
            },

            "Autômato com Pilha": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)",
                "justificativa": "Varre a cadeia linearmente. Em cada caractere processado, executa operações de tempo constante O(1) na pilha (inserção ou remoção)."
            },

            "Máquina de Turing": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)",
                "justificativa": "Percorre a fita linearmente localizando o caractere delimitador '1', transiciona o estado para reajustar o encerramento do unário e finaliza com varreduras de ordem linear."
            }
        }

    def listar(self) -> dict:
        return self.algoritmos