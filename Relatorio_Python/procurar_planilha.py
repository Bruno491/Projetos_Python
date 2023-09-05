import os
from visualizar_planilha import visualizar_planilha

def procurar_planilha():
    # Definir o nome do arquivo Excel
    nome_arquivo = input("Informe o nome do arquivo Excel: ")

    # Definir as pastas a serem verificadas
    pastas = [
        'C:\\Users\\bruno\\OneDrive\\Área de Trabalho',
        'C:\\Users\\bruno\\Downloads',
        'C:\\Users\\bruno\\OneDrive\\Documentos'
    ]

    # Verificar se o arquivo existe em alguma das pastas
    arquivo_encontrado = False
    pasta_arquivo = ""

    for pasta in pastas:
        caminho_arquivo = os.path.join(pasta, f'{nome_arquivo}.xlsx')
        if os.path.isfile(caminho_arquivo):
            arquivo_encontrado = True
            pasta_arquivo = pasta
            break

    if arquivo_encontrado:
        print(f'O arquivo {nome_arquivo}.xlsx foi encontrado na pasta: {pasta_arquivo}')
        abrir_pasta = input('Deseja visualizar a planilha? (S/N): ')
        if abrir_pasta.upper() == 'S':
            visualizar_planilha()
    else:
        print(f'O arquivo {nome_arquivo}.xlsx não foi encontrado.')

        criar_arquivo = input('Deseja criar um novo arquivo? (S/N): ')
        if criar_arquivo.upper() == 'S':
            nome_novo_arquivo = input('Informe o nome para o novo arquivo: ')
            pasta_novo_arquivo = input('Informe a pasta para salvar o novo arquivo: ')

            caminho_novo_arquivo = os.path.join(pasta_novo_arquivo, f'{nome_novo_arquivo}.xlsx')

            print(f'O arquivo {nome_novo_arquivo}.xlsx foi criado na pasta: {pasta_novo_arquivo}')
        else:
            print('Nenhum novo arquivo foi criado.')