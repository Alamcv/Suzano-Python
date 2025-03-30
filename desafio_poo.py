import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(self, conta, transacao)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta) 

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        




def menu():
    menu = """\n

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuario
    [q] Sair

    =>"""

    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if limite_saques <= numero_saques:
        if valor > saldo: 
            print(f"\n Saldo insuficiente. Saldo: R$ {saldo:.2f}")
        elif valor < 0:
            print(f"\n Valor inválido. Para realizar um saque entre com um valor positivo. ")
        elif valor > 0:
            saldo -= valor
            extrato += '\n Operação Saque - Valor: R$ {valor:.2f}'
            numero_saques += 1
            print("Saque realizado com sucesso!")
    else:
        print(f"\n Quantidade de saques diárias ultrapassada.")    
    return extrato, saldo

def depositar(saldo ,valor, extrato):
    if valor < 0:
        print(f"\n Não é possível depositar um valor negativo.")
    else:
        saldo += valor
        extrato += "\n Operação Depósito - Valor: R$ {valor:.2f}"
        print(f"Depósito realizado com sucesso!")

    return saldo, extrato

def visualizar_extrato(saldo, /,*, extrato):
    print(f"|-------------------------EXTRATO-------------------------|")
    print()
    if not extrato: 
        print("   Não existem registros de movimentações realizadas")
    else:
        registros = extrato.splitline()
        for registro in registros:
            print(f"|    {registro}    |")
    print(f"   Saldo atual: R$ {saldo:.2f} ")
    print()
    print(f"|-------------------------EXTRATO-------------------------|")

def cadastrar_usuario(usuarios):
 
    cpf = input(f"Digite o CPF do novo correntista. (APENAS NÚMEROS)")
    cpf = ''.join(char for char in cpf if char.isalnum())

    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print(f"Usuário já cadastrado.")
        return
    
    nome = input("Informe o nome completo: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo (logradouro, número - barrio - cidade/uf): ")

    usuarios.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com suscesso")

def buscar_usuario(cpf, usuarios):

    usuario = [user for user in usuarios if user["cpf"] == cpf]

    if usuario:
        return usuario[0]
    else:
        return None

def cadastrar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Digite o CPF do usuário: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("------- Conta criada com sucesso -------")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado. Antes de cadastrar a conta, realize o cadastro do usuário.")
    

def listar_contas(contas):
    for conta in contas:
        print(conta)


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []



    while True:

        opcao = menu()

        print(f"opcao: {opcao}")

        if opcao == 'd':
            print('Opção Selecionada: Depósito.\n')
            
            valor = float(input("Qual valor deseja depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            print('Opção Selecionada: Saque. \n')

            valor = float(input("Digita o valor de saque desejado."))

            saldo, extrato = sacar(saldo=saldo, valor=valor,extrato=extrato, limite=limite,numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 'e':

            visualizar_extrato(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            cadastrar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
        else:
            print("Opcao inválida. Selecione um opção válida\n\n")

        
main()