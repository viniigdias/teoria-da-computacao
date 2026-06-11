from collections import deque

class GramaticaLivreDeContexto:

    def __init__(self, variaveis, terminais, producoes, simbolo_inicial):
        self.variaveis = set(variaveis)
        self.terminais = set(terminais)
        self.producoes = producoes
        self.simbolo_inicial = simbolo_inicial

    def derivar(self, cadeia, max_passos=1500):
        """
        Deriva a cadeia usando Busca em Largura (BFS) limitando a profundidade.
        Nota Teórica: O BFS possui complexidade exponencial no pior caso. Para evitar loops 
        infinitos em gramáticas altamente recursivas, uma heurística de poda de tamanho 
        (+4) é aplicada. O algoritmo CYK seria determinístico em O(n³), porém exige FNC.
        """
        alvo = "" if cadeia in ["λ", "lambda", ""] else cadeia

        fila = deque([(self.simbolo_inicial, [self.simbolo_inicial], [])])
        visitados = {self.simbolo_inicial}

        vars_ordenadas = sorted(list(self.variaveis), key=len, reverse=True)

        while fila and max_passos > 0:
            max_passos -= 1
            atual, historico, arvore = fila.popleft()

            if atual == alvo:
                return True, historico, arvore

            idx_var = -1
            var_achada = None

            for i in range(len(atual)):
                for var in vars_ordenadas:
                    if atual[i:].startswith(var):
                        idx_var = i
                        var_achada = var
                        break
                if idx_var != -1:
                    break

            if idx_var == -1:
                continue

            terminais_atuais = [c for c in atual if c in self.terminais]
            if len(terminais_atuais) > len(alvo):
                continue

            opcoes = self.producoes.get(var_achada, [])
            for opcao in opcoes:
                substituta = "" if opcao in ["λ", "lambda", ""] else opcao
                
                novo = atual[:idx_var] + substituta + atual[idx_var + len(var_achada):]

                if novo not in visitados:
                    if len(novo) > len(alvo) + 4:
                        continue

                    visitados.add(novo)

                    passo_arvore = {
                        "variavel": var_achada,
                        "regra": opcao if opcao != "" else "λ",
                        "antes": atual,
                        "depois": novo if novo != "" else "λ"
                    }

                    exibicao_limpa = novo if novo != "" else "λ"
                    fila.append((
                        novo, 
                        historico + [exibicao_limpa], 
                        arvore + [passo_arvore]
                    ))

        return False, [self.simbolo_inicial], [{
            "variavel": "-",
            "regra": "-",
            "antes": self.simbolo_inicial,
            "depois": "rejeitada",
            "motivo": "Cadeia rejeitada ou árvore de derivação muito profunda."
        }]