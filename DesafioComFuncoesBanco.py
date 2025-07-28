import textwrap

def menu():
    menu = """\n
    =============== MENU ===============
    [1]\tNovo usuário
    [2]\tNova conta
    [3]\tDepositar
    [4]\tSacar
    [5]\tExtrato
    [6]\tListar usuários
    [7]\tListar contas
    [8]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
     saldo = 200
     limite = 500
     extrato = ""
     numero_saques = 0
     LIMITE_SAQUES = 3
     usuarios = []
     contas = []
     numero_conta = 0
     
     while True:
         opcao =  menu()

         if opcao == "1":
          nome = input("Informe o nome do usuario: ")
          nascimento = input("Informe sua data de nascimento: ")
          cpf = input("Informe o cpf: ")
          endereco = input("Informe seu endereço: ")
          criar_usuario(nome,nascimento, cpf,endereco,usuarios,contas)

         elif opcao == "2":
          numero_conta = + 1
          cpf = input("Informe o cpf: ")
          criar_conta(cpf,numero_conta,usuarios,contas)
    
         elif opcao == "3":
          valor = float(input("Informe o valor do depósito: "))
          deposito(valor,extrato,saldo)

         elif opcao == "4":
          valor = float(input("Informe o valor do saque: "))
          saque(valor=valor,saldo =saldo,numero_saques=numero_saques,limite=limite,LIMITE_SAQUES=LIMITE_SAQUES,extrato=extrato)

         elif opcao == "5": 
          extrato_da_conta(saldo, extrato= extrato)

         elif opcao == "6":
          listar_usuarios(usuarios)

         elif opcao == "7":
          listar_contas(contas)
    
         elif opcao == "8":
          break

         else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")     
     
def cpf_existe(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False

def criar_usuario(nome,nascimento, cpf,endereco,usuarios):
             
        if cpf_existe(cpf):  
            return print("Já existe um usuário com esse CPF. Tente novamente.")
        
        usuario = {
             'nome':nome,
             'nascimento': nascimento,
             'cpf': cpf,
             'endereco' : endereco
        }
        usuarios.append(usuario)
        return print (f"Usuário '{nome}' cadastrado com sucesso!")

def criar_conta(cpf,numero_conta,contas,usuarios):
             
        if not cpf_existe(cpf):  
            return print("CPF não encontrado, para cadastrar uma conta é nescessario ter um usuário cadastrado.")
        
        conta = {
             'agencia':'0001',
             'numero_conta_cliente': numero_conta,
             'cpf': cpf,
        }
        contas.append(conta)
        return print (f"Usuário '{usuarios.nome}' cadastrado com sucesso!")   
          
def saque(valor,saldo,numero_saques,limite,LIMITE_SAQUES,extrato):
    
    excedeu_saldo = valor >  saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
         return print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
         return print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         numero_saques += 1
         return print(f"Saque realizado com sucesso!\n Saldo: R$ {saldo:.2f}\n================ EXTRATO ================ \n{extrato}")
                
    else:
         return print("Operação falhou! O valor informado é inválido.")

def deposito(valor,extrato,saldo):

     if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return print(f"Deposito realizado com sucesso!\n Saldo: R$ {saldo:.2f}\n================ EXTRATO ================ \n{extrato}")
     else:
         return print("Operação falhou! O valor informado é inválido.")

def extrato_da_conta(saldo, /, extrato):

      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")

def listar_usuarios(usuarios):
        if not usuarios:
             print("Nenhum Cliente cadastrado ainda.")
             return
        print("\n Lista de Clientes cadastrados:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"\nUsuário {i}:")
            print(f"  Nome: {usuario['nome']}")
            print(f"  Nascimento: {usuario['nascimento']}")
            print(f"  CPF: {usuario['cpf']}")
            print(f"  Endereço: {usuario['endereco']}")    
 
def listar_contas(contas):
        if not contas:
             print("Nenhuma conta cadastrado ainda.")
             return
        print("\n Lista de contas cadastrados:")
        for i, conta in enumerate(contas, start=1):
            print(f"\nUsuário {i}:")
            print(f"  Agência: {conta['agencia']}")
            print(f"  Numero da conta: {conta['numero_conta_cliente']}")
            print(f"  CPF: {conta['cpf']}")
            
main()
