"""
A atividade de recuperação é destinada aos alunos que não atingiram a pontuação média de 60%.

O objetivo é desenvolver uma calculadora das operações de:
• Soma
• Subtração
• Multiplicação
• Divisão e resto
• Potenciação

Requisitos Obrigatórios
1. Usar apenas o que foi visto em aula até o dia 05 de maio.
2. Todas as operações matemáticas devem ser realizadas apenas usando os operadores de soma e
subtração.
3. Após cada operação, deve ser mostrado uma mensagem ao usuário informando os números da operação
e o resultado.
4. O programa deve possuir uma função principal de execução com o menu do programa (similar ao da
agenda que foi feito em aula).
a. Essa função principal deve possuir um loop while para gerar o menu e passar pelas funções dos
cálculos.
5. Cada uma das operações deve ser feita em funções individuais.
    a. Logo, seu programa possuirá ao menos 6 funções (1 para o menu principal e 5 para as
    operações).
6. Se achar necessário, funções adicionais podem ser criadas (como uma para exibir o menu, outra
para pegar o dado do usuário etc.).
7. Todas as operações devem ser guardadas em um dicionário com o seguinte formato:
    a. {'num_1': 10, 'num_2': 5, 'operacao': '+', 'resultado': 15}
    b. Caso a operação seja de divisão, armazene também o resto.
        {num_1': 10, 'num_2': 5, 'operacao': '/', 'resultado': 2, 'resto': 0}
    c. Caso a divisão seja por zero, salve o resultado como erro.
        {num_1': 10, 'num_2': 0, 'operacao': '/', 'resultado': 'erro'}
    d. As chaves são apenas um modelo. Elas podem ser alteradas a critério do programador.
8. Todas as operações realizadas devem ser armazenadas em uma lista.
9. Para encerrar o programa, o usuário deverá digitar "sair" quando for escolher a operação que
quer realizar.
10.  Quando o programa terminar, todas as operações realizadas devem ser mostradas uma embaixo da
outra, como os exemplos acima (isto é, um print individual por dicionário).
"""


def menu():
    """Função que mostra o menu e retorna a opção escolhida pelo usuário"""
    print('bem-vindo à calculadora')
    print('1. adição')
    print('2. subtração')
    print('3. multiplicação')
    print('4. divisão')
    print('5. potenciação')
    print('0. sair')
    opcao = input(' >> ')
    return opcao


def main():
    """função principal do programa. Vai gerenciar o loop while e a lista de operações."""
    # variável que vai armazenar as operações
    operacoes = []

    # loop while para gerenciar o programa
    while True:
        operacao = {}
        opc = menu()

        # como o break interrompe o loop while, não é necessário usar o elif após o if
        if opc == '0':
            break

        # início das operações
        if opc == '1':
            volta = soma()
            operacao['num_1'] = volta[0]
            operacao['num_2'] = volta[1]
            operacao['operacao'] = '+'
            operacao['resultado'] = volta[-1]
            operacoes.append(operacao)
        elif opc == '2':
            volta = subtracao()
            operacao['num_1'] = volta[0]
            operacao['num_2'] = volta[1]
            operacao['operacao'] = '-'
            operacao['resultado'] = volta[-1]
            operacoes.append(operacao)
        elif opc == '3':
            volta = multiplicacao()
            operacao['num_1'] = volta[0]
            operacao['num_2'] = volta[1]
            operacao['operacao'] = '*'
            operacao['resultado'] = volta[-1]
            operacoes.append(operacao)
        elif opc == '4':
            volta = divisao()
            if 'erro' in volta:
                operacao['num_1'] = volta[0]
                operacao['num_2'] = volta[1]
                operacao['operacao'] = '/'
                operacao['resultado'] = volta[-1]
                operacoes.append(operacao)
            else:
                operacao['num_1'] = volta[0]
                operacao['num_2'] = volta[1]
                operacao['operacao'] = '/'
                operacao['resultado'] = volta[2]
                operacao['resto'] = volta[3]
                operacoes.append(operacao)
        elif opc == '5':
            volta = potenciacao()
            operacao['num_1'] = volta[0]
            operacao['num_2'] = volta[1]
            operacao['operacao'] = '**'
            operacao['resultado'] = volta[2]
            operacoes.append(operacao)
        else:
            print('Opção incorreta.')
    mostra_operacoes(operacoes)


def recebe_numeros():
    """Função que recebe dois número do usuário e os retorna"""
    n1 = int(input('Digite o primeiro número : '))
    n2 = int(input('Digite o segundo número : '))
    return n1, n2


def mostra_operacoes(lista):
    """Mostra as operações realizadas ao final do programa"""
    for item in lista:
        print(item)


def soma():
    """Soma dois números e retorna os números junto com o resultado"""
    n1, n2 = recebe_numeros()
    resultado = n1 + n2

    print(f'{n1} + {n2} = {resultado}')

    return n1, n2, resultado


def subtracao():
    """Subtrai o segundo número do primeiro e retorna os números junto com o resultado"""
    n1, n2 = recebe_numeros()

    resultado = n1 - n2

    print(f'{n1} - {n2} = {resultado}')

    return n1, n2, resultado


def multiplicacao():
    """soma o primeiro o total de vezes pelo segundo"""
    n1, n2 = recebe_numeros()

    resultado = realiza_multiplicacao(n1, n2)

    return n1, n2, resultado


def divisao():
    """realiza a divisão com resto"""
    # n1 ó o dividendo e n2 é o divisor
    n1, n2 = recebe_numeros()

    if n2 == 0:
        print('Não posso dividir por 0!')
        return n1, n2, 'erro'

    quoc, rest = realiza_divisao(n1, n2)

    return n1, n2, quoc, rest


def potenciacao():
    """realiza a potenciação"""
    # n1 é a base e n2 é o expoente
    n1, n2 = recebe_numeros()

    # contador do expoente
    cont_exp = 1
    # o resultado começa em 1 porque é a identidade da multiplicação
    resultado = 1
    while cont_exp <= n2:
        resultado = realiza_multiplicacao(resultado, n1)
        cont_exp += 1
    return n1, n2, resultado


def realiza_multiplicacao(n1, n2):
    """Função para realizar a multiplicação usando apenas a soma e retornar o resultado"""
    resultado = 0
    contador = 0
    while contador < n2:
        resultado += n1
        contador += 1
    return resultado


def realiza_divisao(dividendo, divisor):
    """Função para realizar a divisão usando apenas a subtração e retornar o resultado"""
    quociente = 0
    resto = dividendo
    while resto >= divisor:
        resto -= divisor
        quociente += 1
    return quociente, resto


# a partir daqui teremos funções alternativas para as operações

def soma_recursiva(n1, n2):
    """realiza a soma de forma recursiva"""
    if n2 == 0:
        return n1
    return soma_recursiva(n1 + 1, n2 - 1)


def subtracao_recursiva(n1, n2):
    """realiza a subtração de forma recursiva"""
    if n2 == 0:
        return n1
    return subtracao_recursiva(n1 - 1, n2 - 1)


def multiplicacao_recursiva(n1, n2):
    """realiza a multiplicação de forma recursiva"""
    if n2 == 1:
        return n1
    return n1 + multiplicacao_recursiva(n1, n2 - 1)


def divisao_recursiva(dividendo, divisor):
    """realiza a divisão de forma recursiva"""
    if dividendo < divisor:
        return 0, dividendo
    quociente, resto = divisao_recursiva(dividendo - divisor, divisor)
    return quociente + 1, resto


def potenciacao_recursiva(base, expoente):
    """realiza a potenciação de forma recursiva"""
    if expoente == 0:
        return 1
    return base * potenciacao_recursiva(base, expoente - 1)
