while True: # o loop infinito foi iniciado
    comando = input("Digite 'sair' para desligar o motor: ")

    if comando.lower() == 'sair':
        print ("motor desligado.")
        break # a trava de segurança foi acionada!
else:
    print("O motor continua rodando...")