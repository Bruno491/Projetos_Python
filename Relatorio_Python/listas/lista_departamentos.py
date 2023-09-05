import os
from listas.lista_2 import lista_2
from listas.lista_3 import lista_3
from listas.lista_1 import lista_1

def lista_departamentos():
    op_dep = int('0')
    while op_dep != 4:
        print('<<<<Departamentos>>>>')
        print('1- Departamento 1')
        print('2- Departamento 2')
        print('3- Departamento 3')
        print('4- Voltar')
        op_dep = int(input('Opção: '))
        os.system('cls')
        if op_dep == 1:
            return lista_2()
        elif op_dep == 2:
            return lista_3()
        elif op_dep == 3:
            return lista_1()
        elif op_dep == 4:
            print('Voltando...')
            return 0
        else:
            print('Opção Invalida!')
    