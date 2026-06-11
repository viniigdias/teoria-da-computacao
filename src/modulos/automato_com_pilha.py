class AutomatoComPilha:
    def __init__(self):
        self.estado_inicial = "q0"

    def executar(self, cadeia):
        pilha = []
        historico = []
        estado_atual = self.estado_inicial

        # estados:
        # q0: empilha 'A' para cada 'a'
        # q1: desempilha 'A' para cada 'b'
        
        for simbolo in cadeia:
            historico.append({
                "leitura": simbolo,
                "estado": estado_atual,
                "pilha": list(pilha) if pilha else ["(vazia)"]
            })

            if estado_atual == "q0":
                if simbolo == "a":
                    pilha.append("A")
                elif simbolo == "b":
                    if not pilha:
                        return False, historico
                    pilha.pop()
                    estado_atual = "q1"
                else:
                    return False, historico

            elif estado_atual == "q1":
                if simbolo == "b":
                    if not pilha:
                        return False, historico
                    pilha.pop()
                else:
                    return False, historico

        historico.append({
            "leitura": "λ (fim)",
            "estado": estado_atual,
            "pilha": list(pilha) if pilha else ["(vazia)"]
        })

        aceita = (estado_atual == "q1" and len(pilha) == 0)
        return aceita, historico