# ---------------------------------- AULA 06 ----------------------------------
# ---------------------------------- EXER 03 ----------------------------------
# Crie um programa que peça a idade do usuário.
#   a. Se ele for menor de 16, avise que ele não pode votar ainda;
#   b. Se ele tiver entre 16 e 17 anos, avise que o voto é opcional;
#   c. Se ele tiver entre 18 e 65, avise que o voto é obrigatório;
#   d. Se ele tiver mais que 65 anos, avise que o voto é opcional;

idade = int(input('Digite sua idade : '))
print(idade)

# método 1
if idade < 16:
    print('Você é muito novo para votar!')
# elif idade >= 18 and idade <= 65:
# elif idade > 17 and idade < 66:
elif 17 < idade < 66:
    print('Você é obrigado a votar!')
# vai sobrar quem tem 16, 17 e maiores que 66
else:
    print('Seu voto é opcional!')

# método 2
if idade == 16 or idade == 17 or idade >= 65:
    print('Seu voto é opcional!')
elif idade >= 18:
    print('Você é obrigado a votar!')
else:
    print('Você é muito novo para votar!')

# método 3
if idade < 16:
    print('Você é muito novo para votar!')
elif (idade > 15 and idade < 18) or idade > 64:
    print('Seu voto é opcional!')
else:
    print('Você é obrigado a votar!')
