def lista_2():
    op_cont = int('5')
    
    while op_cont != 0:
        print('lista de contatos do CIT')
        print('1- Usuario3')
        print('2- Usuario4')
        print('Selecione um usuario para enviar o e-mail ou tecle "0" para voltar')
        op_cont = int(input('Opção: '))
        if op_cont == 1:
            return 'Usuario3@outlook.com'
        elif op_cont == 2:
            return 'Usuario4@outlook.com'
        elif op_cont == 0:
            print('Voltando...')
        else:
            print('Opção invalida!')