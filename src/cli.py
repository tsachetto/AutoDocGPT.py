import argparse
import os
import logging
from autodocgpt import generate_docs  # Importa a função principal do AutoDocGPT

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

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
        logging.error(f"Erro: O arquivo '{args.input}' não foi encontrado.")
        exit(1)

    # Lê o conteúdo do arquivo de código com codificação UTF-8
    try:
        with open(args.input, "r", encoding="utf-8") as file:
            code = file.read()
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo '{args.input}': {e}")
        exit(1)

    # Gera a documentação
    logging.info(f"Gerando documentação para '{args.input}'...")
    try:
        documentation = generate_docs(code, args.format)
    except Exception as e:
        logging.error(f"Erro ao gerar a documentação: {e}")
        exit(1)

    # Salva a documentação no arquivo de saída com codificação UTF-8
    try:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(documentation)
        logging.info(f"Documentação salva com sucesso em '{args.output}'!")
    except Exception as e:
        logging.error(f"Erro ao salvar o arquivo '{args.output}': {e}")
        exit(1)

if __name__ == "__main__":
    main()
