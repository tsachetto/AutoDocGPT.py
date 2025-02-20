# Este script é uma ferramenta de documentação automática que analisa um arquivo de código
# e utiliza a API OpenAI para gerar comentários descritivos, facilitando a compreensão do código
# por outros programadores. Ele lê o código de entrada, gera comentários e salva o resultado em um arquivo de saída.

import argparse
import os
from pathlib import Path
from openai import OpenAI

def generate_output_filename(input_path):
    # Converte o caminho de entrada para um objeto Path para fácil manipulação.
    # Gera um novo nome de arquivo para o output baseado no nome do arquivo de entrada,
    # acrescentando '_analisado' ao nome original.
    input_path = Path(input_path)
    return f"{input_path.stem}_analisado{input_path.suffix}"

def main():
    # Inicializa o parser de argumentos para receber entradas do usuário via linha de comando.
    # A descrição explica a finalidade da ferramenta.
    parser = argparse.ArgumentParser(description='CodeDocGPT - Documentação automática de código usando OpenAI')
    # Define um argumento obrigatório para o caminho do arquivo de script a ser analisado.
    parser.add_argument('input_script', help='Caminho do arquivo de entrada a ser analisado')
    # Define um argumento opcional para o caminho do arquivo de saída documentado.
    parser.add_argument('output_script', nargs='?', default=None, help='Caminho do arquivo de saída documentado (opcional)')
    # Define um argumento opcional para dicas adicionais que podem auxiliar na documentação.
    parser.add_argument('dicas', nargs='?', default='', help='Dicas adicionais para orientar a documentação (opcional)')
    args = parser.parse_args()

    # Armazena os caminhos do arquivo de entrada e saída, além das dicas.
    input_script = args.input_script
    output_script = args.output_script
    dicas = args.dicas

    # Obtém a extensão do arquivo de entrada usando pathlib.
    input_ext = Path(input_script).suffix

    # Verifica se um arquivo de saída foi especificado.
    if output_script is not None:
        output_ext = Path(output_script).suffix
        # Garante que a extensão do arquivo de saída seja a mesma que a do arquivo de entrada.
        if output_ext != input_ext:
            # Se houver dicas, adiciona-as ao nome do output.
            if dicas:
                dicas = f"{output_script} {dicas}"
            else:
                dicas = output_script
            # Reseta o arquivo de saída se as extensões não forem compatíveis.
            output_script = None

    # Se nenhum arquivo de saída foi especificado, gera um nome padrão para o arquivo de saída.
    if output_script is None:
        output_script = generate_output_filename(input_script)

    # Tenta abrir e ler o conteúdo do arquivo de entrada.
    try:
        with open(input_script, 'r', encoding='utf-8') as f:
            code_content = f.read()  # Lê todo o conteúdo do arquivo de código.
    except Exception as e:
        # Exibe uma mensagem de erro caso não consiga ler o arquivo de entrada.
        print(f"Erro ao ler arquivo de entrada: {e}")
        exit(1)

    # Define o papel do sistema que orienta o modelo da OpenAI sobre a tarefa a ser executada.
    system_role = "Você é um engenheiro de software experiente e criativo que escreve comentários ricos e explicativos em códigos."

    # Prepara a mensagem base que será enviada para a API, contendo instruções sobre a tarefa.
    base_prompt = """Identifique a linguagem de programação do código fornecido, analise o código inteiro e recrie novos comentários 
    curtos e explicativos para cada sub-etapa do código. Sempre inicie o código comentando uma breve 
    explicação de sua finalidade para qualquer leigo entender, tudo em pt-br, sempre após importações ou declarações iniciais.
    Altere somente os comentários do código, mantendo a lógica e código original sempre intáctos."""
    
    # Adiciona dicas ao prompt final se houver.
    if dicas.strip():
        prompt_final = f" Como dica sobre o código, temos '{dicas}'. Pense nos programadores que irão lidar com esse código no futuro, sendo: "
    else:
        prompt_final = " Pense nos programadores que irão ler esse código no futuro, sendo: "
    
    # Cria uma instância do cliente OpenAI com a chave da API.
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        # Faz uma chamada à API OpenAI para gerar a documentação do código.
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": f"{base_prompt}{prompt_final}\n\nCódigo:\n{code_content}"}
            ],
            max_tokens=2000
        )
        
    except Exception as e:
        # Exibe uma mensagem de erro caso ocorra um problema com a API OpenAI.
        print(f"CodeDocGPT: Erro na API OpenAI: {e}")
        exit(1)

    # Captura a resposta documentada retornada pela API.
    documented_code = response.choices[0].message.content.strip()
    
    # Remove as marcações de bloco de código se estiverem presentes na resposta.
    if documented_code.startswith("```"):
        documented_code = '\n'.join(documented_code.split('\n')[1:-1])

    # Tenta salvar o código documentado no arquivo de saída.
    try:
        with open(output_script, 'w', encoding='utf-8') as f:
            f.write(documented_code)  # Grava o conteúdo documentado no arquivo especificado.
        # Exibe uma mensagem de sucesso indicando onde a documentação foi salva.
        print(f"CodeDocGPT: Documentação gerada com sucesso em {output_script}")
    except Exception as e:
        # Exibe uma mensagem de erro caso ocorra um problema ao salvar o arquivo de saída.
        print(f"CodeDocGPT: Erro ao salvar arquivo de saída: {e}")
        exit(1)

# Verifica se o script está sendo executado diretamente, caso afirmativo, chama a função principal.
if __name__ == "__main__":
    main()
