#Importando a biblioteca random e string
import random
import string

#Criando variáveis com as letras, números e caracteres usados na senha forte
letras = string.ascii_letters
numeros = string.digits
caracteres = string.punctuation

#Fazendo um input para retornar a quantidade de cada número, letra e caracter
n_letras = int(input('Quantas letras você quer em sua senha?\n'))
n_numeros = int(input('Quantos números você quer em sua senha?\n'))
n_caracteres = int(input('Quantos caracteres você quer em sua senha?\n'))

#Adicionando uma lista para guardar o que vai ser utilizado na senha forte
senha_forte = []

#Utilizando a estrutura de repetição FOR junto com a biblioteca random para determinar o que vai ser utilizado na senha
# forte
for c in range(0, n_letras):
    senha_forte += random.choice(letras)

for c in range(0, n_numeros):
    senha_forte += random.choice(numeros)

for c in range(0, n_caracteres):
    senha_forte += random.choice(caracteres)

#Embaralhando os elementos da lista senha_forte e transformando em string para o resultado final
senha_embaralhada = ''.join(random.sample(senha_forte, len(senha_forte)))

print(senha_embaralhada)
