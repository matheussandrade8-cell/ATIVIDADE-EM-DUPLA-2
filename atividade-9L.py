import os
import time
os.system('cls')

soma_pratos = 0
contador = 0

#print('''
#  ===== MENU =====
#1 - Macarrão = R$19,99
#2 - Strogonoff = R$29,90
#3 - Pastel = R$12,99
#4 - Pão com ovo = R$8,99
#5 - Coxinha = 7,99''')

while True:
    print('''
  ===== MENU =====
1 - Macarrão = R$19,99
2 - Strogonoff = R$29,90
3 - Pastel = R$12,99
4 - Pão com ovo = R$8,99
5 - Coxinha = R$7,99''')
    contador += 1
    prato = int(input('Digite o codigo do prato que deseja: '))
    match prato:
        case 1:
            comida = 'Macarrão'
            valor = 19.99
        case 2:
            comida = 'Strogonoff'
            valor = 29.90
        case 3:
            comida = 'Pastel'
            valor = 12.90
        case 4:
            comida = 'Pão com ovo'
            valor = 8.99
        case 5:
            comida = 'Coxinha'
            valor = 7.99
        case _:
            print('Opção inválida, tente novamente')
            continue
    prato_adicional = input('Deseja adicionar mais um prato? (S/N): ').upper()
    soma_pratos += valor
    if prato_adicional == 'N':
        break

print(f'\n   ===== PAGAMENTOS =====')
print(f'Quantidade de pratos escolhidos: {contador}')
print(f'Total a pagar: R${soma_pratos}')