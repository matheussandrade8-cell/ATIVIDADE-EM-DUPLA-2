import os
os.system('cls')

soma = 0

for i in range(3):
    while True:
        nota = float(input(f'Digite a {i+1}º nota do aluno: '))
        if nota < 0 or nota > 10:
            print('Nota inválida, tente novamente!')
        else:
            break
    soma += nota
media = soma / 3

if media >= 7:
    resultado = 'Aprovado'
elif media >= 5:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print(f'\n===== RESULTADO =====')
print(f'Medía do aluno: {media:.2f}')
print(f'Situação: {resultado}')