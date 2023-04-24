# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 04 ----------------------------------
# Crie um programa que peça para o usuário digitar um texto. Pegue a string e
# separe em 3 listas distintas o que é caractere, número e espaços em branco.
# Depois exiba os conteúdos das listas.
texto = input('Digite um longo texto : ')

# método 1
# Listas para armazenar os resultados
numeros = []
caracteres = []
espacos = []

# Para cada letra no texto
for letra in texto:
    # Se for alfanumérico (letra do alfabeto)
    if letra.isalpha():
        # Adiciona a letra à lista de caracteres
        caracteres.append(letra)
    # Se for um número
    elif letra.isnumeric():
        # Adiciona o número à lista de números
        numeros.append(letra)
    # Se for um espaço em branco
    elif letra == ' ':
        # Adiciona o espaço à lista de espaços
        espacos.append(letra)
    # Se não for nenhum desses casos
    else:
        # Exibe uma mensagem indicando que a letra será ignorada
        print('descartando :', letra)

# Exibe os resultados
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

# método 3
# esse método não utiliza os métodos das strings para separar os caracteres
# Criação de listas vazias
caracteres = []
numeros = []
espacos = []

# Percorre a string caracter por caracter
for i in texto:
    # Verifica se o caracter é um número
    if i in "0123456789":
        numeros.append(i)
    # Verifica se o caracter é um espaço em branco
    elif i in " ":
        espacos.append(i)
    # Caso não seja nenhum dos anteriores, é um caracter
    else:
        caracteres.append(i)

# Imprime as listas criadas
print("Caracteres:", caracteres)
print("Números:", numeros)
print("Espaços em branco:", espacos)
