import os
os.system("cls")

renda=float(input("Digite o valor da sua renda:R$"))
emprestimo=float(input("Digite o valor do emprestimo:R$"))
prestacao=int(input("Digite o numero de prestações:"))

#Calcula o valor de cada prestação!
valor=emprestimo/prestacao
#Verificação de emprestimo
if emprestimo<=renda*10 and valor<=renda*0.30:
    print("emprestimo aprovado")
else:
    print("emprestimo negado")

print(f"valor da prestação:{valor}")