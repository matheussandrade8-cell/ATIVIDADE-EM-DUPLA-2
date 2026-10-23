import os
import time
os.system('cls')

tentativas = 0

print('       ===== CADASTRO =====')
cadastro_login = input('Digite o usuario para cadastrar: ')
cadastro_senha = input('Digite a senha para cadastro: ')
print('Cadastro realizado com sucesso!')
time.sleep(2.5)
os.system('cls')

while True:
    tentativas += 1
    print(f'Tentativas: {tentativas}/3')
    login = input('Digite o seu login: ')
    senha = input('Digite a sua senha: ')
    if login == cadastro_login and senha == cadastro_senha:
        print('Bem vindo!')
        break
    else:
        print(f'Login ou senha inválidos, tente novamente')
        time.sleep(2.5)
        os.system('cls')
    if tentativas == 3:
        print('Usuario bloqueado, você atingiu o limite de tentativas!\nTente novamente mais tarde')
        break