# CodeDocGPT 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-CC0-blue)
![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-green)


**CodeDocGPT** é uma ferramenta open-source que utiliza a __Inteligência Artificial__ da OpenAi para gerar comentários claros, robustos e explicativos ao longo de um código, tornando sua leitura e entendimento muito mais acessível e facilitando na gestão de melhorias. Perfeito para desenvolvedores ou equipes de desenvolvimento que queiram economizar tempo e manter seus projetos bem <ins>explicados</ins>!

https://github.com/user-attachments/assets/03df248e-f782-4c14-8462-9e5c8ca5c3a6

## ✨ Funcionalidades

**Geração automática de documentação**: Analisa funções, classes e métodos e gera descrições claras.

**Suporte a múltiplas linguagens**: Funciona com Python, JavaScript e mais (em breve!).

**Formatos de saída**: O código sai intacro, acrescido de uma nova e robusta documentação comentada.

**Interface simples**: Fácil de usar via linha de comando (CLI).

**Powered by OpenAI**: Utiliza modelos avançados de IA para criar documentação de alta qualidade.

## 🚀 Como Usar

**Instalação**

**Instale as dependências**:

```
pip install -r requirements.txt
```

**Configure sua chave da OpenAI**:

Crie um arquivo .env na raiz do projeto e adicione sua chave:

```
OPENAI_API_KEY=sua_chave_aqui
```

Uma excelente opção é criar uma variável de ambiente OPENAI_API_KEY e informar sua chave de API.

**Uso Direto via Curl:**

Instale todas as dependências e rode direto via linha de comando (CMD):

```
curl -s https://raw.githubusercontent.com/tsachetto/CodeDocGPT/main/src/codedocgpt.py | python - seu_script.py
```

**Uso Básico:**

Execute o CodeDocGPT passando o nome do arquivo do seu código que deseja documentar:

```
python codedocgpt.py script_a_ser_analisado.py script_analisado_output.py "Dica: Este é um código que realiza cálculos sobre x asssunto!"
```

Apenas os dois primeiros argumentos (script codedocgpt.py e arquivo de entrada) são obrigatórios!

### Guia

Resumindo, via CMD, chame o python,

chame o script codedocgpt.py

chame o código que deseja analisar

como __opcional__, informe o nome do arquivo de saída

e/ou uma dica entre aspas duplas, para contextualizar o modelo sobre qual tipo de código ele estará analisadno.

## 🛠️ Tecnologias Usadas

**Python**: Linguagem principal.

**OpenAI GPT**: Para gerar a documentação.

**GitHub**: Hospedagem do código.

## 📂 Estrutura do Projeto

```
AutoDocGPT/
├── src/
│   ├── codedocgpt.py          # Código principal (Concluído)
│   ├── cli.py                 # Interface de linha de comando (Breve)
│   └── utils/                 # Funções auxiliares (Breve)
├── tests/                     # Testes unitários (Breve)
├── examples/                  # Exemplos de código para testar (Breve)
├── docs/                      # Documentação do projeto (Breve)
├── Dockerfile                 # Configuração do Docker (Breve)
├── requirements.txt           # Dependências do projeto (Concluído)
├── LICENSE                    # Licença CC0 (Concluído)
└── README.md                  # Este arquivo (Concluído)
```

## 📄 Licença

Este projeto está licenciado sob a Creative Commons Zero (CC0).

Isso significa que você pode usar, modificar e distribuir o código sem restrições. Para mais detalhes, veja o arquivo LICENSE.

## 👏 Créditos

Desenvolvido por Thomaz Sachetto Silva.

Powered by OpenAI 🧠.

## 📬 Contato

Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

**Email:** thomazsachetto@gmail.com

**GitHub:** @tsachetto

Feito com muito ☕ e um pouco de magia da IA! ✨

