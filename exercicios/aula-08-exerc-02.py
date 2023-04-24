# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 02 ----------------------------------
# Utilizando apenas 2 comandos for, exiba a tabuada dos números 1 a 10.

# método 1
# i vai de 1 até 10
for i in range(1, 11):
    print('tabuada do', i)
    # j vai de 1 até 10
    for j in range(1, 11):
        print(i, '*', j, '=', i * j)
    # imprime uma linha em branco para separar cada tabuada
    print()
