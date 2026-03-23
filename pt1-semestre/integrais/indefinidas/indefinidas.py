""" CÓDIGOS DO PROFESSOR Roney Rachide Nunes!

O código abaixo utiliza o SymPy para verificar simbolicamente se uma função F(x) é primitiva de uma função dada f(x).

Após definir a variável simbólica x, o programa calcula a derivada F'(x) e determina os domínios de continuidade de f e de F' no conjunto dos reais, obtendo a interseção desses domínios.

Em seguida, aplica o critério fundamental de verificação: F é primitiva de f em um intervalo se, e somente se, F'(x) = f(x) nesse intervalo. Para isso, simplifica simbolicamente a expressão F'(x) - f(x) e testa se o resultado é identicamente zero e se o domínio comum não é vazio.

Se ambas as condições forem satisfeitas, conclui que F(x) + c representa a família de todas as primitivas de f naquele intervalo; caso contrário, afirma que F não é primitiva de f. """

import sympy as sp
from sympy.calculus.util import continuous_domain
from sympy import S

# Definir a variável simbólica
x = sp.symbols('x')

# Definição das funções
# Verificaremos se F(x) é uma primitiva de f(x).

f = 2*sp.cos(x)*sp.sin(x)+ 2
F = sp.sin(x)**2

# Derivar F
F_derivada = sp.diff(F, x)

# A verificação será feito na interseção dos domínios de f e F'.
# Domínios
dom_f = continuous_domain(f, x, S.Reals)
dom_F_derivada = continuous_domain(F_derivada, x, S.Reals)
intersecao = dom_f.intersect(dom_F_derivada)

# Verificar se F' - f é zero.
# Necessário simplificar a expressão.

verificacao = sp.simplify(F_derivada - f)

if verificacao == 0 and not intersecao.is_empty:
    print()
    print(f"F' = f no intervalo {intersecao}.")
    print()
    print(f"F(x) + c representa todas as primitivas de f no intervalo {intersecao}.")
else:
    print()
    print("F não é uma primitiva de f.")