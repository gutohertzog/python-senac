# Programação Funcional vs Programação Orientada a Objetos #

- - - -

## 1. Programação Funcional ##

A programação funcional (`Functional Programming - FP`) é um paradigma de programação que se baseia em funções matemáticas puras para resolver problemas computacionais. Em vez de se preocupar com o estado e a modificação dos dados, a programação funcional se concentra em aplicar funções aos dados de entrada para produzir dados de saída.

As funções utilizadas na programação funcional são geralmente puras, ou seja, não possuem efeitos colaterais e sempre retornam o mesmo resultado dado os mesmos argumentos. Isso torna a programação funcional mais previsível e fácil de testar e depurar.

Algumas das características mais importantes da programação funcional incluem a imutabilidade dos dados, o uso de funções de primeira classe e a composição de funções. A programação funcional é comumente usada em conjunto com outros paradigmas de programação, como a programação orientada a objetos e a programação imperativa.

Na programação funcional, as funções são utilizadas como principais mecanismos de operação, ao invés de se usar comandos e estruturas de fluxo de controle como while, if, etc.. As funções são tratadas como valores, ou seja, podem ser passadas como argumentos para outras funções, retornadas como resultado de outras funções e atribuídas a variáveis.

A programação funcional se baseia em três princípios principais :
- `Imutabilidade` : os dados não são modificados, e sim produzidos novos dados a partir de dados antigos. Isso torna a programação funcional mais segura e previsível, pois as funções não causam efeitos colaterais indesejados;
- `Funções puras` : as funções são puras, ou seja, não produzem efeitos colaterais e sempre retornam o mesmo resultado dado os mesmos argumentos. Isso torna a programação funcional mais previsível e fácil de testar e depurar;
- `Composição de funções` : As funções podem ser compostas para criar funções mais complexas. Isso torna a programação funcional mais legível e manutenível, pois as funções são pequenas e fáceis de entender;

Alguns exemplos de como a programação funcional é utilizada incluem filtrar, mapear e reduzir dados, encadeamento de funções, trabalhar com funções de alta ordem, programação com currying e programação com closures.

No geral, a programação funcional é uma forma de pensar e resolver problemas computacionais baseada em funções matemáticas puras, imutabilidade de dados e composição de funções. Ela é diferente de outros paradigmas de programação, como a programação orientada a objetos e a programação imperativa, que se concentram em mudar o estado dos dados e usar comandos e estruturas de fluxo de controle.

Seguem alguns exemplos de como a programação funcional é usada :

### 1.1. `Função anônima` ###

```python
soma = lambda x, y: x + y
print(soma(2, 3))
# Saída: 5
```
Neste exemplo, usamos uma função anônima `lambda` para criar uma função simples de soma.

### 1.2. `Filtro` ###
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))
# Saída: [2, 4, 6, 8, 10]
```
Neste exemplo, usamos a função `filter()` para filtrar os números pares de uma lista de números. A função `filter()` recebe uma função condicional e uma lista, e retorna um iterável com os elementos da lista que satisfazem a condição.

### 1.3. `Mapa` ###
```python
numeros = [1, 2, 3, 4, 5]
quadrado = map(lambda x: x ** 2, numeros)
print(list(quadrado))
# Saída: [1, 4, 9, 16, 25]
```
Neste exemplo, usamos a função `map()` para aplicar a função de elevar ao quadrado em cada elemento de uma lista de números.

### 1.4. `Redução` ###
```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)
# Saída: 15
```
Neste exemplo, usamos a função `reduce()` do módulo `functools` para calcular a soma dos elementos de uma lista de números. A função `reduce()` recebe uma função de acumulação e uma lista, e retorna o resultado acumulado de aplicar a função aos elementos da lista.

### 1.5. `Encadeamento de funções` ###
```python
from functools import compose

def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

transformacao = compose(triplo, dobro)
print(transformacao(3))
# Saída: 18
```
Neste exemplo, usamos a função `compose()` do módulo `functools` para encadear as funções de dobro e triplo. A função `compose()` recebe uma série de funções e retorna uma nova função que aplica as funções fornecidas na ordem inversa.

### 1.6. `Programação com currying` ###
```python
from functools import partial

def multiplicar(x, y, z):
    return x * y * z

dobrar = partial(multiplicar, 2)
print(dobrar(3, 4))
# Saída: 24
```
Neste exemplo, usamos a função `partial()` do módulo `functools` para aplicar currying na função multiplicar. A função `partial()` recebe uma função e um conjunto de argumentos fixos e retorna uma nova função com os argumentos fixados.

- - - -

## 2. Programação Orientada a Objeto ##

A programação orientada a objeto (`Object-oriented Programming - OOP`) é um paradigma de programação que se baseia na idéia de objetos, que são entidades que possuem estado (dados) e comportamento (métodos). Cada objeto é uma instância de uma classe, que define o tipo de objeto e seus atributos e métodos.

A programação orientada a objeto se concentra em modelar o mundo real como objetos e classes, e em encapsular o estado e o comportamento dos objetos para proteger a integridade dos dados. Isso torna a programação orientada a objeto mais fácil de entender, manter e expandir.

Algumas das características mais importantes da programação orientada a objeto incluem a abstração, a herança, a polimorfismo, e a sobrecarga de métodos. A programação orientada a objeto é comumente usada em conjunto com outros paradigmas de programação, como a programação funcional e a programação imperativa.
Na programação orientada a objeto, os dados e seus comportamentos são agrupados em entidades chamadas objetos. Cada objeto é uma instância de uma classe, que define o tipo de objeto e seus atributos e métodos.

Cada classe tem seus próprios atributos e métodos, que descrevem o estado e o comportamento do objeto. Os atributos representam as características do objeto e os métodos representam as ações que o objeto pode realizar. Os métodos são funções que são executadas em um objeto específico.

A programação orientada a objeto se baseia em quatro princípios principais:
- `Abstração` : Permite representar apenas os aspectos relevantes de um objeto, escondendo sua implementação detalhada. Isso torna a programação orientada a objeto mais fácil de entender e manter;
- `Encapsulamento` : Protege o estado interno dos objetos, impedindo que ele seja acessado ou modificado diretamente. Isso torna a programação orientada a objeto mais segura e previsível;
- `Herança` : Permite que uma classe herde os atributos e métodos de outra classe. Isso torna a programação orientada a objeto mais organizada e reutilizável;
- `Polimorfismo` : Permite que objetos de diferentes classes sejam tratados como objetos de uma classe pai. Isso torna a programação orientada a objeto mais flexível e escalável;
Além dos princípios mencionados, a programação orientada a objeto também se baseia em outras características e conceitos, como :
- `Instância` : Cada objeto é uma instância de uma classe, ou seja, é uma cópia da classe que contém seus próprios atributos e métodos;
- `Mensagem` : Os objetos se comunicam entre si enviando e recebendo mensagens, que são chamadas de métodos;
- `Construtor` : É um método especial que é chamado quando um objeto é criado, geralmente é utilizado para inicializar os atributos do objeto;
- `Destrutor` : É um método especial que é chamado quando um objeto é destruído, geralmente é utilizado para limpar recursos do sistema alocados pelo objeto;
- `Sobrecarga de métodos` : é a possibilidade de um mesmo método ter comportamentos diferentes dependendo do tipo de argumentos passados;

Na programação orientada a objeto, os objetos são os principais mecanismos de operação, e as classes são utilizadas para definir o tipo e comportamento dos objetos. A programação orientada a objeto tem como objetivo modelar o mundo real como objetos e classes, e encapsular o estado e o comportamento dos objetos para proteger a integridade dos dados.
Seguem alguns exemplos de como a programação orientada a objeto é usada :

### 2.1. `Classe` ###
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("João", 30)
pessoa.saudacao()
# Saída: Olá, meu nome é João e tenho 30 anos.
```
Neste exemplo, criamos uma classe `Pessoa` que possui um construtor `__init__` para inicializar os atributos nome e idade do objeto, além de um método `saudacao()` que imprime uma saudação com o nome e idade da pessoa.

### 2.2. `Abstração` ###
```python
class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return 3.14 * self.raio ** 2
```
Neste exemplo, temos uma classe abstrata `Forma` com o método `area()`, e duas classes que herdam dela, `Quadrado` e `Circulo`, que implementam o método `area()` de acordo com as suas necessidades, mostrando assim a abstração.

### 2.3. `Encapsulamento` ###
```python
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return self.__saldo
        else:
            return "Saldo insuficiente."

conta = Conta(1000)
print(conta.depositar(500))
# Saída: 1500
print(conta.sacar(2000))
# Saída: "Saldo insuficiente."
```
Neste exemplo, criamos uma classe `Conta` que possui atributo de saldo e métodos de depositar e sacar, e os atributos saldo está encapsulado, impedindo que seja acessado ou modificado diretamente.

### 2.4. `Herança` ###
```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
        
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou funcionário com o cargo de {self.cargo}.")

funcionario = Funcionario("Maria", 25, "Gerente")
funcionario.saudacao()
# Saída: Olá, meu nome é Maria, tenho 25 anos e sou funcionário com o cargo de Gerente.
```
Neste exemplo, criamos uma classe `Funcionario` que herda da classe `Pessoa`. A classe `Funcionario` possui um atributo adicional `cargo` e um método `saudacao()` que imprime uma saudação com o nome, idade e cargo do funcionário.

### 2.5. `Polimorfismo` ###
```python
class Gerente(Funcionario):
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome}, sou gerente e responsável por {self.cargo}.")

gerente = Gerente("Lucas", 35, "Vendas")
gerente.saudacao()
# Saída: Olá, meu nome é Lucas, sou gerente e responsável por Vendas.
```
Neste exemplo, criamos uma classe `Gerente` que herda da classe `Funcionario`, e tem um comportamento diferente no método saudacao, mostrando assim o polimorfismo.

### 2.6. `Instância` ###
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("João")
p2 = Pessoa("Maria")

print(p1.nome)
# Saída: "João"
print(p2.nome)
# Saída: "Maria"
```
Neste exemplo, criamos duas instâncias da classe `Pessoa`, p1 e p2, cada uma com seus próprios atributos e métodos.

### 2.7. `Mensagem` ###
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
    def saudacao(self):
        return f"Olá, meu nome é {self.nome}."

p = Pessoa("João")
print(p.saudacao())
# Saída: "Olá, meu nome é João."
```
Neste exemplo, o objeto p envia uma mensagem de saudação ao método `saudacao`, retornando o resultado da expressão.

### 2.8. `Construtor` ###
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("João", 30)
print(p.nome)
# Saída: "João"
print(p.idade)
# Saída: 30
```
Neste exemplo, o construtor `__init__` é usado para inicializar os atributos nome e idade do objeto quando é criado.

### 2.9. `Destrutor` ###
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __del__(self):
        print(f"{self.nome} foi removido.")

p = Pessoa("João")
del p
# Saída: "João foi removido."
```
Neste exemplo, o destrutor `__del__` é usado para executar uma ação quando o objeto é destruído, no caso imprimindo uma mensagem informando que o objeto foi removido.

Obs: O destrutor `del`, não é garantido que será chamado, depende da implementação do interpretador, e em alguns casos pode não ser chamado.

### 2.10. `Sobrecarga de métodos` ###
```c++
#include <iostream>

class Calculadora {
public:
    int soma(int x, int y) {
        return x + y;
    }

    int soma(int x, int y, int z) {
        return x + y + z;
    }
};

int main() {
    Calculadora calculadora;
    std::cout << calculadora.soma(1, 2) << std::endl;
    // Saída: 3
    std::cout << calculadora.soma(1, 2, 3) << std::endl;
    // Saída: 6

    return 0;
}
```
Neste exemplo, a classe `Calculadora` tem dois métodos chamados soma, mas com assinaturas diferentes, um que recebe 2 argumentos e outro que recebe 3 argumentos, mostrando assim a sobrecarga de métodos. Isso pode ser útil em situações onde é necessário ter diferentes comportamentos para a mesma ação, dependendo dos argumentos passados.

O Python não tem suporte a sobrecarga, então o exemplo é feito usando C++.

Esses são alguns exemplos básicos de como a programação orientada a objeto é usada. A programação orientada a objeto pode ser usada para modelar uma grande variedade de problemas, desde simples até complexos, e é comumente usada em diversas áreas, como desenvolvimento de jogos, aplicativos web e mobile, inteligência artificial, entre outros.

- - - -

## 3. FP vs OOP ##

A `programação orientada a objetos (OOP)` e a `programação funcional (FP)` são duas abordagens diferentes para a construção de software. Ambas têm suas próprias vantagens e desvantagens, e muitas vezes são usadas em conjunto para resolver problemas de programação.

- `OOP` se concentra em objetos, que são instâncias de classes. Cada objeto tem seus próprios dados (estado) e métodos (comportamento). O objetivo da `OOP` é encapsular dados e comportamentos em objetos individuais para facilitar a reutilização do código e a manutenção do software;
- `FP` se concentra em funções puras, que são funções que sempre retornam o mesmo resultado para um determinado conjunto de entradas e não têm efeitos colaterais. O objetivo da `FP` é evitar efeitos colaterais e permitir que as funções sejam testadas e compreendidas de forma independente;

Enquanto a `OOP` é mais voltada para a construção de sistemas complexos, a `FP` é mais voltada para o desenvolvimento de algoritmos eficientes e escaláveis. Ambas as abordagens têm suas vantagens e desvantagens, e muitas vezes são usadas em conjunto para resolver problemas de programação.

### 3.1. Quando a FP é mais indicada que a OOP
A programação funcional (FP) é mais indicada que a programação orientada a objetos (OOP) em algumas situações, incluindo :

- `Processamento paralelo e distribuído` : A FP é mais adequada para o processamento paralelo e distribuído, pois as funções puras são fáceis de paralelizar e distribuir, enquanto que a OOP pode ser mais complexa devido ao gerenciamento de estado compartilhado entre objetos;
- `Algoritmos matemáticos e estatísticos` : A FP é mais adequada para a implementação de algoritmos matemáticos e estatísticos, pois as funções puras são fáceis de testar e compreender, enquanto que a OOP pode ser mais complexa devido ao gerenciamento de estado e comportamento;
- `Programação reativa` : A FP é mais adequada para a programação reativa, pois as funções puras são fáceis de encadear e composicionar para criar fluxos de dados complexos, enquanto que a OOP pode ser mais complexa devido ao gerenciamento de estado e eventos;
- `Testes unitários` : A FP é mais adequada para testes unitários, pois as funções puras são fáceis de testar e não dependem de estado externo, enquanto que a OOP pode ser mais complexa devido ao gerenciamento de estado e comportamento;

É importante notar que a programação funcional e orientada a objetos não são mutuamente exclusivas, e muitas vezes são utilizadas juntas, dependendo do problema a ser resolvido.
Aqui está um exemplo de como a programação funcional (FP) pode ser melhor do que a programação orientada a objetos (OOP), usando a operação de mapeamento de uma lista :
```python
# Exemplo de programação funcional
def quadrado(val):
    return val**2

numeros = [1, 2, 3, 4, 5]
quadrados = map(quadrado, numeros)
print(list(quadrados))
# Saída: [1, 4, 9, 16, 25]
```
Neste exemplo, usamos a função `map()` para aplicar a função `quadrado` em cada elemento da lista `numeros`. Como a função `quadrado` é pura (não tem efeitos colaterais) e não depende de estado externo, este é um exemplo de como a programação funcional pode ser mais simples e eficiente do que a programação orientada a objetos.

Aqui está um exemplo equivalente usando programação orientada a objetos :
```python
# Exemplo de programação orientada a objetos
class Numero:
    def __init__(self,val):
        self.val = val
    def quadrado(self):
        return self.val**2

numeros = [Numero(1), Numero(2), Numero(3), Numero(4), Numero(5)]
quadrados = [num.quadrado() for num in numeros]
print(quadrados)
# Saída: [1, 4, 9, 16, 25]
```
Neste exemplo, criamos uma classe `Numero` para representar cada elemento da lista, e criamos um método `quadrado()` para calcular o quadrado de cada elemento. Enquanto a programação orientada a objetos é útil para modelar problemas do mundo real e gerenciar estado, neste caso ela pode ser mais complexa e menos eficiente do que a programação funcional.

### 3.2. Quando a OOP é mais indicada que a FP ###
A programação orientada a objetos (OOP) é melhor do que a programação funcional (FP) em algumas situações, incluindo:

- `Modelagem de problemas` : OOP é melhor para modelar problemas do mundo real, pois permite que os programadores criem objetos que representam conceitos reais, como pessoas, animais, carros, etc;
- `Projetos de grande escala` : OOP é melhor para projetos de grande escala, pois permite que os programadores dividam um projeto em classes e objetos menores e mais fáceis de gerenciar;
- `Interação com usuário` : OOP é melhor para projetos que precisam lidar com interfaces gráficas de usuário (GUIs), pois permite que os programadores criem classes e objetos que representam elementos da GUI, como botões, caixas de texto, etc;
- `Desenvolvimento de software orientado a eventos` : OOP é melhor para o desenvolvimento de software orientado a eventos, pois permite que os programadores criem classes e objetos que representam eventos e gerenciem a lógica de negócios para esses eventos;
- `Herança` : OOP permite a implementação de relações de herança entre classes, permitindo a criação de hierarquias de classes, onde uma classe pode herdar atributos e métodos de outra classe, o que pode ser uma vantagem em alguns casos;

Novamente, é importante lembrar que a programação orientada a objetos e funcional não são mutuamente exclusivas e muitas vezes são utilizadas juntas, dependendo do problema a ser resolvido.
Aqui estão alguns exemplos de como a programação orientada a objetos (OOP) pode ser melhor do que a programação funcional (FP) :
```python
class Conta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            raise ValueError("Saldo insuficiente")

conta1 = Conta(1000)
print(conta1.depositar(500))
# Saída: 1500
print(conta1.sacar(1000))
# Saída: 500
```
Neste exemplo, usamos a programação orientada a objetos para modelar uma conta bancária, com seus métodos e atributos, como depósito e saque. Isso é melhor do que a programação funcional pois torna mais fácil entender e gerenciar o estado da conta.

Aqui está um exemplo equivalente à classe de Conta que usei anteriormente, mas implementado com programação funcional :
```python
def depositar(conta, valor):
    return conta + valor

def sacar(conta, valor):
    if conta >= valor:
        return conta - valor
    else:
        raise ValueError("Saldo insuficiente")

saldo = 1000
saldo = depositar(saldo, 500)
print(saldo)
# Saída: 1500
saldo = sacar(saldo, 1000)
print(saldo)
# Saída: 500
```
Neste exemplo, em vez de usar classes e objetos para modelar a conta e seus métodos, usamos funções puras para representar as operações de depósito e saque. A variável `saldo` representa o estado atual da conta. As funções `depositar()` e `sacar()` não precisam de nenhum estado interno, elas operam apenas sobre o estado externo (saldo) e retornam o novo estado.

Abaixo temos mais um exemplo em um projeto maior :
```python
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self.matricula = matricula
    def trabalhar(self):
        print("Trabalhando")

class Gerente(Funcionario):
    def __init__(self,nome,idade,matricula,senha):
        super().__init__(nome,idade,matricula)
        self.senha = senha
    def gerenciar(self):
        print("Gerenciando")

gerente = Gerente("João",35,"G001","senha123")
print(gerente.nome)
# Saída: João
gerente.gerenciar()
# Saída: Gerenciando
```
Neste exemplo, usamos a programação orientada a objetos para modelar uma hierarquia de classes, onde temos `Pessoa`, `Funcionario` e `Gerente`, cada uma com seus atributos e métodos específicos. Isso é melhor do que a programação funcional pois torna mais fácil dividir um projeto em módulos menores e mais fáceis de gerenciar.

Abaixo temos um exemplo equivalente à hierarquia de classes Pessoa, Funcionário e Gerente, mas implementado com programação funcional :
```python
def cria_pessoa(nome, idade):
    return {"nome": nome, "idade": idade}

def cria_funcionario(pessoa, matricula):
    return {**pessoa, "matricula": matricula, "trabalhar": lambda: print("Trabalhando")}

def cria_gerente(funcionario, senha):
    return {**funcionario, "senha": senha, "gerenciar": lambda: print("Gerenciando")}

pessoa = cria_pessoa("João", 35)
funcionario = cria_funcionario(pessoa, "F001")
gerente = cria_gerente(funcionario, "senha123")

print(gerente["nome"])
# Saída: João
gerente["gerenciar"]()
# Saída: Gerenciando
```
Neste exemplo, em vez de usar classes e objetos para modelar a hierarquia de pessoas, funcionários e gerentes, usamos dicionários e funções para representar as entidades e suas características. Cada entidade é representada por um dicionário de atributos e funções, e as funções `cria_pessoa()`, `cria_funcionario()` e `cria_gerente()` são usadas para criar as entidades e adicionar as características apropriadas.

- - - -

## 4. Considerações Finais ##

A programação funcional e a programação orientada a objetos são dois paradigmas de programação distintos, cada um com suas próprias vantagens e desvantagens.

A programação funcional se baseia em funções matemáticas puras, sem efeitos colaterais, e enfatiza a composição de funções ao invés de herança e modificação de estado. Isso pode tornar o código mais fácil de entender e testar, além de facilitar a paralelização e distribuição de tarefas. Além disso, a programação funcional é uma boa escolha para trabalhar com grandes conjuntos de dados, como processamento de dados em cluster.

Por outro lado, a programação orientada a objetos se baseia em modelos de objetos que possuem estado e comportamento, e enfatiza a herança e a composição de objetos ao invés de funções. Isso pode tornar o código mais fácil de entender e manter, além de ser uma boa escolha para modelar problemas complexos e desenvolvimento de aplicações de alta escala.

Em geral, ambos os paradigmas têm seus usos e aplicações específicas, e o escolha do melhor depende do problema que se pretende resolver. Alguns projetos podem se beneficiar mais da programação funcional, enquanto outros podem se beneficiar mais da programação orientada a objetos. Em alguns casos, pode ser benéfico utilizar a programação funcional e orientada a objetos juntas, combinando as vantagens de ambos os paradigmas.

É importante notar que ambas as programação funcional e orientada a objetos são ferramentas poderosas e cada uma tem sua própria filosofia e abordagem para resolver problemas. O desenvolvedor deve estar ciente das diferenças entre elas e saber quando usar cada uma delas.

A programação funcional é uma boa escolha para trabalhar com grandes conjuntos de dados, como processamento de dados em cluster, enquanto que a programação orientada a objetos é uma boa escolha para modelar problemas complexos e desenvolvimento de aplicações de alta escala.

Em resumo, a programação funcional e orientada a objetos são dois paradigmas distintos, cada um com suas próprias vantagens e desvantagens e o escolha do melhor depende do problema que se pretende resolver.
