# ---------------------------------- AULA 10 ----------------------------------
# ---------------------------------- EXER 02 ----------------------------------
# Crie um programa que peça um texto ao usuário e converta cada letra em seu respectivo número. Exemplo: o usuário digitou "a nao", vai ser convertido para "0100140115", onde o "01" representa o "a", o "14" representa o "n", o "15" representa o "o" e o “00” representa o espaço. Desconsidere palavras acentuadas, números e pontuações.

alfabeto = ' abcdefghijklmnopqrstuvwxyz'
print(len(alfabeto))

texto = input('Digite qualquer coisa : ')
texto = texto.lower()

# método 1
# variável que armazenará o texto convertido
convertido = ''
# percorre cada caracter do texto
# variável que armazenará a posição do caracter no alfabeto
for caracter in texto:
    i = 0
    # percorre cada caracter do alfabeto
    while i < len(alfabeto):
        # compara o caracter do texto com o caracter do alfabeto
        if caracter == alfabeto[i]:
            # se i for menor que 10
            if i < 10:
                # adiciona um 0 antes da posição
                convertido += '0' + str(i)
            # se não
            else:
                # adiciona a posição
                convertido += str(i)
            # sai do loop
            break
        # incrementa o valor de i, que vai testar a próxima letra do alfabeto
        i += 1

# exibe o texto
print('texto =', texto)
# exibe o texto convertido
print('convertido =', convertido)
