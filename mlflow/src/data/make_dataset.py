# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


# Definição do comando principal da aplicação usando a biblioteca click
@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))  # Argumento para o caminho do arquivo de entrada (deve existir)
@click.argument('output_filepath', type=click.Path())  # Argumento para o caminho do arquivo de saída (não precisa existir)
def main(input_filepath, output_filepath):
    """ Função que processa os dados brutos (raw) e gera um conjunto de dados limpo pronto para análise
        (salvo na pasta ../processed).
    """
    # Configura o logger para registrar informações durante a execução do código
    logger = logging.getLogger(__name__)  # Cria um logger com o nome do módulo
    logger.info('making final data set from raw data')  # Registra uma mensagem informando o processo atual

# Bloco de execução do script
if __name__ == '__main__':
    # Define o formato do log para exibir informações detalhadas
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)  # Configura o logging para exibir mensagens no formato definido

    # Definição do diretório do projeto para facilitar a navegação por arquivos
    project_dir = Path(__file__).resolve().parents[2]  # Caminho para o diretório do projeto (duas pastas acima do arquivo atual)

    # Encontra automaticamente o arquivo .env na hierarquia de pastas e carrega suas variáveis de ambiente
    load_dotenv(find_dotenv())  # Carrega as variáveis de ambiente a partir do arquivo .env, se encontrado

    # Chama a função principal para iniciar o processamento
    main()