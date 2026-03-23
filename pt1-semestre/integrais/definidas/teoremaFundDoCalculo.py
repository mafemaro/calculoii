""" CÓDIGOS DO PROFESSOR Roney Rachide Nunes!

O código abaixo calcula o valor da integral definida da função f(x) = cos(x) em um intervalo [a, b] utilizando duas abordagens diferentes.

Inicialmente, o programa solicita ao usuário os valores de a, b e o número n de subdivisões do intervalo. Em seguida, calcula o comprimento de cada subintervalo. Com essa divisão, o valor da integral é aproximado por meio de somas de Riemann.

Para isso, o programa percorre os n subintervalos e soma as contribuições da função em diferentes pontos amostrais de cada subintervalo: o extremo direito, o extremo esquerdo, o ponto médio e um ponto aleatório. Cada escolha gera uma aproximação distinta para o valor da integral.

Na segunda parte do código, utiliza-se a biblioteca SymPy para calcular simbolicamente uma função F tal que F′(x) = f(x). Em seguida, aplica-se o Teorema Fundamental do Cálculo para determinar o valor exato da integral definida.

De acordo com esse teorema, se F′(x) = f(x), então a integral definida entre a e b é igual a F(b) − F(a). O programa calcula esse valor substituindo os limites na expressão simbólica de F e exibe o resultado numérico.

Dessa forma, o código permite comparar as aproximações obtidas pelas somas de Riemann com o valor exato fornecido pelo Teorema Fundamental do Cálculo. """

import numpy as np
import sympy as sp
x = sp.symbols('x')

# Lê do usuário o intervalo [a,b].
print("Digite o extremo esquerdo do intervalo de integração.")
a = float(input("a = "))
print()
print("Digite o extremo direito do intervalo de integração.")
b = float(input("b = "))
print()

#Lê do usuário o número de subdivisões do intervalo [a,b].
print("Digite a quantidade de subintervalos utilizada para a aproximação.")
n = int(input("n = "))
print()

# Inicializa as variáveis que armazenarão cada uma das aproximações
integralD = 0 # o ponto amostral será o extremo direito de cada subintervalo
integralE = 0 # o ponto amostral será o extremo esquerdo de cada subintervalo
integralM = 0 # o ponto amostral será o ponto médio de cada subintervalo
integralA = 0 # o ponto amostral será um ponto aleatório cada subintervalo

# Define (simbolicamente) a função que será integrada (permite encontrar F tal que F' = f)
f_sym = sp.cos(x)

# Gera a função numérica
f = sp.lambdify(x, f_sym, 'numpy')

# Define o tamanho de cada subintervalo
Delta_x = (b-a)/n

# Calcula a aproximação para integral de f em [a,b],
# tomando como ponto amostral o extremo direito de cada subintervalo.
for i in range (1,n+1):
    xi = a + i*Delta_x
    integralD = integralD + f(xi)*Delta_x

# Calcula a aproximação para integral de f em [a,b],
# tomando como ponto amostral o extremo esquerdo de cada subintervalo.
for i in range(1, n+1):
    xi = a + (i-1)*Delta_x
    integralE = integralE + f(xi)*Delta_x

# Calcula a aproximação para integral de f em [a,b],
# tomando como ponto amostral o ponto médio de cada subintervalo.
SomaM = 0
for i in range(1, n+1):
    xi = a + (2*i - 1)*Delta_x/2
    integralM = integralM + f(xi)*Delta_x

# Calcula a aproximação para integral de f em [a,b],
# tomando como ponto amostral um ponto aleatório em cada subintervalo.
SomaA = 0
for i in range(1, n+1):
    xi = np.random.uniform(a + (i-1)*Delta_x, a + i*Delta_x)
    integralA = integralA + f(xi)*Delta_x

print()
print(f"Aproximação para a integral definida de f no intervalo [{a},{b}]")
print()
print()
print("a) considerando como ponto amostral o extremo direito de cada subintervalo:")
print(f"{integralD} ")

print()
print("b) considerando como ponto amostral o extremo esquerdo de cada subintervalo:")
print(f"{integralE} ")

print()
print(f"c) considerando como ponto amostral o ponto médio de cada subintervalo:")
print(f"{integralM} ")

print()
print(f"d) considerando como ponto amostral um ponto aleatório de cada subintervalo:")
print(f"{integralA} ")
print()

###################################################################################################

#Determinar uma função F tal que F' = f
F = sp.integrate(f_sym, x)

#Aplicar o Teorema Fundamental do Cálculo
TFC = F.subs(x,b)- F.subs(x,a)

print("Utilizando o Teorema Fundamental do Cálculo,")
print("o valor calculado para integral de f no intervalo [a,b]")
print(f"é {TFC}")