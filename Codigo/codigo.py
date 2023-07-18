MENU = input("""             ================ MENU ================
             
 Digite (s) para sacar;
 Digite (d) para depositar;
 Digite (e) para mostrar o extrato;
 Digite (q) para sair.

 """)
deposito = 0.0
saque = 0.0
saldo = 15000.0
maximo_saque = 0

while True :
    print(MENU)
    


    if MENU == "s":
        operacao_1 = (float(input("Digite o valor que você quer sacar (até 500 reais): ")))
        print(operacao_1)
        saque += operacao_1

        if operacao_1 > 500: 
            print("O valor máximo permitido é 500!")
            continue

        if operacao_1 <= 500:
           operacao_2 = (str(input("Deseja fazer mais algum saque?(s/n)")))
           print(operacao_2)
        maximo_saque += 1

        if maximo_saque == 3:
            print(" ")
            print("Não é possível fazer mais saques, você atingiu a máximo diário!")
            break

        if operacao_2 == "s":
            continue

        elif operacao_2 == "n" and maximo_saque == 3:
            break
        else:
             print("Por favor, insira um valor válido.")
        
        
        continue
    
        



    elif MENU == "d":
        operacao_1 = (float(input("Digite o valor que você deseja depositar: ")))
        print(f" R${operacao_1:.2f}")     
        deposito += operacao_1  

        if operacao_1 > 0:
            print("")
            print("O valor foi depositado!")
            break

        else: 
            print("")
            print("Por favor insira um valor válido")
            continue

        
    elif MENU == "e":
        print(f"O seu saldo é de: R${saldo:.2f}")
        break
    
            

    elif MENU == "q":
        break



    else:
        print("Não foi possível realizar processo algum.")
        break
print(" ")
saldo = saldo - saque + deposito
print(" ")
print('volte sempre!')
print(" ")
print(f"""
           =============== SAQUE ===============
      
                        R${saque:.2f}

           =============== DEPÓSITO ===============

                        R${deposito:.2f}

           =============== SALDO ===============

                        R${saldo:.2f}""")