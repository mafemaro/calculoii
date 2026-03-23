""" CÓDIGOS DO PROFESSOR Roney Rachide Nunes!

O código abaixo realiza uma verificação simbólica, via SymPy, para determinar se duas funções F(x) e G(x) são primitivas de uma mesma função em algum intervalo real.

Inicialmente, define x como variável real e calcula os domínios de continuidade de F e G no conjunto dos reais, determinando sua interseção. Em seguida, utiliza o critério teórico segundo o qual duas funções são primitivas de uma mesma função se, e somente se, diferem por uma constante em um intervalo — isto é, se a derivada de F - G é identicamente nula nesse intervalo.

O programa então deriva simbolicamente a diferença, simplifica o resultado e verifica se essa derivada é zero e se o domínio comum não é vazio; caso ambas as condições sejam satisfeitas, conclui que F e G são primitivas da mesma função naquele intervalo real. """

import sympy as sp
from sympy.calculus.util import continuous_domain
from sympy import S

# Definir a variável simbólica
x = sp.symbols('x', real=True)

# F(x) é uma primitiva conhecida (sei que está correta!)
# G(x) é uma candidata à primitiva. Quero verificar se está correto.
F = sp.cos(x)**2
G = -sp.sin(x)**2

# A verificação será feito na interseção dos domínios de F e G.
# Domínios
dom_F = continuous_domain(F, x, S.Reals)
dom_G = continuous_domain(G, x, S.Reals)
intersecao = dom_F.intersect(dom_G)

# Queremos verificar se F - G é uma constante
diferenca = F - G

# F - G constante em um intervalo se, e só se, (F-G)' = 0 nesse intervalo
derivada = sp.diff(diferenca, x)

verificacao = sp.simplify(derivada)

if verificacao == 0 and not intersecao.is_empty:
    print()
    print(f"F e G são primitivas de uma mesma função no intervalo {intersecao}.")

else:
    print()
    print("F e G não são primitivas de uma mesma função em algum intervalo real.")