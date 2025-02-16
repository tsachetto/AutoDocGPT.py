import argparse
import os
from pathlib import Path
from openai import OpenAI

def main():
    parser = argparse.ArgumentParser(description='AutoDocGPT - Documentação automática de código usando OpenAI')
    parser.add_argument('input_script', help='Caminho do arquivo de entrada a ser analisado')
    parser.add_argument('output_script', help='Caminho do arquivo de saída documentado')
    parser.add_argument('dicas', nargs='?', default='', help='Dicas adicionais para orientar a documentação')
    args = parser.parse_args()

    # Verifica extensões dos arquivos
    input_ext = Path(args.input_script).suffix
    output_ext = Path(args.output_script).suffix
    if input_ext != output_ext:
        print("Erro: As extensões dos arquivos de entrada e saída devem ser iguais.")
        exit(1)

    # Lê o código fonte com limite de caracteres
    try:
        with open(args.input_script, 'r', encoding='utf-8') as f:
            code_content = f.read(50000)
    except Exception as e:
        print(f"Erro ao ler arquivo de entrada: {e}")
        exit(1)

    # Configura o prompt
    system_role = "Você é um engenheiro de software experiente e criativo que escreve documentação clara e objetiva em códigos."
    base_prompt = "Identifique a linguagem do código fornecido. Analise-o e recrie uma nova documentação adequada comentando em cada etapa identificando suas funcionalidades, inclusive explicando cada condicionais (if etc), loops (for, when etc) ou sub processos. Complementando, crie uma introdução em forma de comentário explicando a finalidade do código analisado em até 100 palavras com tabulação e quebra de linha. Importante: retornar o código integral com a apenas com a nova documentaçao sobreposta, sem alterar a programação. Tudo em PT-BR.\n"
    
    if args.dicas:
        prompt_final = f"Como dica sobre o código temos: {args.dicas}\nInclua comentários relevantes em cada parte."
    else:
        prompt_final = "Pense nos programadores que irão lidar com esse código depois.\n"
    
    prompt_final += "A saída deve ser apenas o código orignal com os novos comentários da documentação."

    # Monta a requisição para OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": f"{base_prompt}{prompt_final}\n\nCódigo:\n{code_content}"}
            ],
            max_tokens=2500
        )
    except Exception as e:
        print(f"Erro na API OpenAI: {e}")
        exit(1)

    # Processa a resposta
    documented_code = response.choices[0].message.content.strip()
    
    # Remove blocos de código Markdown se existirem
    if documented_code.startswith("```"):
        documented_code = '\n'.join(documented_code.split('\n')[1:-1])

    # Salva o arquivo de saída
    try:
        with open(args.output_script, 'w', encoding='utf-8') as f:
            f.write(documented_code)
        print(f"Documentação gerada com sucesso em {args.output_script}")
    except Exception as e:
        print(f"Erro ao salvar arquivo de saída: {e}")
        exit(1)

if __name__ == "__main__":
    main()
