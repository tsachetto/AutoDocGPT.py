import argparse
import os
from autodocgpt import generate_docs  # Importa a função principal do AutoDocGPT

def main():
    # Configura o parser de argumentos da CLI
    parser = argparse.ArgumentParser(
        description="AutoDocGPT: Gerador automático de documentação de código usando IA."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Caminho do arquivo de código a ser documentado.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="docs.md",
        help="Caminho do arquivo de saída para a documentação. Padrão: docs.md",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["markdown", "html"],
        default="markdown",
        help="Formato da documentação gerada. Opções: markdown, html. Padrão: markdown",
    )
    args = parser.parse_args()

    # Verifica se o arquivo de entrada existe
    if not os.path.exists(args.input):
        print(f"Erro: O arquivo '{args.input}' não foi encontrado.")
        return

    # Lê o conteúdo do arquivo de código
    try:
        with open(args.input, "r") as file:
            code = file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo '{args.input}': {e}")
        return

    # Gera a documentação
    print(f"Gerando documentação para '{args.input}'...")
    try:
        documentation = generate_docs(code, args.format)
    except Exception as e:
        print(f"Erro ao gerar a documentação: {e}")
        return

    # Salva a documentação no arquivo de saída
    try:
        with open(args.output, "w") as file:
            file.write(documentation)
        print(f"Documentação salva com sucesso em '{args.output}'!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{args.output}': {e}")

if __name__ == "__main__":
    main()
