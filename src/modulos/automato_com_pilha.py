class AutomatoComPilha:
    def __init__(self) -> None:
        self.estado_inicial = "q0"

    def executar(self, cadeia: str) -> tuple[bool, list[dict]]:
        pilha = ["Z0"]
        historico = []
        estado_atual = self.estado_inicial

        for simbolo in cadeia:
            historico.append({
                "leitura": simbolo,
                "estado": estado_atual,
                "pilha": list(pilha)
            })

            if estado_atual == "q0":
                if simbolo == "a":
                    pilha.append("A")
                elif simbolo == "b":
                    if len(pilha) <= 1 or pilha[-1] != "A":
                        return False, historico
                    pilha.pop()
                    estado_atual = "q1"
                else:
                    return False, historico

            elif estado_atual == "q1":
                if simbolo == "b":
                    if len(pilha) <= 1 or pilha[-1] != "A":
                        return False, historico
                    pilha.pop()
                else:
                    return False, historico

        historico.append({
            "leitura": "λ (fim)",
            "estado": estado_atual,
            "pilha": list(pilha)
        })

        aceita = (estado_atual == "q1" and pilha == ["Z0"])
        return aceita, historico