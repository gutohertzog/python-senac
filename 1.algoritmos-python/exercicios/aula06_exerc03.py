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
# Verifica se a idade é igual ou maior que 18 anos
if idade >= 18:
    # Se sim, imprime que o voto é obrigatório
    print('Seu voto é obrigatório!')
# Se não, verifica se é maior ou igual a 16 anos ou maior ou igual a 65 anos
elif idade >= 16 or idade >= 65:
    # Se sim, imprime que o voto é opcional
    print('Seu voto é opcional!')
# Se não, imprime que a pessoa é muito nova para votar
else:
    print('Você é muito novo para votar!')

# método 3
# Verifica se a idade é menor que 16
if idade < 16:
    # Se sim, imprime na tela que o voto é opcional
    print('Você é muito novo para votar!')
# Verifica se a idade é maior que 15 e menor que 18 ou se é maior que 64
elif (idade > 15 and idade < 18) or idade > 64:
    # Se sim, imprime na tela que o voto é opcional
    print('Seu voto é opcional!')
# Se não, imprime na tela que o voto é obrigatório
else:
    print('Você é obrigado a votar!')

# método 4
# esse método descarta entradas com idades menores que 1
if idade >= 1 and idade < 16:
    print ("vc ainda não pode votar")
elif idade >= 16 and idade <= 17:
    print ("voto eh opcional")
elif idade >= 18 and idade <= 65:
    print ("voto eh obrigatório")
elif idade > 65:
    print ("voto eh opcional")
else:
    print ("essa idade não existe!!!!")
