class GramaticaLivreDeContexto:

    def __init__(self, variaveis, terminais, producoes, simbolo_inicial):
        self.variaveis = variaveis
        self.terminais = terminais
        self.producoes = producoes
        self.simbolo_inicial = simbolo_inicial

    def derivar(self, cadeia, max_passos=20):
        atual = self.simbolo_inicial
        historico = [atual]

        for _ in range(max_passos):
            substituiu = False
            for variavel, producao in self.producoes.items():
                for regra in producao:
                    if variavel in atual:
                        atual = atual.replace(variavel, regra, 1)
                        historico.append(atual)
                        substituiu = True
                        break
                if substituiu:
                    break

            if atual == cadeia:
                return True, historico
            if not any(v in atual for v in self.variaveis):
                break

        return atual == cadeia, historico