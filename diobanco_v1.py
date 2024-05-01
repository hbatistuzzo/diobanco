# O código abaixo é baseado no template didático construído pelo Guilherme Carvalho.

menu = ("""
Seja Bem Vindo(A) 

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair
        
=> """)

# constantes definidas abaixo
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 # token
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": # Caso o usuario queira depositar um valor
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: # Restrição: valor deve ser positivo
            saldo += valor # Atualiza o saldo com o input do usuario
            extrato += f"Depósito: R$ {valor:.2f}\n" # Atualiza o extrato

        else: # Caso não obedeça à restrição do valor positivo
            print("Operação não executada! O valor informado é inválido.")

    elif opcao == "s": # Caso o usuario queira sacar um valor
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo # RESTRIÇÃO 1: valor não pode ser maior que o saldo atual

        excedeu_limite = valor > limite # RESTRIÇÂO 2: valor não pode exceder a constante LIMITE definida acima

        excedeu_saques = numero_saques >= LIMITE_SAQUES # RESTRIÇÃO 3: numero maximo de saques = 3

        if excedeu_saldo:
            print("Operação não executada! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação não executada! O valor do saque excede seu limite.")

        elif excedeu_saques:
            print("Operação não executada! Limite de saques diário excedido.")

        elif valor > 0: # caso passe por todas as restrições, basta conferir que o valor é positivo
            saldo -= valor # atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n" # atualiza o extrato
            numero_saques += 1 # atualiza o token

        else: # Caso não obedeça à restrição do valor positivo
            print("Operação não executada! O valor informado é inválido.")

    elif opcao == "e": # extrato customizado e estilizado
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # if ternário
        print(f"\nSaldo: R$ {saldo:.2f}") # O saldo sempre é exibido
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")