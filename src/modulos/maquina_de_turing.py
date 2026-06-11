class MaquinaDeTuring:
    def somar_unario(self, entrada):
        espaco_seguro = max(10, len(entrada) + 5)
        fita = list(entrada) + ["_"] * espaco_seguro 
        cabecote = 0
        estado = "q0"
        historico = []

        while estado != "q_aceita" and estado != "q_rejeita":
            historico.append({
                "estado": estado,
                "cabecote": cabecote,
                "fita": list(fita)
            })

            leitura = fita[cabecote]

            if estado == "q0":
                if leitura == "0":
                    cabecote += 1
                elif leitura == "1":
                    fita[cabecote] = "0"
                    estado = "q1"
                    cabecote += 1
                else:
                    estado = "q_rejeita"

            elif estado == "q1":
                if leitura == "0":
                    cabecote += 1
                elif leitura == "_":
                    cabecote -= 1
                    estado = "q2"
                else:
                    estado = "q_rejeita"

            elif estado == "q2":
                if leitura == "0":
                    fita[cabecote] = "_"
                    estado = "q_aceita"
                else:
                    estado = "q_rejeita"


        historico.append({
            "estado": estado,
            "cabecote": cabecote,
            "fita": list(fita)
        })

        resultado_final = "".join(fita).replace("_", "")
        return estado == "q_aceita", historico, resultado_final