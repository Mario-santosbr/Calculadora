def somar (a,b):
    return a+b
def subtrair (a,b):
    return a-b
def multiplicar (a,b):
    return a*b
def dividir(a,b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida"
    return a/b

while True:
    print ("\n==== CALCULADORA ====")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")

    opcao = input ("escolha uma opção: ")
    if opcao == "5":
        print ("Obrigado por usar a calculadora! Até mais!!")
        break

    elif opcao == "1":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = somar(num1,num2)
        print("Resultado:" , resultado)

    elif opcao == "2":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = subtrair(num1,num2)
        print("Resultado:" , resultado)

    elif opcao == "3":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = multiplicar(num1,num2)
        print("Resultado:" , resultado)

    elif opcao == "4":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = dividir(num1,num2)
        print("Resultado:" , resultado)

    else: print("Erro: Opção inválida!! Escolha uma opção de 1 a 5.")

