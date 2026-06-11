import pytest
from src.modulos.linguagem_formal import LinguagemFormal
from src.modulos.automato_finito import AutomatoFinito
from src.modulos.gramatica_livre_contexto import GramaticaLivreDeContexto
from src.modulos.automato_com_pilha import AutomatoComPilha
from src.modulos.maquina_de_turing import MaquinaDeTuring


def test_linguagem_formal():
    lf = LinguagemFormal({'a', 'b'})
    
    assert lf.cadeia_pertence_ao_alfabeto("abba") == True
    assert lf.cadeia_pertence_ao_alfabeto("abc") == False
    assert lf.tamanho_da_cadeia("abba") == 4
    assert lf.concatenar("ab", "ba") == "abba"
    assert len(lf.sigma_estrela(2)) == 7 
    assert len(lf.sigma_mais(2)) == 6 

def test_automato_finito():
    transicoes = {
        ("q0", "a"): "q1",
        ("q1", "b"): "q2"
    }
    af = AutomatoFinito(
        estados=["q0", "q1", "q2"], 
        estado_inicial="q0", 
        estados_finais=["q2"], 
        transicoes=transicoes
    )
    
    aceita_valida, historico, passos = af.executar("ab")
    assert aceita_valida == True
    assert historico[-1] == "q2"

    aceita_invalida, _, _ = af.executar("aa")
    assert aceita_invalida == False
    
    aceita_incompleta, _, _ = af.executar("a")
    assert aceita_incompleta == False


def test_gramatica_livre_de_contexto():
    producoes = {
        "S": ["aSb", "λ"]
    }
    glc = GramaticaLivreDeContexto({"S"}, {"a", "b"}, producoes, "S")
    
    aceita_1, _, _ = glc.derivar("aabb")
    assert aceita_1 == True
    
    aceita_2, _, _ = glc.derivar("aaabbb")
    assert aceita_2 == True
    
    aceita_inv_1, _, _ = glc.derivar("aabbb")
    assert aceita_inv_1 == False
    
    aceita_inv_2, _, _ = glc.derivar("bbaa") 
    assert aceita_inv_2 == False


def test_automato_com_pilha():
    ap = AutomatoComPilha()
    
    aceita_1, _ = ap.executar("ab")
    assert aceita_1 == True
    
    aceita_2, _ = ap.executar("aaabbb")
    assert aceita_2 == True
    
    aceita_inv_1, _ = ap.executar("aab")
    assert aceita_inv_1 == False
    
    aceita_inv_2, _ = ap.executar("ba")
    assert aceita_inv_2 == False
    
    aceita_inv_3, _ = ap.executar("a")
    assert aceita_inv_3 == False


def test_maquina_de_turing():
    mt = MaquinaDeTuring()
    
    aceita_1, _, resultado_1 = mt.somar_unario("000100") 
    assert aceita_1 == True
    assert resultado_1 == "00000"
    
    aceita_2, _, resultado_2 = mt.somar_unario("010") 
    assert aceita_2 == True
    assert resultado_2 == "00"
    
    aceita_inv, _, _ = mt.somar_unario("000") 
    assert aceita_inv == False