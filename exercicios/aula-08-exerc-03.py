# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 03 ----------------------------------
# Crie um algoritmo que peça uma frase a um usuário. Converta para uma lista.
# Verifique qual é a maior palavra da lista. Ao final mostre a maior palavra,
# quantas letras ela tem e em qual posição ela foi encontrada.

texto = input('Digite um longo texto : ')
lista = texto.split()

indice = 0
maior_indice = 0
maior_palavra = ''

for palavra in lista:
    if len(maior_palavra) < len(palavra):
        maior_palavra = palavra
        maior_indice = indice
    indice += 1

print('maior palavra :', maior_palavra)
print('índice dela :', maior_indice)
print('Tamanho dela :', len(maior_palavra))
