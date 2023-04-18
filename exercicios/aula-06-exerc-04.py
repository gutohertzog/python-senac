# ---------------------------------- AULA 06 ----------------------------------
# ---------------------------------- EXER 04 ----------------------------------
# Crie uma calculadora. Seu programa deve ter 3 inputs. O primeiro pegará um
# número float, o segundo irá pegar a operação aritmética a ser realizada
# (adição, subtração, multiplicação, divisão e potência) e o terceiro input
# deve pegar o segundo número em formato float. Mostre o resultado da operação
# em um texto completo, como abaixo:
#   a. A equação é : 2 ** 6 = 64
#   b. Onde o primeiro input foi 2, o segundo input foi ** e o terceiro foi 6.
#   c. Avise o usuário caso a operação inserida seja inválida.
#   d. Se a operação for de divisão e o segundo número for 0, avise “Impossível
#       dividir por zero”.

num1 = input('Digite um número : ')
oper = input('Escolha uma das seguintes operações + - * / ** : ')
num2 = input('Digite outro número : ')

# método 1
if oper == '+':
    num1 = float(num1)
    num2 = float(num2)
    result = num1 + num2
    print('A equação é : {} + {} = {}'.format(num1, num2, result))
elif oper == '-':
    num1 = float(num1)
    num2 = float(num2)
    result = num1 - num2
    print('A equação é : {} - {} = {}'.format(num1, num2, result))
elif oper == '*':
    num1 = float(num1)
    num2 = float(num2)
    result = num1 * num2
    print('A equação é : {} * {} = {}'.format(num1, num2, result))
elif oper == '/':
    if num2 == '0':
        print('não posso dividir por 0')
    else:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
        print('A equação é : {} / {} = {}'.format(num1, num2, result))
elif oper == '**':
    num1 = float(num1)
    num2 = float(num2)
    result = num1 ** num2
    print('A equação é : {} ** {} = {}'.format(num1, num2, result))
else:
    print('não sei que operação é essa!')

# método 2
# testa para divisão por zero
if oper == '/' and num2 == '0':
    print('não posso dividir por 0')
# verifica se o operador está incorreto
elif oper != '+' or oper != '-' or oper != '*' or oper != '/' or oper != '**':
    print('não sei que operação é essa!')
# operador correto, realiza o cálculo
else:
    if oper == '+':
        result = float(num1) + float(num2)
    elif oper == '-':
        result = float(num1) - float(num2)
    elif oper == '*':
        result = float(num1) * float(num2)
    elif oper == '/':
        result = float(num1) / float(num2)
    else:
        result = float(num1) ** float(num2)
    print('A equação é : {} {} {} = {}'.format(num1, oper, num2, result))
