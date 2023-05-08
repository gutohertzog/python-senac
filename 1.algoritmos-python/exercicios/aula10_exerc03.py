# ---------------------------------- AULA 10 ----------------------------------
# ---------------------------------- EXER 03 ----------------------------------
# Árvore de Natal !
# Crie um algoritmo que construa uma árvore de Natal.
# Seu programa deve perguntar ao usuário que altura ele gostaria a árvore. Depois de responder, seu programa deve desenhar a árvore com a altura desejada pelo usuário.

# Dicas:
# • para o desenvolvimento, fixe o valor 5 para sua árvore, deixe para pedir o tamanho apenas no final
# • você terá que usar 1 while e 3 for loops "#" para uma árvore de tamanho 5 :
# • abaixo há uma lista do número de espaço e do número de “
#   - 4 - 1
#   - 3 - 3
#   - 2 - 5
#   - 1 - 7
#   - 0 - 9
#   - 4 - 1 (tronco)
# • passos do seu programa:
#   - decrementar os espaços em 1 a cada repetição;
#   - incrementar 1 "#" em 2 a cada repetição;
#   - reservar 1 linha para o tronco da árvore;
#   - decrementar a altura da árvore até chegar em 0;
#   - imprimir os espaços e então a "#" para cada linha;
#   - imprimir os espaços e depois 1 "#" para o tronco;

altura = int(input('digite a altura da árvore : '))
# altura = 5

# método 1
i = 0
espaco = altura - 1
folhas = 1
while i < altura:
    # Desenha os espaços
    for j in range(espaco):
        print(' ', end='')
    # Desenha as folhas
    for j in range(folhas):
        print('#', end='')
    # Pula para a próxima linha
    print()

    # Aumenta o número de folhas e diminui os espaços
    folhas += 2
    espaco -= 1
    i += 1

espaco = altura - 1
# Desenha o tronco
for j in range(espaco):
    print(' ', end='')
print('@')

# método 2
i = 0
espaco = altura - 1
folhas = 1
while i < altura:
    print(' ' * espaco, end='')
    print('#' * folhas)

    folhas += 2
    espaco -= 1
    i += 1
espaco = altura - 1
for j in range(espaco):
    print(' ', end='')
print('@')

# método 3
i = 0
espaco = altura - 1
folhas = 1
while i < altura:
    print(' ' * espaco, '#' * folhas, sep='')

    folhas += 2
    espaco -= 1
    i += 1
espaco = altura - 1
for j in range(espaco):
    print(' ', end='')
print('@')

# método 4
i = 0
espaco = altura - 1
folhas = 1
while i < altura:
    texto = ' ' * espaco
    texto += '#' * folhas
    print(texto)

    folhas += 2
    espaco -= 1
    i += 1
espaco = altura - 1
for j in range(espaco):
    print(' ', end='')
print('@')
