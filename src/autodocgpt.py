import openai
import ast
import os
import argparse
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Obter a chave da API a partir de variáveis de ambiente
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Chave da API não encontrada. Configure a variável de ambiente OPENAI_API_KEY.")
openai.api_key = openai_api_key

def extract_definitions(code: str):
    """
    Extrai funções e classes do código usando AST.
    Retorna duas listas: funções e classes.
    """
    tree = ast.parse(code)
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return functions, classes

def generate_doc_for_function(func: ast.FunctionDef) -> str:
    """
    Gera a documentação para uma função usando a API da OpenAI.
    Tenta incluir a definição da função como contexto no prompt.
    """
    try:
        # Se o Python for 3.9+, usamos ast.unparse para obter o código fonte da função
        func_source = ast.unparse(func) if hasattr(ast, "unparse") else func.name
    except Exception:
        func_source = func.name

    prompt = f"Explique detalhadamente a função a seguir, incluindo seus parâmetros, retornos e comportamento:\n\n{func_source}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        explanation = response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Erro ao gerar documentação para a função {func.name}: {e}")
        explanation = "Não foi possível gerar a documentação via IA."
        
    return f"## Função: `{func.name}`\n**Descrição**: {explanation}\n\n"

def generate_doc_for_class(cls: ast.ClassDef) -> str:
    """
    Gera a documentação para uma classe e seus métodos usando a API da OpenAI.
    """
    try:
        class_source = ast.unparse(cls) if hasattr(ast, "unparse") else cls.name
    except Exception:
        class_source = cls.name

    prompt = f"Explique detalhadamente a classe a seguir, incluindo sua finalidade, atributos e métodos:\n\n{class_source}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        explanation = response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Erro ao gerar documentação para a classe {cls.name}: {e}")
        explanation = "Não foi possível gerar a documentação via IA."
        
    docs = f"## Classe: `{cls.name}`\n**Descrição**: {explanation}\n\n"
    
    # Documenta os métodos internos da classe
    methods = [node for node in cls.body if isinstance(node, ast.FunctionDef)]
    if methods:
        docs += f"### Métodos da classe `{cls.name}`:\n\n"
        for method in methods:
            docs += generate_doc_for_function(method)
    
    return docs

def generate_docs(code: str, output_format: str = "markdown") -> str:
    """
    Gera a documentação completa do código, processando funções e classes.
    Se output_format for 'html', converte o Markdown para HTML.
    """
    functions, classes = extract_definitions(code)
    docs = "# Documentação do Código\n\n"
    
    # Documenta as classes primeiro
    for cls in classes:
        docs += generate_doc_for_class(cls)
    
    # Documenta as funções que estão no nível do módulo (não dentro de classes)
    for func in functions:
        if func.col_offset == 0:  # Heurística para funções definidas no módulo
            docs += generate_doc_for_function(func)
    
    if output_format.lower() == "html":
        try:
            import markdown
            docs = markdown.markdown(docs)
        except ImportError:
            logging.warning("Pacote 'markdown' não encontrado. A saída continuará em Markdown.")
    
    return docs

def main():
    parser = argparse.ArgumentParser(description="Gera documentação automática de código usando IA.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Arquivo de código para documentar")
    parser.add_argument("--output", "-o", type=str, required=True, help="Arquivo de saída para a documentação")
    parser.add_argument("--format", "-f", type=str, choices=["markdown", "html"], default="markdown",
                        help="Formato de saída da documentação (markdown ou html)")
    args = parser.parse_args()
    
    try:
        with open(args.input, "r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo de entrada: {e}")
        return

    documentation = generate_docs(code, args.format)
    
    try:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(documentation)
        logging.info(f"Documentação gerada com sucesso em {args.output}")
    except Exception as e:
        logging.error(f"Erro ao escrever o arquivo de saída: {e}")

if __name__ == "__main__":
    main()
