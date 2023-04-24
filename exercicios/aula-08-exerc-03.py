# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 03 ----------------------------------
# Crie um algoritmo que peça uma frase a um usuário. Converta para uma lista.
# Verifique qual é a maior palavra da lista. Ao final mostre a maior palavra,
# quantas letras ela tem e em qual posição ela foi encontrada.

# Recebe o texto
texto = input('Digite um longo texto : ')
# Separa o texto em palavras
lista = texto.split()

# Inicializa variáveis de controle
indice = 0
maior_indice = 0
maior_palavra = ''

# Percorre a lista de palavras
for palavra in lista:
    # Verifica se a palavra atual é maior que a maior_palavra
    if len(maior_palavra) < len(palavra):
        maior_palavra = palavra
        maior_indice = indice

    # Incrementa o índice
    indice += 1

# Imprime os resultados
print('maior palavra :', maior_palavra)
print('índice dela :', maior_indice)
print('Tamanho dela :', len(maior_palavra))
