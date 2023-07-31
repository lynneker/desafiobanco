menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito R$:"))

        if valor > 0:
            saldo += valor
            extrato += (f"Deposito: RS{valor:.2f}\n")

        else:
            print("Valor invalido")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = saldo > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Excedeu limite de saque por dia")

        elif excedeu_saques:
            print("Excedeu o limite de saques diarios")
    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$:{valor:.2f}\n"
            numero_saques +=1
        
        else:
            print("Operação Falhou o valor infomrado é invalido")
    
    elif opcao == "e":
        print("\n ########## - Extrato - ##########\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo é de R$: {saldo:.2f}\n")
        print("##################################e")

    elif opcao == "q":
        break

    else:
        print("Operação inválida")