import os
os.system("cls")


valor=float(input("digite o valor do produto:R$"))
print("1 - A vista ")
print("2 - A prazo ")
forma=int(input("escolha a forma de pagamento:"))

match forma:
    case 1:
        desconto=valor*0.10
        total=valor-desconto
        print("Forma de pagamento: A vista")
        print(f"desconto:R${desconto:.2f}")
        print(f"total a pagar:R${total:.2f}")
    case 2:
        parcelas=int(input("Digite quantas parcelas quer divider (1 a 6):"))
        if parcelas >=1 and parcelas <= 6:
            valor_parcelas=valor/parcelas

            print("Forma de pagamento: A prazo")
            print("Desconto: R$ 0.00")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor de cada parcela: R$ {valor_parcelas:.2f}")
            print(f"Total a pagar: R$ {valor:.2f}")
        else:
            print("quantidade de parcelas invalida")
    case _:
        print("Forma de pagamento invalido")