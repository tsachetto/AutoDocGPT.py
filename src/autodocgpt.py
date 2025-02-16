import argparse
import os
from pathlib import Path
from openai import OpenAI

def generate_output_filename(input_path):
    """Gera o nome do arquivo de saída adicionando '_analisado' antes da extensão."""
    input_path = Path(input_path)
    return f"{input_path.stem}_analisado{input_path.suffix}"

def main():
    parser = argparse.ArgumentParser(description='AutoDocGPT - Documentação automática de código usando OpenAI')
    parser.add_argument('input_script', help='Caminho do arquivo de entrada a ser analisado')
    parser.add_argument('output_script', nargs='?', default=None, help='Caminho do arquivo de saída documentado (opcional)')
    parser.add_argument('dicas', nargs='?', default='', help='Dicas adicionais para orientar a documentação (opcional)')
    args = parser.parse_args()

    input_script = args.input_script
    output_script = args.output_script
    dicas = args.dicas

    input_ext = Path(input_script).suffix

    # Processa output_script e dicas
    if output_script is not None:
        output_ext = Path(output_script).suffix
        if output_ext != input_ext:
            # Adiciona output_script fornecido como parte das dicas
            if dicas:
                dicas = f"{output_script} {dicas}"
            else:
                dicas = output_script
            output_script = None

    # Gera nome do arquivo de saída se não fornecido
    if output_script is None:
        output_script = generate_output_filename(input_script)

    # Lê o código fonte com limite de caracteres
    try:
        with open(input_script, 'r', encoding='utf-8') as f:
            code_content = f.read(50000)
    except Exception as e:
        print(f"Erro ao ler arquivo de entrada: {e}")
        exit(1)

    # Configura o prompt
    system_role = "Você é um engenheiro de software experiente e criativo que escreve documentação clara e objetiva em códigos."
    base_prompt = " Identifique a linguagem de programação do código fornecido, analise o código inteiro e recrie uma nova documentação robusta e verbosa para cada etapa do código, comentando com #. No início do código, comente um passo a passo do funcionamento do código em linguagem natural para qualquer leigo entender o código, iniciando cada linha com #, sendo a primeira uma descrição que explique o código em uma única linha. Tudo em PT-BR."
    
    if dicas.strip():
        prompt_final = f" Como dica sobre o código, temos: {dicas}. Pense nos programadores que irão lidar com esse código depois."
    else:
        prompt_final = " Pense nos programadores que irão lidar com esse código depois."
    
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
        #print(f"{base_prompt}\n{prompt_final}")
    except Exception as e:
        print(f"AutoDocGPT: Erro na API OpenAI: {e}")
        exit(1)

    # Processa a resposta
    documented_code = response.choices[0].message.content.strip()
    
    # Remove blocos de código Markdown se existirem
    if documented_code.startswith("```"):
        documented_code = '\n'.join(documented_code.split('\n')[1:-1])

    # Salva o arquivo de saída
    try:
        with open(output_script, 'w', encoding='utf-8') as f:
            f.write(documented_code)
        print(f"AutoDocGPT: Documentação gerada com sucesso em {output_script}")
    except Exception as e:
        print(f"AutoDocGPT: Erro ao salvar arquivo de saída: {e}")
        exit(1)

if __name__ == "__main__":
    main()
