Você tocou no ponto exato! Aqueles **15% de Documentação** são a soma perfeita do Relatório Técnico em PDF (que já finalizamos) com um **README.md** impecável no seu repositório.

Na hora da apresentação (os 10%), você **não precisa ler** o README ou o PDF. A apresentação deve focar nos **30% de Funcionamento** (mostrar a tela rodando) e **20% de Conceitos** (explicar o porquê de cada coisa, como combinamos no roteiro). O professor vai avaliar a documentação depois, lendo o seu GitHub e o seu PDF com calma. Mas vale muito a pena, no início do vídeo, mostrar a aba do GitHub rapidinho e dizer: *"Todo o nosso código está versionado aqui, com instruções de execução e exemplos de entrada e saída documentados"*.

Para garantir a nota máxima na documentação do GitHub, copie o texto abaixo e substitua tudo o que está no seu `README.md` atual. Eu já incluí todos os exemplos exatos que testamos hoje.

---

```markdown
# Simulador de Linguagens Formais e Modelos Computacionais

Projeto prático desenvolvido para a disciplina de Aspectos Teóricos da Computação. Esta aplicação interativa modela, valida e simula conceitos fundamentais da Teoria da Computação através de uma interface visual dinâmica.

Projeto online (Deploy na nuvem): [Acessar Simulador](https://aspectos-teoricos-da-computacao.streamlit.app/)

---

## ⚙️ Como Executar

O projeto foi construído utilizando **Python 3.10+** e a biblioteca **Streamlit** para a interface gráfica. O motor matemático está isolado no back-end, garantindo alta performance nas validações.

### Opção 1: Execução Local
1. Clone este repositório em sua máquina:
   ```bash
   git clone [https://github.com/viniigdias/teoria-da-computacao.git](https://github.com/viniigdias/teoria-da-computacao.git)

```

2. Acesse a pasta do projeto:
```bash
cd teoria-da-computacao

```


3. Instale as dependências:
```bash
pip install -r requirements.txt

```


4. Inicie o servidor do Streamlit:
```bash
streamlit run src/interface/app.py

```


*O simulador abrirá automaticamente no seu navegador no endereço `http://localhost:8501`.*

### Opção 2: Acesso Online

Não é necessário instalar nada. O projeto possui um deploy ativo e pode ser acessado diretamente pelo link:
👉 **[Simulador de Teoria da Computação](https://aspectos-teoricos-da-computacao.streamlit.app/)**

---

## 🧪 Exemplos de Entrada e Saída

Abaixo estão os casos de teste padronizados para homologar o funcionamento de cada módulo matemático do simulador.

### Módulo 1: Linguagens Formais (Validação)

* **Objetivo:** Verificar pertinência de cadeia a um alfabeto definido.
* **Exemplo de Entrada:**
* Alfabeto: `a, b`
* Cadeia: `abba`


* **Exemplo de Saída Esperada:** `✅ Cadeia válida | Tamanho: 4`

### Módulo 2: Autômato Finito

* **Objetivo:** Rastrear transições determinísticas de um AFD.
* **Exemplo de Entrada (Caminho Feliz):**
* Autômato: (Usar o JSON padrão de exemplo na tela)
* Cadeia: `ab`


* **Exemplo de Saída Esperada:** Rastreamento `q0 -> q1 -> q2` | `✅ ACEITA`
* **Exemplo de Entrada (Rejeição):**
* Cadeia: `abc`


* **Exemplo de Saída Esperada:** Rastreamento `q0 -> q1 -> q2` (Falha por ausência de transição para 'c') | `❌ REJEITA`

### Módulo 3: Gramática Livre de Contexto (GLC)

* **Objetivo:** Gerar árvore de derivação via Busca em Largura (BFS).
* **Exemplo de Entrada:**
* Regras de Produção: `S -> aSb` e `S -> λ`
* Cadeia: `aaabbb`


* **Exemplo de Saída Esperada:** Tabela de árvore de derivação gerada com sucesso finalizando em λ | `✅ Cadeia ACEITA`

### Módulo 4: Autômato com Pilha (AP)

* **Objetivo:** Validar a linguagem $a^n b^n$ manipulando o marcador de fundo $Z_0$.
* **Exemplo de Entrada:**
* Cadeia: `aabb`


* **Exemplo de Saída Esperada:** A tabela exibe o empilhamento dos 'A's e o desempilhamento até sobrar apenas `[Z0]` no último passo | `✅ CADEIA ACEITA`

### Módulo 5: Máquina de Turing

* **Objetivo:** Calcular a soma de dois números em representação unária.
* **Exemplo de Entrada:**
* Fita Inicial: `000100` (Soma de 3 + 2)


* **Exemplo de Saída Esperada:** O processamento exibe o cabeçote apagando o separador '1' | Resultado Final: `00000` (5 zeros).

---

## 📚 Documentação Técnica

A análise detalhada de Complexidade Computacional (Notações Assintóticas) e as justificativas teóricas de cada módulo estão documentadas dentro da própria interface do simulador (Aba **Módulo 6**) e no Relatório Técnico oficial do projeto.

**Desenvolvido por:**

* Vinicius Gomes Dias
* Vitor Cesar Gonçalves Lima

```
