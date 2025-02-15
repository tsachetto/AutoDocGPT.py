# AutoDocGPT 🚀
[GitHub License](https://img.shields.io/badge/license-CC0-blue)
[Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
[OpenAI](https://img.shields.io/badge/powered%20by-OpenAI-green)

AutoDocGPT é uma ferramenta open-source que usa Inteligência Artificial para gerar documentação automática de código. Basta passar seu script, e ele cria uma documentação clara e profissional em Markdown ou HTML. Perfeito para desenvolvedores que querem economizar tempo e manter seus projetos bem documentados!

# ✨ Funcionalidades
Geração automática de documentação: Analisa funções, classes e métodos e gera descrições claras.

Suporte a múltiplas linguagens: Funciona com Python, JavaScript e mais (em breve!).

Formatos de saída: Gera documentação em Markdown ou HTML.

Interface simples: Fácil de usar via linha de comando (CLI).

Powered by OpenAI: Utiliza modelos avançados de IA para criar documentação de alta qualidade.

# 🚀 Como Usar
Instalação
Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/AutoDocGPT.git
cd AutoDocGPT
Instale as dependências:

bash
Copy
pip install -r requirements.txt
Configure sua chave da OpenAI:

Crie um arquivo .env na raiz do projeto e adicione sua chave:

plaintext
Copy
OPENAI_API_KEY=sua_chave_aqui
Uso Básico
Execute o script passando o arquivo de código que deseja documentar:

bash
Copy
python autodocgpt.py --input script.py --output docs.md --format markdown
Exemplo de Saída (Markdown)
markdown
Copy
# Documentação do Código

## Função: `soma(a, b)`
**Descrição**: Esta função recebe dois números, `a` e `b`, e retorna a soma deles.

### Parâmetros:
- `a` (int): O primeiro número.
- `b` (int): O segundo número.

### Retorno:
- `int`: A soma de `a` e `b`.
🛠️ Tecnologias Usadas
Python: Linguagem principal.

OpenAI GPT: Para gerar a documentação.

Markdown/HTML: Formatos de saída.

Docker: Para facilitar a execução em qualquer ambiente.

#📂 Estrutura do Projeto
Copy
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

#🤝 Como Contribuir
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do repositório.

Crie uma branch para sua feature:

bash
Copy
git checkout -b minha-feature
Commit suas mudanças:

bash
Copy
git commit -m 'Adicionei uma nova feature'
Envie para o repositório remoto:

bash
Copy
git push origin minha-feature
Abra um Pull Request.

#📄 Licença
Este projeto está licenciado sob a Creative Commons Zero (CC0). Isso significa que você pode usar, modificar e distribuir o código sem restrições. Para mais detalhes, veja o arquivo LICENSE.

#👏 Créditos
Desenvolvido por [Seu Nome].

Powered by OpenAI.

#📬 Contato
Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

Email: thomazsachetto@gmail.com
GitHub: @tsachetto

Feito com ☕ e um pouco de magia da IA! ✨

