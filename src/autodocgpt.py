import openai
import ast

# Configuração da API da OpenAI
openai.api_key = "sua_chave_aqui"

def analyze_code(code):
    """
    Analisa o código e identifica funções e classes.
    """
    tree = ast.parse(code)
    functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    return functions

def generate_docs(code):
    """
    Gera documentação para o código usando IA.
    """
    functions = analyze_code(code)
    docs = "# Documentação do Código\n\n"
    
    for func in functions:
        prompt = f"Explique a função {func.name} em detalhes."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        docs += f"## Função: `{func.name}`\n"
        docs += f"**Descrição**: {response.choices[0].text.strip()}\n\n"
    
    return docs

if __name__ == "__main__":
    with open("script.py", "r") as file:
        code = file.read()
    
    documentation = generate_docs(code)
    with open("docs.md", "w") as file:
        file.write(documentation)
