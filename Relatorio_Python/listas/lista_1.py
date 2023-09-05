def lista_1():
    op_cont = int('0')
    
    while op_cont != 0 or op_cont != 1 or op_cont != 2:
        print('lista de contatos do centro de impressão')
        print('1- Usuario1')
        print('2- Usuario2')
        print('Selecione um usuario para enviar o e-mail ou tecle "0" para voltar')
        op_cont = int(input('Opção: '))
        if op_cont == 1:
            return 'Usuario1@outlook.com'
        elif op_cont == 2:
            #return 'lab.estagio2@toledoprudente.edu.br'
            return 'Usuario2@outlook.com'
        elif op_cont == 0:
            print('Voltando...')
        else:
            print('Opção invalida!')