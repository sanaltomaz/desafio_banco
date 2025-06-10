def menu_inicial():
    print("Seja bem vindo!")
    print("1. Entrar")
    print("2. Registrar")
    print("3. Sair")
    print("Banco Slicer")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        print("Você escolheu a Opção 1.")
        # Aqui você pode chamar outra função ou executar algum código específico
    elif escolha == '2':
        print("Você escolheu a Opção 2.")
        # Aqui você pode chamar outra função ou executar algum código específico
    elif escolha == '3':
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu_inicial()  # Chama o menu novamente se a opção for inválida