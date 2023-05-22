"""módulo resposável por conter todas as funções que serão usados no programa"""

# constante que serão usadas por todas as funções
# -------------------------------------------------------------------------------------------------
# dicionários completos
ARAB_ROM: dict[int, str] = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
    50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
ROM_ARAB: dict[str, int] = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
    'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

# dicionário que contém as quantidades máximas de repetições de cada algarismo romano
REPETICOES: dict[str, int] = {
    'I': 3, 'V': 1, 'X': 3, 'L': 1, 'C': 3, 'D': 1, 'M': 3}


# -------------------------------------------------------------------------------------------------
# funções que realizam as conversões
# todas as conversões serão feitas em números arábicos já validados pelo tamanho ou
# em números romanos já validados pela quantidade de algarismos e ordem
def converte_arab_rom(num_arab: int) -> str:
    """função para converter números arábicos em romanos
    o número recebido já estará no intervalo de -3999 e 3999
    """
    num_rom: str = ''
    # primeiro tem que verificar se o número é negativo
    if num_arab < 0:
        # se for, adiciona o 'menos' na frente do número romano a ser gerado
        num_rom += '-'
        # e transforma o número em positivo
        num_arab *= -1

    # agora, vai passar por cada algarismo romano
    for valor, alg_rom in sorted(ARAB_ROM.items(), reverse=True):
        # enquanto o número arábico for maior ou igual ao valor do algarismo romano
        # segue adicionando o algarismo romano ao num_rom
        while num_arab >= valor:
            num_rom += alg_rom
            num_arab -= valor

    return num_rom


def converte_rom_arab(num_rom: str) -> int:
    """função para converter números romanos em arábicos
    o número recebido já estará validado pela quantidade de algarismos e ordem
    """
    num_arab: int = 0
    # variável que vai guardar se o número romano é negativo
    eh_negativo: bool = False
    # primeiro, tem que verificar se o número romano é negativo
    if num_rom[0] == '-':
        # se for, transforma o número em positivo
        num_rom = num_rom[1:]
        eh_negativo = True

    # agora, vai passar por cada algarismo romano
    for indice, algarismo in enumerate(num_rom):
        # vai pegar o valor do algarismo romano
        valor: int = ROM_ARAB[algarismo]
        # se o valor do próximo algarismo for maior que o valor do algarismo atual
        if indice < len(num_rom) - 1 and ROM_ARAB[num_rom[indice + 1]] > valor:
            # subtrai o valor do algarismo atual
            num_arab -= valor
        # se não for, soma o valor do algarismo atual
        else:
            num_arab += valor

    # se o número romano for negativo, transforma o número arábico em negativo
    if eh_negativo:
        num_arab *= -1

    return num_arab


# -------------------------------------------------------------------------------------------------
# funções que realizam a validação dos números romanos
def valida_quantidade(num_rom: str) -> bool:
    """função que valida a quantidade de algarismos romanos
        exemplo: XXX é válido, mas IVIII não é
    se for inválido, vai retornar False, se for válido, vai retornar True"""
    # vai passar por cada algarismo
    for algarismo in num_rom:
        # vai contar quantas vezes o algarismo aparece
        quantidade: int = num_rom.count(algarismo)
        # vai verificar se a quantidade é maior que a permitida
        if quantidade > REPETICOES[algarismo]:
            # se for maior, retorna False
            return False
    # se nenhum for algarismo for maior que o permitido, retorna True
    return True


def valida_ordem(num_rom: str) -> bool:
    """os números romanos possuem uma ordem específica para serem válidos,
        exemplo: o número XXIV é válido, mas o número IXXV não é,
    logo, essa função tem por objetivo validar essa ordem
    vai retornar True caso a ordem esteja correta e False caso não esteja
    Essa validação será feita após a validação de quantidade;
    """
    indice: int = 0
    # primeiro, a validação mais fácil de realizar é a de números compostos
    while indice < len(num_rom) - 1:
        algarismo = num_rom[indice]
        # validações para o algarismos I
        if algarismo == 'I':
            # se a valida_I retornar False, o número é inválido
            if not valida_i(num_rom[indice + 1:]):
                return False
        # validações para o algarismos V
        if algarismo == 'V':
            # se a valida_V retornar False, o número é inválido
            if not valida_v(num_rom[indice + 1:]):
                return False
        # validações para o algarismos X
        if algarismo == 'X':
            # se a valida_X retornar False, o número é inválido
            if not valida_x(num_rom[indice + 1:]):
                return False
        # validações para o algarismos L
        if algarismo == 'L':
            # se a valida_L retornar False, o número é inválido
            if not valida_l(num_rom[indice + 1:]):
                return False
        # validações para o algarismos C
        if algarismo == 'C':
            # se a valida_C retornar False, o número é inválido
            if not valida_c(num_rom[indice + 1:]):
                return False
        # validações para o algarismos D
        if algarismo == 'D':
            # se a valida_D retornar False, o número é inválido
            if not valida_d(num_rom[indice + 1:]):
                return False

        indice += 1

    return True


def valida_i(seguintes: str) -> bool:
    """validação específica para o algarismo I"""
    # verificando para os algarismos proibidos depois de I
    for alg in 'LCDM':
        # se algum proibido estiver depois de I, o número é inválido
        if alg in seguintes:
            return False
    # depois, verifica se a quantidade de X é maior que 1 após ele
    # (V já foi verificado na validação de quantidade)
    if seguintes.count('X') > 1:
        return False
    # exluindo os casos de IIV, por exemplo
    for alg in 'VX':
        # se o algarismo estiver a partir da segunda posição de I, o número é inválido
        if alg in seguintes[1:]:
            return False
    return True


def valida_v(seguintes: str) -> bool:
    """validação específica para o algarismo V"""
    # verificando para os algarismos proibidos depois de V
    for alg in 'XLCDM':
        # se algum proibido estiver depois de V, o número é inválido
        if alg in seguintes:
            return False
    return True


def valida_x(seguintes: str) -> bool:
    """validação específica para o algarismo X"""
    # verificando para os algarismos proibidos depois de X
    for alg in 'DM':
        # se algum proibido estiver depois de X, o número é inválido
        if alg in seguintes:
            return False
    # depois, verifica se a quantidade de C é maior que 1 após ele
    # (L já foi verificado na validação de quantidade)
    if seguintes.count('C') > 1:
        return False
    # exluindo os casos de XXC, por exemplo
    for alg in 'LC':
        # se o algarismo estiver a partir da segunda posição de X, o número é inválido
        if alg in seguintes[1:]:
            return False
    return True


def valida_l(seguintes: str) -> bool:
    """validação específica para o algarismo L"""
    # verificando para os algarismos proibidos depois de L
    for alg in 'CDM':
        # se algum proibido estiver depois de L, o número é inválido
        if alg in seguintes:
            return False
    return True


def valida_c(seguintes: str) -> bool:
    """validação específica para o algarismo C"""
    # como C não tem restrição quanto ao algarismos após ele, não é necessário fazer
    # a validação dele como os menores que ele
    # mas é preciso verificar se a quantidade de M é maior que 1 depois dele
    # (D já foi verificado na validação de quantidade)
    if seguintes.count('M') > 1:
        return False
    # exluindo os casos de CCM, por exemplo
    for alg in 'DM':
        # se o algarismo estiver a partir da segunda posição de C, o número é inválido
        if alg in seguintes[1:]:
            return False
    return True


def valida_d(seguintes: str) -> bool:
    """validação específica para o algarismo D"""
    # verificando para os algarismos proibidos depois de D
    if 'M' in seguintes:
        return False
    return True


# -------------------------------------------------------------------------------------------------
# funções tradicionais que realizam as operações matemáticas pedidas
def soma(num_1: int, num_2: int) -> int:
    """função que soma dois números em arábico"""
    resultado: int = num_1 + num_2
    return resultado


def subtrai(num_1: int, num_2: int) -> int:
    """função que subtrai dois números em arábico"""
    resultado: int = num_1 - num_2
    return resultado


def multiplica(num_1: int, num_2: int) -> int:
    """função que multiplica dois números em arábico"""
    resultado: int = num_1 * num_2
    return resultado


def divide(num_1: int, num_2: int) -> tuple:
    """função que divide dois números em arábico"""
    resultado: int = num_1 // num_2
    resto: int = num_1 % num_2
    return resultado, resto


def potencia(num_1: int, num_2: int) -> int:
    """função que calcula a potência de dois números em arábico"""
    resultado: int = num_1 ** num_2
    return resultado


# -------------------------------------------------------------------------------------------------
# funções para testar as funções anteriores
def testa_validade(lista: list[str]) -> None:
    """função para realizar os testes de validade"""
    for numero in lista:
        resultado_quant = valida_quantidade(numero)
        print(f"{numero} é quantidade válido? {resultado_quant}")
        if resultado_quant:
            resultado_ordem = valida_ordem(numero)
            print(f"{numero} é ordem válido? {resultado_ordem}")
        print("-" * 20)
    print("-" * 50)


def testa_conversao_rom_arab(lista: list[str]) -> None:
    """função para realizar os testes de conversão"""
    for numero in lista:
        if valida_quantidade(numero) and valida_ordem(numero):
            resultado = converte_rom_arab(numero)
            print(f"{numero} em arábico é {resultado}")
            print("-" * 20)
    print("-" * 50)


def testa_convesao_arab_rom(lista: list[int]) -> None:
    """função para realizar os testes de conversão"""
    for numero in lista:
        if -3999 <= numero <= 3999:
            resultado = converte_arab_rom(numero)
            print(f"{numero} em romano é {resultado}")
            print("-" * 20)
    print("-" * 50)


# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    numeros_romanos = [
        "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
        "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
        "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
        "MMMMCMXCIX", "MMMMCMXCIXI", "MMMMCMXCIXII", "MMMMCMXCIXIII", "MMMMCMXCIXIV", "MMMMCMXCIXV", "MMMMCMXCIXVI", "MMMMCMXCIXVII", "MMMMCMXCIXVIII", "MMMMCMXCIXIX",
        "XLL", "LLX", "CCD", "CMMI", "MMXMM", "XM", "VV", "IIV", "IIIIII", "IIX",
        "MMMMM", "IM", "IMM", "IMMM", "IMMMM", "IMMMMM", "IMMMMMM", "IMMMMMMM", "IMMMMMMMM", "IMMMMMMMMM"
    ]
    numeros_arabicos = [
        -3999, -3000, -2000, -1000, -999, -500, -499, -100, -99, -50,
        -49, -10, -9, -5, -4, -1, 0, 1, 4, 5,
        9, 10, 40, 49, 50, 90, 99, 100, 400, 499,
        500, 900, 999, 1000, 1999, 2000, 2999, 3000, 3999, 4000,
        5000, 6000, 7000, 8000, 9000, 9999, 10000, 20000, 30000, 40000
    ]

    testa_validade(numeros_romanos)
    testa_conversao_rom_arab(numeros_romanos)
    testa_convesao_arab_rom(numeros_arabicos)
