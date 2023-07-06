#Importando a biblioteca random e string
import random
import string
from time import sleep

#Criando variáveis com as letras, números e caracteres usados na senha forte
letras_minusculas = string.ascii_lowercase
numeros = string.digits
caracteres = string.punctuation
letras_maiusculas = string. ascii_uppercase

programa_finalizado = False
while not programa_finalizado:
    #Criando um menu para escolha do gerador ou verificador
    print('Bem vindo ao meu gerador de senhas fortes.\n'
          'Gerador de senha...............Digite 1\n'
          'Verificador de senha...........Digite 2\n')
    escolha_menu = int(input('Qual sua escolha? \n'))

    #Criando a estrutura condicional para entrada do verificador de senha
    if escolha_menu == 2:
        print('=-' * 14)
        print('VERIFICADOR DE SENHA FORTE')
        print('=-' * 14)
        senha_atual = str(input('Qual senha deseja verificar?\n'))

        #Verificando se a senha atual é forte
        if len(senha_atual) < 8:
            print('Sua senha precisa conter no mínimo 8 caracteres')

        if senha_atual.lower() == senha_atual:
            print('Sua senha precisa conter ao menos 1 letra maiúscula.')

        if senha_atual.upper() == senha_atual:
            print('Sua senha precisa conter ao menos 1 letra minúscula.')

        tem_numero_senha = False
        for num in senha_atual:
            if num.isdigit():
                tem_numero_senha = True
                break
        if not tem_numero_senha:
            print('Sua senha precisa conter ao menos 1 número')

        tem_caractere_senha = False
        for carac in senha_atual:
            if carac in string.punctuation:
                tem_caractere_senha = True
                break
        if not tem_caractere_senha:
            print('Sua senha precisa conter ao menos 1 caractere')

        break
    elif escolha_menu == 1:
        while True:
            #Fazendo um input para retornar a quantidade de cada número, letra e caractere
            n_letras = int(input('Quantas letras você quer em sua senha?\n'))
            n_numeros = int(input('Quantos números você quer em sua senha?\n'))
            n_caracteres = int(input('Quantos caracteres especiais você quer em sua senha?\n'))

            #Adicionando uma lista para guardar o que vai ser utilizado na senha forte
            senha_forte = []

            #Utilizando estrutura de repetição "FOR" com a biblioteca random para determinar o que vai ser utilizado na
            # senha forte
            for le_min in range(0, n_letras - 1):
                senha_forte.append(random.choice(letras_minusculas))
            for le_mai in range(0, 1):
                senha_forte.append(random.choice(letras_maiusculas))

            for n in range(0, n_numeros):
                senha_forte.append(random.choice(numeros))

            for c in range(0, n_caracteres):
                senha_forte.append(random.choice(caracteres))

            #Embaralhando os elementos da lista senha_forte e transformando em string para o resultado
            senha_embaralhada = ''.join(random.sample(senha_forte, len(senha_forte)))

            if len(senha_embaralhada) < 8:
                print('A senha precisa ter pelo menos 8 caracteres.')
                print('Voltando ao gerador de senhas...')
                sleep(3)
            else:
                print(f'Aqui está a sua senha: {senha_embaralhada}')
                programa_finalizado = True
                break
    else:
        escolha_menu = str(input('Essa opção não está disponível. Deseja voltar ao menu? [SIM/NÃO]: '))
        if escolha_menu.strip().upper() == 'SIM' or escolha_menu.strip().upper() == 'S':
            print('Voltando...')
            sleep(3)
        elif escolha_menu.strip().upper() == 'NÃO' or escolha_menu.strip().upper() == 'NAO' or escolha_menu.strip().\
                upper() == 'N':
            break
        else:
            print('Ocorreu um erro. VOLTANDO AO MENU!')
            sleep(3)

print('-' * 20)
print('Programa finalizado.')
print('-' * 20)
