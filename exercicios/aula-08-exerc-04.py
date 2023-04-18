# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 04 ----------------------------------
# Crie um programa que peça para o usuário digitar um texto. Pegue a string e
# separe em 3 listas distintas o que é caractere, número e espaços em branco.
# Depois exiba os conteúdos das listas.
texto = input('Digite um longo texto : ')

# método 1
numeros = []
caracteres = []
espacos = []

for letra in texto:
    if letra.isalpha():
        caracteres.append(letra)
    elif letra.isnumeric():
        numeros.append(letra)
    elif letra == ' ':
        espacos.append(letra)
    else:
        print('descartando :', letra)

print(caracteres)
print(numeros)
print(espacos)

# método 2
numeros = []
caracteres = []
espacos = []

tamanho_texto = len(texto)

for i in range(tamanho_texto):
    if texto[i].isalpha():
        caracteres.append(texto[i])
    elif texto[i].isnumeric():
        numeros.append(texto[i])
    elif texto[i] == ' ':
        espacos.append(texto[i])
    else:
        print('descartando :', texto[i])

print(caracteres)
print(numeros)
print(espacos)
