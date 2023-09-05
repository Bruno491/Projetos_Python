def lista_3():
    op_cont = int('5')
    
    while op_cont != 0:
        print('lista de contatos do RAV')
        print('1 - Usuario5')
        print('2 - Usuario6')
        print('Selecione um usuario para enviar o e-mail ou tecle "0" para voltar')
        op_cont = int(input('Opção: '))
        if op_cont == 1:
            return 'Usuario5@outlook.com'
        elif op_cont == 2:
            return 'Usuario6@outlook.com'
        elif op_cont == 0:
            print('Voltando...')
        else:
            print('Opção invalida!')