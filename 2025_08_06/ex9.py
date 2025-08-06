"""
Calculadora Simples com Menu
Exiba um menu:
1. Soma  
2. Subtração  
3. Multiplicação  
4. Divisão  

Leia a opção e dois números, então exiba o resultado.
Repita até o usuário digitar "sair" (use while True).

"""

def calcula(primeiro: int, segundo:int, operacao: str):
    if operacao=="+":
        return a+b
    elif operacao=="-":
        return a-b
    elif operacao=="*":
        return a*b
    else:
        if b!=0:
            return a/b
        else:
            return 0


while True:
    print("\nSelecione a opção (ou \"sair\")")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    opcao = input("Escolha: ")

    if opcao=="sair":
        break
    else:
        a = int(input("Primeiro numero: "))
        b = int(input("Segundo numero: "))
        if opcao=='1':
            res = calcula(a, b, "+")
        elif opcao=='2':
            res = calcula(a, b, "-")
        elif opcao=='3':
            res = calcula(a, b, "*")
        elif opcao=='4':
            res = calcula(a, b, "/")

        print(f"Resultado: {res}")