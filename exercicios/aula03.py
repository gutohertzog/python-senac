import math
# 1. Calcule a raiz quadrada de 64.
print('math.sqrt(64) = ', math.sqrt(64))
# 2. Arredonde o número 3.7 para o inteiro mais próximo.
print('round(3.7, 0) = ', round(3.7, 0))
# 3. Calcule o valor absoluto de -10.
print('abs(-10) = ', abs(-10))
# 4. Calcule o seno de 30 graus.
print('math.sin(30 * 3.14 / 180)) # valores aproximado = ',
      math.sin(30 * 3.14 / 180))  # valores aproximados
# 5. Calcule o cosseno de 45 graus.
print('math.cos(45 * 3.14 / 180) = ', math.cos(45 * 3.14 / 180))
# 6. Calcule a tangente de 60 graus.
print('math.tan(60 * 3.14 / 180) = ', math.tan(60 * 3.14 / 180))
# 7. Arredonde o número 4.2 para o próximo número inteiro maior.
print('math.floor(4.2) = ', math.floor(4.2))
# 8. Calcule o logaritmo natural de 10.
print('math.log10(10) = ', math.log10(10))
# 9. Calcule o logaritmo de 100 na base 10.
print('math.log(100,10) = ', math.log(100, 10))
# 10. Calcule a exponencial de 2.
print('math.pow(2,2) = ', math.pow(2, 2))
# 11. Calcule a potência de 2 elevado a 10.
print('math.pow(2,10) = ', math.pow(2, 10))
# 12. Calcule a raiz quadrada de 144.
print('math.sqrt(144) = ', math.sqrt(144))
# 13. Mostre o valor do pi.
print('math.pi = ', math.pi)
# 14. Calcule a hipotenusa de um triângulo retângulo com catetos de 3 e 4.
hip = 3 ** 2 + 4 ** 2
print('math.pow(hip,0.5) = ', math.pow(hip, 0.5))
# 15. Calcule o arco cosseno de 0.5 em radianos.
print('math.cos(0.5) = ', math.cos(0.5))
# 16. Calcule o arco tangente de 1 em graus.
print('math.tan(1 * 3.14 / 180) = ', math.tan(1 * 3.14 / 180))
# 17. Calcule a função de chão de 5.7.
print('math.floor(5.7) = ', math.floor(5.7))
# 18. Calcule a função de teto de 3.2.
print('math.ceil(3.2) = ', math.ceil(3.2))
# 19. Calcule a raiz cúbica de 27.
print('math.cbrt(27) = ', math.cbrt(27))
print('math.pow(27,1/3) = ', math.pow(27, 1/3))
# 20. Calcule a distância euclidiana entre os pontos(1, 2) e(4, 6).
# como temos apenas dois pontos, calcularemos a distância entre dois pontos bidimensional, que será
# p1 - q1 ao quadrado e p2 - q2 ao quadrado, depois é tirada a raiz quadrada
print('math.sqrt(math.pow(1-4,2) + math.pow(2-6,2)) = ',
      math.sqrt(math.pow(1-4, 2) + math.pow(2-6, 2)))
# 21. Calcule o valor de 2 elevado a 5 usando a função pow().
print('math.pow(2,5) = ', math.pow(2, 5))
# 22. Calcule o valor de 4 elevado a 0.5 e depois use a função sqrt().
print('math.sqrt(math.pow(4,0.5)) = ', math.sqrt(math.pow(4, 0.5)))
# 23. Calcule o logaritmo natural de 10 usando a função log().
print('math.log(10) = ', math.log(10))
# 24. Calcule o valor da função exponencial de 3 usando a função exp().
print('math.exp(3) = ', math.exp(3))
# 25. Arredonde o número 3.14159265359 para o inteiro mais próximo usando a função round().
print('round(3.14159265359) = ', round(3.14159265359))
# 26. Arredonde o número 3.14159265359 para duas casas decimais usando a função round().
print('round(3.14159265359,2) = ', round(3.14159265359, 2))
# 27. Arredonde o número 3.7 para cima usando a função ceil().
print('math.ceil(3.7) = ', math.ceil(3.7))
# 28. Arredonde o número 3.7 para baixo usando a função floor().
print('math.floor(3.7) = ', math.floor(3.7))
# 29. Calcule o valor absoluto de - 5 usando a função fabs().
print('math.fabs(-5) = ', math.fabs(-5))
# 30. Calcule o resto da divisão de 10 por 3 usando a função fmod().
print('math.fmod(10,3) = ', math.fmod(10, 3))
# 31. Calcule o fatorial de 5 usando a função factorial().
print('math.factorial(5) = ', math.factorial(5))
# 32. Calcule o valor de 2 elevado a 10 usando a função pow().
print('math.pow(2,10) = ', math.pow(2, 10))
# 33. Calcule o valor de 9 elevado a 0.5 e depois use a função sqrt().
print('math.sqrt(math.pow(9,0.5)) = ', math.sqrt(math.pow(9, 0.5)))
# 34. Calcule o logaritmo de 100 na base 10 usando a função log10().
print('math.log10(100) = ', math.log10(100))
# 35. Calcule o valor da função exponencial de 2.5 usando a função exp().
print('math.exp(2.5) = ', math.exp(2.5))
# 36. Arredonde o número 4.5678 para o inteiro mais próximo usando a função round().
print('round(4.5678) = ', round(4.5678))
# 37. Arredonde o número 4.5678 para três casas decimais usando a função round().
print('round(4.5678,3) = ', round(4.5678, 3))
# 38. Arredonde o número 4.2 para cima usando a função ceil().
print('math.ceil(4.2) = ', math.ceil(4.2))
# 39. Arredonde o número 4.9 para baixo usando a função floor().
print('math.floor(4.9) = ', math.floor(4.9))
# 40. Calcule o valor absoluto de -10 usando a função fabs().
print('math.fabs(-10) = ', math.fabs(-10))
# 41. Calcule o resto da divisão de 20 por 7 usando a função fmod().
print('math.fmod(20,7) = ', math.fmod(20, 7))
# 42. Calcule o fatorial de 7 usando a função factorial().
print('math.factorial(7) = ', math.factorial(7))
# 43. Calcule o valor de 3 elevado a 4 usando a função pow().
print('math.pow(3,4) = ', math.pow(3, 4))
# 44. Calcule o valor de 25 elevado a 0.5 usando a função sqrt().
print('math.pow(25, 0.5) = ', math.pow(25, 0.5))
# 45. Calcule o logaritmo natural de 5 usando a função log().
print('math.log(5) = ', math.log(5))
# 46. Calcule o valor da função exponencial de 1.5 usando a função exp().
print('math.exp(1.5) = ', math.exp(1.5))
# 47. Arredonde o número 2.71828 para o inteiro mais próximo usando a função round().
print('round(2.71828) = ', round(2.71828))
# 48. Arredonde o número 2.71828 para quatro casas decimais usando a função round().
print('round(2.71828) = ', round(2.71828))
# 49. Arredonde o número 7.6 para cima usando a função ceil().
print('math.ceil(7.6) = ', math.ceil(7.6))
# 50. Arredonde o número 7.1 para baixo usando a função floor().
print('math.floor(7.1) = ', math.floor(7.1))
# 51. Calcule a área de um círculo de raio 5.
print('math.pi * 5 * 5 = ', math.pi * 5 * 5)
# 52. Calcule o perímetro de um quadrado de lado 6.
print('6 * 4 = ', 6 * 4)
# 53. Calcule a área de um retângulo de base 8 e altura 4.
print('8 * 4 = ', 8 * 4)
# 54. Calcule a diagonal de um quadrado de lado 7.
print('7 * math.sqrt(2) = ', 7 * math.sqrt(2))
# 55. Calcule o perímetro de um triângulo equilátero de lado 10.
print('10 * 3 = ', 10 * 3)
# 56. Calcule a área de um trapézio de bases 4 e 8 e altura 5.
print(((4 + 8) * 5) / 2)
# 57. Calcule a hipotenusa de um triângulo retângulo com catetos de 3 e 4.
cateto_1 = 3
cateto_2 = 4
hip = math.pow(cateto_1, 2) + math.pow(cateto_2, 2)
print(math.sqrt(hip))
# 58. Calcule o ângulo entre dois vetores, um com coordenadas(2, 3) e outro com coordenadas(-1, 4).
# u = (2,3)
# v = (-1,4)
uv = (2*(-1)) + (3 * 4)
u = math.sqrt(math.pow(2, 2) + 3 ** 2)
# a raiz de um número nada mais é do que o número elevado a 1/2
v = math.pow((-1) ** 2 + 4 ** 2, 1/2)
theta = uv / (u * v)
angulo = math.acos(theta) * 180 / math.pi
print(angulo)
# 59. Calcule a área de um hexágono regular de lado 7.
lado = 7
area = 6 * ((math.pow(lado, 2) * math.pow(3, 1/2)) / 4)
print('a área é {:.2f}'.format(area))
# 60. Calcule o raio do círculo circunscrito em um triângulo equilátero de lado 9.
lado = 9
raio = lado / math.sqrt(3)
print(raio)
# 61. Calcule a área de um triângulo isósceles com base 10 e altura 8.
base = 10
altura = 8
area = (base * altura) / 2
print(area)
# 62. Calcule a altura de um triângulo equilátero de lado 5.
lado = 5
altura = (lado * math.sqrt(3)) / 2
print(altura)
# 63. Calcule o perímetro de um losango com diagonais de comprimentos 6 e 8.
diagonal_1 = 6
diagonal_2 = 8
perimetro = 4 * math.sqrt(math.pow(diagonal_1, 2) + math.pow(diagonal_2, 2))
print(perimetro)
# 64. Calcule o raio da circunferência inscrita em um triângulo retângulo de catetos 3 e 4.
cateto_1 = 3
cateto_2 = 4
raio = (cateto_1 + cateto_2 -
        math.sqrt(math.pow(cateto_1, 2) + math.pow(cateto_2, 2))) / 2
print(raio)
# 65. Calcule a área de um pentágono regular de lado 12.
lado = 12
area = (5 * math.pow(lado, 2) * math.sqrt(5 + 2 * math.sqrt(5))) / 4
print(area)
# 66. Calcule o ângulo formado pelos ponteiros de um relógio às 3: 45.
hora = 3
minuto = 45
angulo = abs((hora * 30 + minuto * 0.5) - (minuto * 6))
print(angulo)
# 67. Calcule o comprimento da circunferência de um círculo de raio 9.
raio = 9
comprimento = 2 * math.pi * raio
print(comprimento)
# 68. Calcule a área de um triângulo retângulo de hipotenusa 5 e um cateto de comprimento 3.
cateto = 3
hipotenusa = 5
area = (cateto * math.sqrt(math.pow(hipotenusa, 2) - math.pow(cateto, 2))) / 2
print(area)
# 69. Calcule a área de um círculo inscrito em um triângulo equilátero de lado 12.
lado = 12
raio = (lado * math.sqrt(3)) / 6
area = math.pi * math.pow(raio, 2)
print(area)
# 70. Calcule a área de um triângulo isósceles com base 8 e um dos lados de comprimento 5.
base = 8
lado = 5
area = (base * math.sqrt(math.pow(lado, 2) - math.pow(base, 2) / 4)) / 2
print(area)
# 71. Calcule o ângulo entre duas retas, uma com equação y = 2x + 3 e outra com equação y = -3x + 4.
# 72. Calcule a área de um quadrado inscrito em um círculo de raio 10.
raio = 10
area = math.pow(raio, 2) / 2
print(area)
# 73. Calcule o ângulo central correspondente a um arco de 4 unidades em uma circunferência de raio 5.
raio = 5
arco = 4
angulo = (arco * 360) / (2 * math.pi * raio)
print(angulo)
# 74. Calcule o raio do círculo inscrito em um triângulo retângulo de catetos 5 e 12.
cateto_1 = 5
cateto_2 = 12
raio = (cateto_1 + cateto_2 -
        math.sqrt(math.pow(cateto_1, 2) + math.pow(cateto_2, 2))) / 2
print(raio)
# 75. Calcule a área de um triângulo escaleno com lados de comprimentos 7, 9 e 13.
lado_1 = 7
lado_2 = 9
lado_3 = 13
p = (lado_1 + lado_2 + lado_3) / 2
area = math.sqrt(p * (p - lado_1) * (p - lado_2) * (p - lado_3))
print(area)
# 76. Calcule a área de um triângulo retângulo de catetos 6 e 8.
cateto_1 = 6
cateto_2 = 8
area = (cateto_1 * cateto_2) / 2
print(area)
# 77. Calcule a área de um losango com diagonais de comprimentos 10 e 14.
diagonal_1 = 10
diagonal_2 = 14
area = (diagonal_1 * diagonal_2) / 2
print(area)
# 78. Calcule o perímetro de um triângulo isósceles com base 12 e altura 8.
base = 12
altura = 8
perimetro = 2 * base + altura
print(perimetro)
# 79. Calcule o ângulo central correspondente a um arco de 2π/3 unidades em uma circunferência de raio 8.
raio = 8
arco = 2 * math.pi / 3
angulo = (arco * 360) / (2 * math.pi * raio)
print(angulo)
# 80. Calcule o raio do círculo circunscrito em um triângulo retângulo de catetos 6 e 8.
cateto_1 = 6
cateto_2 = 8
raio = (cateto_1 + cateto_2 -
        math.sqrt(math.pow(cateto_1, 2) + math.pow(cateto_2, 2))) / 2
print(raio)
# 81. Calcule a área lateral de um cilindro de raio 3 e altura 6.
raio = 3
altura = 6
area_lateral = 2 * math.pi * raio * altura
print(area_lateral)
# 82. Calcule a área total de uma pirâmide de base quadrada de lado 5 e altura 8.
lado = 5
altura = 8
area_total = math.pow(lado, 2) + 4 * (lado * altura) / 2
print(area_total)
# 83. Calcule o volume de um cubo de aresta 4.
aresta = 4
volume = math.pow(aresta, 3)
print(volume)
# 84. Calcule a área lateral de um cone de raio 2 e geratriz 5.
raio = 2
geratriz = 5
area_lateral = math.pi * raio * geratriz
print(area_lateral)
# 85. Calcule o volume de uma esfera de raio 6.
raio = 6
volume = (4 * math.pi * math.pow(raio, 3)) / 3
print(volume)
# 86. Calcule a área total de um prisma triangular de base com lados 6, 8 e 10 e altura 12.
lado_1 = 6
lado_2 = 8
lado_3 = 10
altura = 12
area_total = 2 * (lado_1 * altura) / 2 + 2 * (lado_2 *
                                              altura) / 2 + 2 * (lado_3 * altura) / 2
print(area_total)
# 87. Calcule o volume de um cilindro de raio 5 e altura 10.
raio = 5
altura = 10
volume = math.pi * math.pow(raio, 2) * altura
print(volume)
# 88. Calcule a área lateral de uma pirâmide de base hexagonal de lado 6 e altura 8.
lado = 6
altura = 8
area_lateral = 6 * (lado * altura) / 2
print(area_lateral)
# 89. Calcule o volume de um tetraedro regular de aresta 7.
aresta = 7
volume = math.pow(aresta, 3) / (6 * math.sqrt(2))
print(volume)
# 90. Calcule a área total de um paralelepípedo retângulo de arestas 5, 8 e 12.
aresta_1 = 5
aresta_2 = 8
aresta_3 = 12
area_total = 2 * (aresta_1 * aresta_2) + 2 * \
    (aresta_1 * aresta_3) + 2 * (aresta_2 * aresta_3)
print(area_total)
# 91. Calcule o volume de um cone de raio 3 e altura 7.
raio = 3
altura = 7
volume = (math.pi * math.pow(raio, 2) * altura) / 3
print(volume)
# 92. Calcule a área lateral de um prisma de base pentagonal de lado 4 e altura 9.
lado = 4
altura = 9
area_lateral = 5 * (lado * altura) / 2
print(area_lateral)
# 93. Calcule o volume de uma pirâmide de base quadrada de lado 10 e altura 6.
lado = 10
altura = 6
volume = (math.pow(lado, 2) * altura) / 3
print(volume)
# 94. Calcule a área total de um cilindro de raio 2 e altura 10.
raio = 2
altura = 10
area_total = 2 * math.pi * raio * (raio + altura)
print(area_total)
# 95. Calcule o volume de uma esfera circunscrita em um cubo de aresta 4.
aresta = 4
volume = (math.pow(aresta, 3) * math.pi) / 6
print(volume)
# 96. Calcule a área lateral de um cone de raio 4 e geratriz 9.
raio = 4
geratriz = 9
area_lateral = math.pi * raio * geratriz
print(area_lateral)
# 97. Calcule o volume de um prisma de base retangular de lados 7 e 9 e altura 12.
lado_1 = 7
lado_2 = 9
altura = 12
volume = (lado_1 * lado_2 * altura) / 2
print(volume)
# 98. Calcule a área total de um tetraedro regular de aresta 5.
aresta = 5
area_total = math.sqrt(3) * math.pow(aresta, 2)
print(area_total)
# 99. Calcule o volume de um paralelepípedo retângulo de arestas 3, 6 e 9.
aresta_1 = 3
aresta_2 = 6
aresta_3 = 9
volume = aresta_1 * aresta_2 * aresta_3
print(volume)
# 100. Calcule a área lateral de uma pirâmide de base triangular de lados 8, 10 e 12 e altura 7.
lado_1 = 8
lado_2 = 10
lado_3 = 12
altura = 7
area_lateral = (lado_1 * altura) / 2 + (lado_2 * altura) / \
    2 + (lado_3 * altura) / 2
print(area_lateral)
# 101. Calcule o volume de um cilindro de raio 7 e altura 12.
raio = 7
altura = 12
volume = math.pi * math.pow(raio, 2) * altura
print(volume)
# 102. Calcule a área total de uma esfera de raio 10.
raio = 10
area_total = 4 * math.pi * math.pow(raio, 2)
print(area_total)
# 103. Calcule o volume de um cone de raio 6 e altura 10.
raio = 6
altura = 10
volume = (math.pi * math.pow(raio, 2) * altura) / 3
print(volume)
# 104. Calcule a área lateral de um prisma de base hexagonal de lado 3 e altura 8.
lado = 3
altura = 8
area_lateral = 6 * (lado * altura) / 2
print(area_lateral)
# 105. Calcule o volume de uma pirâmide de base quadrada de lado 8 e altura 10.
lado = 8
altura = 10
volume = (math.pow(lado, 2) * altura) / 3
print(volume)
# 106. Calcule a área total de um cubo de aresta 6.
aresta = 6
area_total = 6 * math.pow(aresta, 2)
print(area_total)
# 107. Calcule o volume de um tetraedro regular de aresta 9.
aresta = 9
volume = math.pow(aresta, 3) / (6 * math.sqrt(2))
print(volume)
# 108. Calcule a área lateral de um cilindro de raio 8 e altura 15.
raio = 8
altura = 15
area_lateral = 2 * math.pi * raio * altura
print(area_lateral)
# 109. Calcule o volume de uma pirâmide de base triangular de lados 7, 8 e 9 e altura 12.
lado_1 = 7
lado_2 = 8
lado_3 = 9
altura = 12
volume = (lado_1 * altura) / 2 + (lado_2 * altura) / 2 + (lado_3 * altura) / 2
print(volume)
# 110. Calcule a área total de um prisma de base retangular de lados 5 e 7 e altura 10.
lado_1 = 5
lado_2 = 7
altura = 10
area_total = 2 * (lado_1 * lado_2 + lado_1 * altura + lado_2 * altura)
print(area_total)
# 111. Use a função help() para encontrar informações sobre a função print().
print(help(print))
# 112. Use a função help() para encontrar informações sobre o módulo math.
print(help(math))
# 113. Use a função help() para encontrar informações sobre a classe str.
print(help(str))
# 114. Use a função help() para encontrar informações sobre a função abs().
print(help(abs))
# 115. Use a função help() para encontrar informações sobre a função round().
print(help(round))
# 116. Use a função help() para encontrar informações sobre a classe int.
print(help(int))
# 117. Use a função help() para encontrar informações sobre a classe float.
print(help(float))
# 118. Use a função help() para encontrar informações sobre a função type().
print(help(type))
# 119. Use a função help() para encontrar informações sobre o import .
# print(help(import))
# 120. Use a função help() para encontrar informações sobre a função input().
print(help(input))

# Mais Complexos
# 1. Calcule o valor da função exponencial de 4 elevado a raiz quadrada de 9, arredondando para duas casas decimais.
print('{:.2f}'.format(math.pow(math.exp(4), math.sqrt(9))))
# 2. Calcule o logaritmo na base 2 do valor absoluto de -16, elevado a 0.5, arredondando para o inteiro mais próximo.
resultado = math.log(math.pow(abs(-16), 0.5), 2)
print(round(resultado))
# 3. Calcule o valor da função exponencial de 3 elevado ao valor absoluto de -5, multiplicado pelo fatorial de 4, arredondando para uma casa decimal.
resultado = math.exp(math.pow(3, abs(-5))) * math.factorial(4)
resultado = round(resultado, 1)
print(resultado)
# 4. Calcule o valor de 2 elevado ao logaritmo na base 2 de 8, arredondando para o inteiro mais próximo.
resultado = math.pow(2, math.log(2, 8))
print(round(resultado))
# 5. Calcule o valor absoluto do resto da divisão de 17 por 5, elevado ao cubo, arredondando para três casas decimais.
resultado = abs(math.pow(17 % 5, 3))
print(round(resultado, 3))
# 6. Calcule o valor da função exponencial de 2 elevado ao valor absoluto de -3, arredondando para o inteiro mais próximo, e em seguida, calcule o fatorial desse valor.
resultado = math.exp(math.pow(2, abs(-3)))
print(round(resultado))
# 7. Calcule o valor da função exponencial de 4 elevado a raiz quadrada de 16, dividido pelo logaritmo natural de 2, arredondando para duas casas decimais.
resultado = math.exp(math.pow(4, math.sqrt(16))) / math.log(2)
print(round(resultado, 2))
# 8. Calcule o logaritmo na base 10 do valor absoluto do resto da divisão de 18 por 5, elevado ao cubo, arredondando para o inteiro mais próximo.
resultado = math.log10(abs(math.pow(18 % 5, 3)))
print(round(resultado))
# 9. Calcule o valor absoluto do resto da divisão de 23 por 6, elevado ao valor absoluto de -2, arredondando para três casas decimais, e em seguida, calcule o fatorial desse valor.
resultado = abs(math.pow(23 % 6, abs(-2)))
resultado = round(resultado, 3)
print(math.factorial(int(resultado)))
# 10. Calcule o valor da função exponencial de 5 elevado ao valor absoluto de -4, dividido pelo logaritmo natural de 3 elevado ao cubo, arredondando para uma casa decimal.
resultado = math.exp(math.pow(5, abs(-4))) / math.log(math.pow(3, 3))
resultado = round(resultado, 1)
print(resultado)
# 11. Calcule a área de um triângulo de lados 5, 7 e 9.
lado_1 = 5
lado_2 = 7
lado_3 = 9
semi_perimetro = (lado_1 + lado_2 + lado_3) / 2
area = math.sqrt(semi_perimetro * (semi_perimetro - lado_1) *
                 (semi_perimetro - lado_2) * (semi_perimetro - lado_3))
print(area)
# 12. Calcule o volume de um cilindro oblíquo de altura 10, raio da base 4 e geratriz 8.
altura = 10
raio = 4
geratriz = 8
area_base = math.pi * math.pow(raio, 2)
area_lateral = geratriz * 2 * math.pi * raio
volume = area_base * altura
print(volume)
# 13. Calcule a área lateral de um cone circular reto inscrito em uma esfera de raio 10.
raio = 10
area_base = math.pi * math.pow(raio, 2)
area_lateral = area_base * 2
print(area_lateral)
# 14. Calcule o volume de um prisma hexagonal regular de aresta 5 e altura 8.
aresta = 5
altura = 8
area_base = 3 * math.sqrt(3) * math.pow(aresta, 2) / 2
volume = area_base * altura
print(volume)
# 15. Calcule a área total de um toro de raio maior 7 e raio menor 3.
raio_maior = 7
raio_menor = 3
area_total = 4 * math.pi * math.pow(raio_maior, 2) * math.pow(raio_menor, 2)
print(area_total)
# 16. Calcule o volume de uma esfera de raio 12 inscrita em um dodecaedro regular de aresta 8.
raio = 12
aresta = 8
volume = 1 / 3 * math.pi * math.pow(raio, 3)
print(volume)
# 17. Calcule a área total de um icosaedro regular de aresta 5.
aresta = 5
area_total = 5 * math.sqrt(3) * math.pow(aresta, 2)
print(area_total)
# 18. Calcule o volume de um cone circular reto de raio da base 6 e altura 10, inscrito em um cilindro circular reto de raio da base 8 e altura 15.
raio_cone = 6
altura_cone = 10
raio_cilindro = 8
altura_cilindro = 15
volume_cone = 1 / 3 * math.pi * math.pow(raio_cone, 2) * altura_cone
volume_cilindro = math.pi * math.pow(raio_cilindro, 2) * altura_cilindro
volume = volume_cilindro - volume_cone
print(volume)
# 19. Calcule a área lateral de um tronco de cone circular reto de raios da base maiores 10 e menores 5 e altura 12.
raio_maior = 10
raio_menor = 5
altura = 12
area_lateral = math.pi * (raio_maior + raio_menor) * math.sqrt(
    math.pow(altura, 2) + math.pow(raio_maior - raio_menor, 2))
print(area_lateral)
# 20. Calcule o volume de um octaedro regular de aresta 10, inscrito em uma esfera de raio 15.
aresta = 10
raio = 15
volume = 1 / 3 * math.sqrt(2) * math.pow(aresta, 3)
print(volume)
