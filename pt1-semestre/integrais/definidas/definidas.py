""" CÓDIGOS DO PROFESSOR Roney Rachide Nunes!

O código abaixo calcula uma aproximação para a integral definida de uma função contínua f em um intervalo entre dois pontos, utilizando uma soma de Riemann.

Inicialmente, o programa solicita ao usuário os valores dos extremos do intervalo de integração, bem como o número de subdivisões que serão usadas na aproximação.

Em seguida, define-se a função f(x) e calcula-se o comprimento de cada subintervalo.

O programa então percorre cada um dos subintervalos utilizando um laço de repetição e determina o ponto correspondente ao extremo direito de cada subintervalo. Para cada um desses pontos, calcula-se o valor da função multiplicado pelo tamanho do subintervalo, e esse valor é adicionado à soma total.

Ao final do processo, o valor acumulado fornece uma aproximação para a integral definida.

Quanto maior for o número de subdivisões, mais precisa tende a ser essa aproximação. """

import math

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

# Inicializa a variável que armazenará a aproximação da integral definida.
integral = 0

# Define a função que delimita a região cuja área queremos calcular.
def f(x):
  return math.sin(x)

# Define o tamanho de cada subintervalo
Delta_x = (b-a)/n

# Laço que percorre cada um dos subintervalos
for i in range (1,n+1):
  # Define xi
  # Calcula a Soma de Riemann
  xi = a + i*Delta_x
  integral = integral + f(xi)*Delta_x

# Imprime a aproximação para a integral definida de f em [a,b].
print()
print(f"A aproximmação da integral definida de f no intervalo [{a},{b}]")
print(f"considerando {n} subdivisões no intervalo é ")
print(integral)