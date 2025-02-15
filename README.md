# AutoDocGPT 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-CC0-blue)
![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-green)

**AutoDocGPT** é uma ferramenta open-source que usa __Inteligência Artificial__ para gerar documentação automática de código. Basta passar seu script, e ele cria uma documentação clara e profissional em Markdown ou HTML.
Perfeito para desenvolvedores ou equipes de desenvolvimento que queiram economizar tempo e manter seus projetos bem <ins>documentados</ins>!

## ✨ Funcionalidades
**Geração automática de documentação**: Analisa funções, classes e métodos e gera descrições claras.

**Suporte a múltiplas linguagens**: Funciona com Python, JavaScript e mais (em breve!).

**Formatos de saída**: Gera documentação em Markdown ou HTML.

**Interface simples**: Fácil de usar via linha de comando (CLI).

**Powered by OpenAI**: Utiliza modelos avançados de IA para criar documentação de alta qualidade.

## 🚀 Como Usar
**Instalação**

**Clone o repositório**:

```
git clone https://github.com/seu-usuario/AutoDocGPT.git
cd AutoDocGPT
```

**Instale as dependências**:

```
pip install -r requirements.txt
```

**Configure sua chave da OpenAI**:

Crie um arquivo .env na raiz do projeto e adicione sua chave:
```
OPENAI_API_KEY=sua_chave_aqui
```

**Uso Básico:**

Execute o script passando o arquivo de código que deseja documentar:

```
python autodocgpt.py --input script.py --output docs.md --format markdown
```

Exemplo de Saída (Markdown)

```
# Documentação do Código

## Função: `soma(a, b)`
**Descrição**: Esta função recebe dois números, `a` e `b`, e retorna a soma deles.

### Parâmetros:

- `a` (int): O primeiro número.
- `b` (int): O segundo número.

### Retorno:

- `int`: A soma de `a` e `b`.
```

## 🛠️ Tecnologias Usadas

**Python**: Linguagem principal.

**OpenAI GPT**: Para gerar a documentação.

**Markdown/HTML**: Formatos de saída.

**Docker**: Para facilitar a execução em qualquer ambiente.


## 📂 Estrutura do Projeto

```
AutoDocGPT/
├── src/
│   ├── autodocgpt.py          # Código principal
│   ├── cli.py                 # Interface de linha de comando
│   └── utils/                 # Funções auxiliares
├── tests/                     # Testes unitários
├── examples/                  # Exemplos de código para testar
├── docs/                      # Documentação do projeto
├── Dockerfile                 # Configuração do Docker
├── requirements.txt           # Dependências do projeto
├── LICENSE                    # Licença CC0
└── README.md                  # Este arquivo
```

## 📄 Licença
Este projeto está licenciado sob a Creative Commons Zero (CC0). Isso significa que você pode usar, modificar e distribuir o código sem restrições. Para mais detalhes, veja o arquivo LICENSE.

## 👏 Créditos
Desenvolvido por Thomaz Sachetto Silva.

Powered by OpenAI 🧠.

## 📬 Contato
Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

**Email: thomazsachetto@gmail.com**
**GitHub: @tsachetto**

Feito com ☕ e um pouco de magia da IA! ✨

