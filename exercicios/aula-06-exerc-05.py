# ---------------------------------- AULA 06 ----------------------------------
# ---------------------------------- EXER 05 ----------------------------------
# Crie um algoritmo para determinar para onde alguém deve ir com base na sua
# idade. Abaixo está o critério que determina para onde ir:
#   a. se idade for menor que 3 -> vá para o Berçário
#   b. se idade for de 3 até 5 -> vá para a Educação Infantil na Série NX
#       i. a variação das séries (o X) vai do N1 até o N3
#   c. se idade for de 6 até 14 -> vá para o Ensino Fundamental no Ano X
#       i. a variação dos anos (o X) vai do 1º até o 9º
#   d. se idade for de 15 até 17 -> vá para o Ensino Médio no Ano X
#       i. a variação dos anos (o X) vai do 1º até o 3º
#   e. se idade for maior que 17 -> vá para a faculdade
#   f. Exemplo: se o usuário digitar 13, a saída deverá ser “Vá para o Ensino
#       Fundamental no Ano 8”

idade = int(input('Digite sua idade : '))

if idade < 3:
    print('Vá para o Berçário')
# elif idade >= 3 and idade <= 5:
elif idade <= 5:
    # idade = 3,4,5
    serie = idade - 2
    print('Vá para a Educação Infantil na Série N{}'.format(serie))
elif idade <= 14:
    # idade = 6,7,8,9,10,11,12,13,14
    serie = idade - 5
    print('Vá para o Ensino Fundamental no Ano {}'.format(serie))
elif idade <= 17:
    # idade  = 15,16,17
    serie = idade - 14
    print('Vá para o Ensino Médio no Ano {}'.format(serie))
else:
    print('Vá para a faculdade')
