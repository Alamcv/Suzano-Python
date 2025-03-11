menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Opção Selecionada: Depósito.\n')
        
        valor = int(input("Qual valor deseja depositar: "))
        
        while valor < 0:
            valor = int(input("Valor não pode ser negativo. \n Digite um valor válido ou 0 para retornar ao menu principal. "))
        
        if valor > 0:
            
            saldo = saldo + valor
            extrato = extrato + f"Operação Depósito: R$ {valor:.2f} \n"

            print(f"Saldo atual da conta é de R$ {saldo:.2f}")
        else:
            continue
    
    elif opcao == 's':
        print('Opção Selecionada: Saque. \n')

        if numero_saques < LIMITE_SAQUES:

            valor = int(input("Digita o valor de saque desejado."))

            while valor < 0 or valor > 500:
                valor = int(input("Valor não pode ser negativo e nem superiro a 500. \n Digite um valor válido ou 0 para retornar ao menu principal. "))
            
            if saldo >= valor: 
                if valor > 0:
                    
                    saldo = saldo - valor
                    numero_saques = numero_saques + 1
                    extrato = extrato + f"Operação Saque: R${valor:.2f} \n"

                    print(f"Saldo atual da conta é de R$ {saldo}")
                else:
                    continue
            else:
                print(f"Valor de saque R$ {valor:.2f} ultrapassa o valor de saldo R$ {saldo:.2f}. \n Não é possível realizar o saque.")
                
        else:
            print("Quantidade máxima de saques diários ultrapassado. Tente novamente amanhã.")
            continue

    elif opcao == 'e':
        print('Opção Selecionada: Extrato. \n')
        print("*************************EXTRATO*************************")
        print("Não há histórico de movimentações nessa conta." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("*********************************************************")
    
    elif opcao == 'q':
        break
    else:
        print("Opcao inválida. Selecione um opção válida\n\n")

        