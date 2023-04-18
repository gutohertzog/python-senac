# ---------------------------------- AULA 08 ----------------------------------
# ---------------------------------- EXER 02 ----------------------------------
# Utilizando apenas 2 comandos for, exiba a tabuada dos números 1 a 10.

for i in range(1, 11):
    print('tabuada do', i)
    for j in range(1, 11):
        print(i, '*', j, '=', i * j)
    print()
