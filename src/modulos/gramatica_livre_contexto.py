class GramaticaLivreDeContexto:

    def __init__(self, variaveis, terminais, producoes, simbolo_inicial):
        self.variaveis = variaveis
        self.terminais = terminais
        self.producoes = producoes
        self.simbolo_inicial = simbolo_inicial

    def derivar(self, cadeia, max_passos=20):
        historico = [self.simbolo_inicial]
        arvore = []

        for simbolo in cadeia:
            if simbolo not in self.terminais:
                arvore.append({
                    "variavel": "-",
                    "regra": "-",
                    "antes": self.simbolo_inicial,
                    "depois": "rejeitada",
                    "motivo": f"Símbolo inválido: {simbolo}"
                })
                return False, historico, arvore

        if (
            self.simbolo_inicial == "S"
            and "S" in self.producoes
            and "aSb" in self.producoes["S"]
            and "λ" in self.producoes["S"]
        ):
            qtd_a = cadeia.count("a")
            qtd_b = cadeia.count("b")
            atual = self.simbolo_inicial

            for _ in range(qtd_a):
                novo = atual.replace("S", "aSb", 1)

                arvore.append({
                    "variavel": "S",
                    "regra": "aSb",
                    "antes": atual,
                    "depois": novo,
                    "motivo": "Aplicação da produção"
                })

                atual = novo
                historico.append(atual)

            novo = atual.replace("S", "", 1)

            arvore.append({
                "variavel": "S",
                "regra": "λ",
                "antes": atual,
                "depois": novo if novo != "" else "λ",
                "motivo": "Finalização da derivação"
            })

            atual = novo
            historico.append(atual if atual != "" else "λ")

            if qtd_a != qtd_b:
                arvore.append({
                    "variavel": "-",
                    "regra": "-",
                    "antes": atual,
                    "depois": "rejeitada",
                    "motivo": "Quantidade de 'a' diferente da quantidade de 'b'"
                })
                return False, historico, arvore

            if cadeia != ("a" * qtd_a + "b" * qtd_b):
                arvore.append({
                    "variavel": "-",
                    "regra": "-",
                    "antes": atual,
                    "depois": "rejeitada",
                    "motivo": "A cadeia não está no formato aⁿbⁿ"
                })
                return False, historico, arvore

            return atual == cadeia, historico, arvore

        return False, historico, [{
            "variavel": "-",
            "regra": "-",
            "antes": self.simbolo_inicial,
            "depois": "rejeitada",
            "motivo": "Gramática não reconhecida por este simulador"
        }]