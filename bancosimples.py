while True:
    depos="R$"
    saq="R$"
    deposito=0
    maxsaq=3
    d=input("Deseja fazer um depósito? ")
    if d.upper() == 'SIM':
        quantd=int(input('Digite a quantidade de depositos que deseja fazer: '))
        for j in range(quantd):
            numero=int(input('Digite o valor que deseja depositar: '))
            while numero<0:
                print('Não é permitido depositar valores menores que 0')
                numero=int(input('Digite o valor que deseja depositar ou "0" para desistir do despósito: '))
                if numero==0:
                    break
            deposito=deposito+numero
            depos=depos+"R$"+str(numero)+".00 -  " 
    s=input('Deseja sacar um valor? ')
    if s.upper() == 'SIM':
        quant=int(input('Digite a quantidade de saques que deseja fazer: '))
        while quant>maxsaq:
            print('Não são permitidos mais de 3 saques por dia')
            if maxsaq == 0:
                break
            else:
                quant=int(input('Digite uma nova quantidade ou 0 para desistir dos saques: '))
                if quant == 0:
                    break
        for i in range(quant):
            saques=3
            print(f'Você tem um saldo de {saques} saques diários. Não são permitidos saques de valor maior que R$500,00 ')
            retirar=int(input('Digite o valor que deseja retirar: '))
            while retirar>500:
                print('Não são permitidos saques de mais de R$500,00')
                retirar=int(input('Digite outro valor ou 0 para desistir do saque: '))
                if retirar == 0:
                    break
            if retirar == 0:
               continue
            elif retirar<0:
               print("Não são permitidos valores menores que 0")
               retirar=int(input("Digite o valor que deseja sacar ou 0 para desistir do saque: "))
               if retirar == 0:
                   break
            while (deposito-retirar)<0:
                print("não é permitido um saque maior que o saldo atual da conta")
                retirar=int(input('Digite outro valor ou 0 para desistir do saque: '))
            else:
                deposito=deposito-retirar
                saq=saq+"R$"+str(retirar)+".00 - "
                maxsaq-=1
                quant-=1
    ex=input('Deseja ver seu extrato? ')
    if ex.upper() == 'SIM':
        print(f'Seus depositos foram:{depos}')
        print(f'Seus saques foram:{saq}')
        print(f'Saldo atual da conta:R${deposito}')
    print('''
    
    Proximo dia: \n''')
        
           
