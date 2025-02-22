# Este script é uma ferramenta de documentação automática que analisa um arquivo de código
# e utiliza a API OpenAI para gerar comentários descritivos, facilitando a compreensão do código
# por outros programadores. Ele lê o código de entrada, gera comentários e salva o resultado em um arquivo de saída.

import argparse
import os
from pathlib import Path
from openai import OpenAI

def generate_output_filename(input_path):
    
    input_path = Path(input_path)
    return f"{input_path.stem}_analisado{input_path.suffix}"

def main():
    parser = argparse.ArgumentParser(description='CodeDocGPT - Documentação automática de código usando OpenAI')
    parser.add_argument('input_script', help='Caminho do arquivo de entrada a ser analisado')
    parser.add_argument('output_script', nargs='?', default=None, help='Caminho do arquivo de saída documentado (opcional)')
    parser.add_argument('dicas', nargs='?', default='', help='Dicas adicionais para orientar a documentação (opcional)')
    args = parser.parse_args()

    input_script = args.input_script
    output_script = args.output_script
    dicas = args.dicas

    input_ext = Path(input_script).suffix

    
    if output_script is not None:
        output_ext = Path(output_script).suffix
        if output_ext != input_ext:
            
            if dicas:
                dicas = f"{output_script} {dicas}"
            else:
                dicas = output_script
            output_script = None

    
    if output_script is None:
        output_script = generate_output_filename(input_script)

    
    try:
        with open(input_script, 'r', encoding='utf-8') as f:
            code_content = f.read()  # Lê o arquivo inteiro
    except Exception as e:
        print(f"Erro ao ler arquivo de entrada: {e}")
        exit(1)

    system_role = "Você é um experiente engenheiro de software que escreve comentários ricos e explicativos sempre em pt-br."

    base_prompt = """Identifique a linguagem de programação do código fornecido e recrie novos comentários curtos e explicativos
    para cada sub-etapa existente. Considere iniciar o código comentando uma breve explicação de seu funcionamento e contextualização.
    Altere somente os comentários do código, mantendo a lógica, sintaxe e escrita originais sempre intactas."""
    
    if dicas.strip():
        prompt_final = f" Como dica sobre o código, considere '{dicas}'. E pense nos programadores que irão ler esse código no futuro, sendo o código: "
    else:
        prompt_final = " Pense nos programadores que irão ler esse código no futuro, sendo o código: "
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": f"{base_prompt}{prompt_final}\n\nCódigo:\n{code_content}"}
            ],
            max_tokens=2000
        )
        
    except Exception as e:
        print(f"CodeDocGPT: Erro na API OpenAI: {e}")
        exit(1)

    documented_code = response.choices[0].message.content.strip()
    
    if documented_code.startswith("```"):
        documented_code = '\n'.join(documented_code.split('\n')[1:-1])

    try:
        with open(output_script, 'w', encoding='utf-8') as f:
            f.write(documented_code)
        print(f"CodeDocGPT: Documentação gerada com sucesso em {output_script}")
    except Exception as e:
        print(f"CodeDocGPT: Erro ao salvar arquivo de saída: {e}")
        exit(1)

if __name__ == "__main__":
    main()
