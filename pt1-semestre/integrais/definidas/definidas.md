# 📘 Integrais Definidas - Cálculo II

---

## 📚 Introdução

As **integrais definidas** são usadas para calcular o valor acumulado de uma função em um intervalo.

A notação é:

$\int_a^b f(x)\,dx$

onde:

- $a$ → limite inferior  
- $b$ → limite superior  
- $f(x)$ → função  

---

### 🔹 Diferença: Definida vs Indefinida

| Tipo | Resultado |
|------|----------|
| Integral indefinida | Função + constante ($F(x) + C$) |
| Integral definida | Número real |

---

### 💡 Ideia principal

A integral definida representa a **área acumulada sob a curva** no intervalo $[a, b]$.

---

## 📐 Interpretação Geométrica

A integral definida pode ser interpretada como a **área entre a curva e o eixo x**.

---

### 🔹 Casos importantes

#### 📌 Quando $f(x) \ge 0$

A área é **positiva**:

👉 Região entre a curva e o eixo x acima do eixo

---

#### 📌 Quando $f(x) \le 0$

A área é **negativa**:

👉 Região abaixo do eixo x

---

### 📌 Interpretação visual (conceitual)

Imagine:

- Um gráfico de uma função
- Dividimos o intervalo em pequenas partes
- Calculamos retângulos de altura $f(x)$
- Somamos todas essas áreas

👉 Quanto menores os retângulos, mais precisa é a aproximação

---

## 🧠 Definição Formal

A integral definida é dada por:

$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i)\,\Delta x$

---

### 🔹 Soma de Riemann

A ideia é:

1. Dividir o intervalo $[a, b]$ em $n$ partes  
2. Aproximar a área com retângulos  
3. Somar as áreas  
4. Fazer o limite quando $n \to \infty$  

---

### 🔹 Intuição

- Mais retângulos → melhor aproximação  
- No limite → área exata  

---

## 🔁 Teorema Fundamental do Cálculo

Esse é o resultado mais importante do cálculo.

---

### 💡 Enunciado

Se $F(x)$ é uma primitiva de $f(x)$, então:

$\int_a^b f(x)\,dx = F(b) - F(a)$

---

### 🔹 Interpretação

A integral definida pode ser calculada usando uma primitiva:

👉 Encontramos $F(x)$  
👉 Substituímos os limites  

---

### 📌 Por que funciona?

Porque:

- A derivada “desfaz” a primitiva  
- A integral “acumula” a variação  

---

## ⚙️ Propriedades das Integrais Definidas

---

### 🔹 Linearidade

$\int_a^b (f(x) + g(x))\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$

---

### 🔹 Constante multiplicativa

$\int_a^b c \cdot f(x)\,dx = c \cdot \int_a^b f(x)\,dx$

---

### 🔹 Troca de limites

$\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$

---

### 🔹 Intervalo nulo

$\int_a^a f(x)\,dx = 0$

---

### 🔹 Soma de intervalos

$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$

---

## 🧮 Exemplos Resolvidos

---

### 🔹 Exemplo 1 (básico)

$\int_0^2 x\,dx$

**Passo 1: encontrar primitiva**

$F(x) = \frac{x^2}{2}$

**Passo 2: aplicar limites**

$F(2) - F(0)$

$= \frac{2^2}{2} - 0$

$= 2$

---

### 🔹 Exemplo 2

$\int_1^3 x^2\,dx$

**Primitiva:**

$F(x) = \frac{x^3}{3}$

**Aplicando limites:**

$F(3) - F(1)$

$= \frac{27}{3} - \frac{1}{3}$

$= \frac{26}{3}$

---

### 🔹 Exemplo 3

$\int_0^{\pi} \sin x\,dx$

**Primitiva:**

$F(x) = -\cos x$

**Aplicando:**

$F(\pi) - F(0)$

$= (-\cos \pi) - (-\cos 0)$

$= (1) - (-1)$

$= 2$

---

### 🔹 Exemplo 4 (com função constante)

$\int_0^5 3\,dx$

**Primitiva:**

$F(x) = 3x$

**Aplicando:**

$F(5) - F(0)$

$= 15 - 0 = 15$

---

### 🔹 Exemplo 5 (interpretação de área)

$\int_0^2 (x - 2)\,dx$

**Primitiva:**

$F(x) = \frac{x^2}{2} - 2x$

**Aplicando:**

$F(2) - F(0)$

$= (2 - 4) - 0$

$= -2$

👉 Resultado negativo indica área abaixo do eixo x

---

## ⚠️ Erros Comuns

- ❌ Esquecer de aplicar os limites  
- ❌ Não calcular corretamente a primitiva  
- ❌ Erros de sinal (principalmente em funções trigonométricas)  
- ❌ Confundir integral definida com indefinida  
- ❌ Não substituir corretamente $a$ e $b$  

---

## 🎯 Dicas para Prova

- 🔍 Primeiro encontre a primitiva  
- ⚡ Sempre aplique: $F(b) - F(a)$  
- 📌 Organize bem as contas para evitar erros  
- 🧠 Cuidado com sinais negativos  
- 📚 Decore as primitivas básicas  

---

## 🏁 Conclusão

As integrais definidas representam o **acúmulo de uma função em um intervalo**.

👉 Ideia central:

- Derivada → taxa de variação  
- Integral definida → acumulação (área)

E o mais importante:

👉 Toda integral definida pode ser resolvida usando o Teorema Fundamental do Cálculo.

📌 Sempre pense:

👉 *"Qual primitiva e como aplicar os limites?"*