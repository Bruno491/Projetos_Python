from tabulate import tabulate
import openpyxl

def visualizar_planilha():
    # Carregar o arquivo Excel
    arquivo_excel = openpyxl.load_workbook('C:\\restante_do_caminho\\Pasta1.xlsx')

    # Selecionar a planilha desejada
    planilha = arquivo_excel['Nome da planilha']

    # Criar uma lista para armazenar as linhas da tabela
    tabela = []

    # Percorrer as células e adicionar os valores à tabela
    for linha in planilha.iter_rows(values_only=True):
        tabela.append(linha)

    # Exibir a tabela com espaçamentos e alinhamentos corretos
    print(tabulate(tabela, headers='firstrow', tablefmt='fancy_grid'))

def edita_planilha():
    # Faça alguma coisa aqui

    if __name__ == "__main__":
        visualizar_planilha()