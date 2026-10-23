import os
os.system("cls")

produto=input("Digite o nome do produto!:")
quantidade=int(input("Digite a quantidade comprada!:"))
preco_unitario=float(input("Digite o valor do produto R$:"))
# Calcula o total sem desconto
total=quantidade*preco_unitario
# Define o desconto conforme a quantidade
if quantidade <=5:
    Desconto=0.02
elif quantidade <=10:
    Desconto=0.03
else:
    Desconto=0.05
# Calcula o desconto e o total a pagar
valor_desconto = total * Desconto
total_pagar = total - valor_desconto

print("=Total da compra=")
print(f"Produto:{produto}")
print(f"quntidade:{quantidade}")
print(f"Total sem desconto:R${total:.2f}")
print(f"Desconto aplicado:{Desconto:.2f}")
print(f"Valor do Desconto:R${valor_desconto:.2f}")
print(f"Total a pagar:R${total_pagar:.2f}")