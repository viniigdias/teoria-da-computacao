class ComplexidadeComputacional:

    def __init__(self):
        self.algoritmos = {
            "Linguagem Formal": {
                "melhor_caso": "Ω(1)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)"
            },

            "Autômato Finito": {
                "melhor_caso": "Ω(1)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)"
            },

            "Gramática Livre de Contexto": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "Θ(n²)",
                "pior_caso": "O(n³)"
            },

            "Autômato com Pilha": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)"
            },

            "Máquina de Turing": {
                "melhor_caso": "Ω(n)",
                "caso_medio": "Θ(n)",
                "pior_caso": "O(n)"
            }
        }

    def listar(self):
        return self.algoritmos

    def mostrar(self):
        resultado = []

        for nome, complexidade in self.algoritmos.items():
            texto = f"""
Algoritmo: {nome}

Melhor Caso: {complexidade['melhor_caso']}
Caso Médio: {complexidade['caso_medio']}
Pior Caso: {complexidade['pior_caso']}
"""
            resultado.append(texto)

        return "\n".join(resultado)
