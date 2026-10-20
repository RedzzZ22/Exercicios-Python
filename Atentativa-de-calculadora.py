print("###########")
print("Calculadora")
print("###########")

num1 = float (input("escolha um número: "))
num2 = float (input("escolha o segundo número: "))

while True:
    print ("escolha o tipo de calculo:")
    print ("+")
    print ("-")
    print ("*")
    print ("/")
    print ("")
    calc = input("")

    if calc == "+":
        print (f"o resultado da conta {num1} + {num2} é: {num1 + num2}")
        break
    elif calc == "-":
        print (f"o resultado da conta {num1} - {num2} é: {num1 - num2}")
        break
    elif calc == "*":
        print (f"o resultado da conta {num1} * {num2} é: {num1 * num2}")
        break
    elif calc == "/":
        print (f"o resultado da conta {num1} / {num2} é: {num1 / num2}")
        break
    else:
        print ("este calculo não existe.")
        print ("coloque outro")
