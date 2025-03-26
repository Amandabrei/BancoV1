menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
depositos = []
saques = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            saques.append(valor)
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n================ EXTRATO ===============")
        if not depositos and not saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("======================================")
    
    elif opcao == "q":
        print("Obrigado por utilizar nosso banco! Até logo.")
        break
    
    else:
        print("Operação inválida, tente novamente.")

#código criado por Amanda Breidenbach