"""
1. Calculadora de Números Romanos.
    a. Crie uma calculadora das operações +, -, *, /, **.
        i. O intervalo de entrada e resultado deve ser (-4000,4000).
        ii. isto é, o valor mínimo recebido e calculado será -3999.
        iii. e o valor máximo recebido e calculado será 3999.
    b. O resultado da divisão deve ser representado como quociente e resto.
    c. A entrada dos dois números deve ser em números romanos.
    d. O resultado deve ser mostrado em números romanos.
    e. Use blocos try / except onde achar necessário, mas seja ESPECÍFICO.
    f. Você deve usar funções, que por sua vez devem estar em um módulo separado.
    g. Todos os cálculos devem ser salvos em um dicionário, que deve ser armazenado em uma lista.
    h. Ao encerrar o programa, todos os cálculos realizados devem ser salvos em um arquivo json.
2. Modelos:
    a. Operação tradicional
        calculo = {'n1': 'X', 'n2': 'IV', 'op': '+', 'res': 'XIV'}
    b. Operação onde foi entrado um valor maior que 3999 ou menor que -3999.
        calculo = {'n1': 'erro', 'n2': 'MM', 'op': '/', 'res': 'erro'}
    c. Modelo usando subtração com algum valor negativo.
        calculo = {'n1': '-C', 'n2': 'X', 'op': '-', 'res': '-CX'}
    d. Modelo de divisão.
        calculo = {'n1': 'XI', 'n2': 'III', 'op': '/', 'res': 'III', '%': 'II'}
"""
