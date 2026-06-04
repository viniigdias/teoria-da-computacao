class LinguagemFormal:

    def __init__(self, alfabeto: set[str]):
        self.alfabeto = alfabeto

    def cadeia_pertence_ao_alfabeto(self, cadeia: str) -> bool:
        return all(simbolo in self.alfabeto for simbolo in cadeia)

    def tamanho_da_cadeia(self, cadeia: str) -> int:
        return len(cadeia)

    def concatenar(self, cadeia_a: str, cadeia_b: str) -> str:
        return cadeia_a + cadeia_b

    def sigma_estrela(self, tamanho_maximo: int) -> list[str]:
        from itertools import product
        resultado = ['']
        for tamanho in range(1, tamanho_maximo + 1):
            for combinacao in product(self.alfabeto, repeat=tamanho):
                resultado.append(''.join(combinacao))
        return resultado

    def sigma_mais(self, tamanho_maximo: int) -> list[str]:
        return [c for c in self.sigma_estrela(tamanho_maximo) if c != '']