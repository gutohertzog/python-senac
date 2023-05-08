# ---------------------------------- AULA 10 ----------------------------------
# ---------------------------------- EXER 01 ----------------------------------
# Crie um programa que peça ao usuário para digitar uma palavra e imprima a palavra em formato de escada crescente usando um loop while.
# Exemplo: se o usuário digitar "Gandalf", deve ter a saída:
# G
# Ga
# Gan
# Gand
# Ganda
# Gandal
# Gandalf
palavra = input('digite algo : ')

# método 1
# 1. A variável i é inicializada com o valor 0, que é o índice do primeiro caractere da cadeia de caracteres.
# 2. O loop while continua até que i seja igual ao comprimento da string, então o loop continuará até que i seja igual ao tamanho.
# 3. Dentro do loop, a função print() imprime a fatia da cadeia de caracteres do índice 0 para i+1 (i+1 porque o índice de parada não está incluído), que é o mesmo que a fatia de 0 para i, exceto que inclui o caractere no índice i.
# 4. A variável i é incrementada em 1 após cada iteração do loop.
# 5. Quando i for igual ao tamanho da palavra, o loop termina e o programa termina.
i = 0
while i < len(palavra):
    print('palavra[:{}] = {}'.format(i+1, palavra[:i+1]))
    i += 1

# método 2
i = 1
while i < len(palavra) + 1:
    for letra in palavra[:i]:
        print(letra, end='')
    print()
    i += 1
