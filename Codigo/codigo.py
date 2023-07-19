menu = ("""
        =========================== MENU ===========================
             
(d) depositar
(s) sacar
(e) extrato
(q) sair

=>  """)

numero_de_saques = 0
valor_do_saque = 0
deposito = 0
# extrato = " "
saldo = 10000

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o quanto você deseja depositar: "))

        if valor_deposito > 0:
            print(f"-> O valor de R${valor_deposito} foi depositado")
            deposito += valor_deposito
            saldo += valor_deposito
            continue
        else:
            print("(-> Insira um valor válido!)")
            continue

    elif opcao == "s":
        valor_sacado = float(input("Digite o quanto você deseja sacar: "))
        
        if valor_sacado > saldo:
            print("-> Saldo insuficiente. Insira um valor válido!")
            continue
        elif valor_sacado <= 0:
            print("-> Insira um valor válido!")
            continue
        else:
            print("-> O valor foi sacado!")
            numero_de_saques += 1
            saldo -= valor_sacado
            valor_do_saque += valor_sacado
            continue

    elif opcao == "e":
        print("         ================== Extrato ==================")
        print("")
        print(f"saldo: R${saldo:.2f}")
        print(f"depósito: R${deposito:.2f}")
        print(f"saque: R${valor_do_saque:.2f}")
        print("")

        opcao_2 = str(input("Deseja sair do programa?(s/n) => "))
        if opcao_2 == "s":
            break
        elif opcao_2 == "n":
            continue
        else:
            break

    elif opcao == "q":
        break

    else:
        print("-> Insira uma letra válida!")
        continue

print("")
print("Volte sempre!")
print("")
