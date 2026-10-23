import os
os.system('cls')

QUANTIDADE_LACO = 5
soma = 0
pares = 0
impares = 0

for i in range (QUANTIDADE_LACO):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero:
        soma += numero

print(f'\nPares: {pares}')
print(f'Impares: {impares}')
print(f'Soma: {soma}')