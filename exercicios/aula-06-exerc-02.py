# ---------------------------------- AULA 06 ----------------------------------
# ---------------------------------- EXER 02 ----------------------------------
# Crie um algoritmo que verifique se o número digitado é positivo ou negativo e
# se é par ou ímpar. Se for ímpar, que informe se ele é múltiplo de 3, 5 ou 7.

numero = int(input('Digite um número inteiro qualquer : '))

# testa para positivo
if numero > 0:
    print('é positivo')
    # testa para par
    if numero % 2 == 0:
        print('é par')
    # se não é par, só pode ser ímpar
    else:
        print('é ímpar')
        # teste para os respectivos múltiplos
        if numero % 3 == 0:
            print('é múltiplo de 3')
        elif numero % 5 == 0:
            print('é múltiplo de 5')
        elif numero % 7 == 0:
            print('é múltiplo de 7')
        # não é múltiplo de nenhum acima
        else:
            print('não é múltiplo de 3, 5 ou 7')
# testa para negativo
elif numero < 0:
    print('é negativo')
    # testa para par
    if numero % 2 == 0:
        print('é par')
    # se não é par, só pode ser ímpar
    else:
        print('é ímpar')
        # teste para os respectivos múltiplos
        # vai mostrar apenas o primeiro múltiplo
        if numero % 3 == 0:
            print('é múltiplo de 3')
        elif numero % 5 == 0:
            print('é múltiplo de 5')
        elif numero % 7 == 0:
            print('é múltiplo de 7')
        else:
            print('não é múltiplo de 3, 5 ou 7')
else:
    print('é zero')
