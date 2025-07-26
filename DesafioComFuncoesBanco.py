menu = """

[1] Cadastrar usuário
[2] Cadastrar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair

=> """

saldo = 200
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

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


while True:
    opcao = input(menu)

    if opcao == "3":
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor,extrato,saldo)

    elif opcao == "4":
        valor = float(input("Informe o valor do saque: "))
        saque(valor=valor,saldo =saldo,numero_saques=numero_saques,limite=limite,LIMITE_SAQUES=LIMITE_SAQUES,extrato=extrato)

    elif opcao == "5":
        extrato_da_conta(saldo, extrato= extrato)
         
    elif opcao == "6":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


