class AutomatoFinito:

    def _init_(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def executar(self, cadeia):
        estado_atual = self.estado_inicial
        historico = [estado_atual]

        for simbolo in cadeia:
            chave = (estado_atual, simbolo)
            if chave not in self.transicoes:
                return False, historico
            estado_atual = self.transicoes[chave]
            historico.append(estado_atual)

        aceita = estado_atual in self.estados_finais
        return aceita, historico