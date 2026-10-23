import os
os.system("cls")

print("=Calculadora=")
n1=float(input("Digite o primeiro numero:"))
n2=float(input("Digite o segundo numero:"))
operador=input("Selecione o operador(+,*,-,/):")
match operador:
    case "+":
        resultado=n1+n2
        print(f"primeiro numero:{n1}")
        print(f"segundo numero:{n2}")
        print(f"operador escolhido:{operador}")
        print(f"Resultado: {resultado}")
    case "-":
            resultado=n1-n2
            print(f"primeiro numero:{n1}")
            print(f"segundo numero:{n2}")
            print(f"operador escolhido:{operador}")
            print(f"Resultado: {resultado}")
    case "*":
            resultado=n1*n2
            print(f"primeiro numero:{n1}")
            print(f"segundo numero:{n2}")
            print(f"operador escolhido:{operador}")
            print(f"Resultado: {resultado}")
    case "/":
            resultado=n1/n2
            print(f"primeiro numero:{n1}")
            print(f"segundo numero:{n2}")
            print(f"operador escolhido:{operador}")
            print(f"Resultado: {resultado}")
            if n2 !=0:
                resultado=n1/n2
                print(f"resultado:{resultado}")
            else:
                print("não é permitido dividir por zero!")
    case _:
        print("operação invalida!")


