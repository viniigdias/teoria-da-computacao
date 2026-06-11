class AutomatoFinito:

    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def executar(self, cadeia):
        estado_atual = self.estado_inicial
        historico = [estado_atual]
        passos = []

        for simbolo in cadeia:
            chave = (estado_atual, simbolo)

            if chave not in self.transicoes:
                passos.append(f"Não existe transição: {estado_atual} --{simbolo}--> ?")
                return False, historico, passos

            proximo_estado = self.transicoes[chave]

            passos.append(f"{estado_atual} --{simbolo}--> {proximo_estado}")

            estado_atual = proximo_estado
            historico.append(estado_atual)

        aceita = estado_atual in self.estados_finais
        return aceita, historico, passos
