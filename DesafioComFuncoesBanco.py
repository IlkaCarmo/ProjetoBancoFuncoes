menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 200
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def saque(valor):
    global saldo
    global numero_saques
    global limite
    global LIMITE_SAQUES
    global extrato

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
         return print("Saque realizado com sucesso")

    else:
         return print("Operação falhou! O valor informado é inválido.")

def deposito(valor):
     global extrato
     global saldo

     if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return print("Deposito realizado com sucesso.")
     else:
         return print("Operação falhou! O valor informado é inválido.")

def extrato_da_conta():
      global extrato
      global saldo

      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saque(valor)

    elif opcao == "e":
        extrato_da_conta()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


