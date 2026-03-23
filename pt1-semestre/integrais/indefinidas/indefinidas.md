# 📘 Integrais Indefinidas

---

## 📚 Introdução

As **integrais indefinidas** representam o processo de encontrar uma função a partir de sua taxa de variação.

Dada uma função \( f(x) \), buscamos uma função \( F(x) \) tal que:

\[
F'(x) = f(x)
\]

A integral indefinida é representada por:

\[
\int f(x)\,dx
\]

O resultado não é uma única função, mas uma família de funções.

---

## 🔁 Relação com Derivadas

A integral é o **processo inverso da derivada**.

- Derivada → calcula a taxa de variação  
- Integral → reconstrói a função original  

### 💡 Ideia fundamental

Se:

\[
\frac{d}{dx}F(x) = f(x)
\]

Então:

\[
\int f(x)\,dx = F(x) + C
\]

---

### 📌 Exemplos

#### Exemplo 1

\[
\frac{d}{dx}(x^2) = 2x
\]

Logo:

\[
\int 2x\,dx = x^2 + C
\]

---

#### Exemplo 2

\[
\frac{d}{dx}(\cos x) = -\sin x
\]

Logo:

\[
\int -\sin x\,dx = \cos x + C
\]

---

## 🧠 Definição Formal

Uma função \( F(x) \) é uma primitiva de \( f(x) \) se:

\[
F'(x) = f(x)
\]

A integral indefinida é definida como:

\[
\int f(x)\,dx = F(x) + C
\]

---

### 🔹 Notação

- \( \int \) → símbolo de integral  
- \( f(x) \) → função a ser integrada  
- \( dx \) → variável de integração  

---

### 🔹 Constante de Integração (+C)

A constante \( C \) existe porque:

- A derivada de uma constante é zero  
- Várias funções podem ter a mesma derivada  

Exemplo:

\[
\frac{d}{dx}(x^2 + 1) = 2x
\]
\[
\frac{d}{dx}(x^2 + 5) = 2x
\]

Logo:

\[
\int 2x\,dx = x^2 + C
\]

---

## 📊 Tabela de Integrais Básicas

| Função \( f(x) \) | Integral \( \int f(x)\,dx \) |
|------------------|------------------------------|
| \( x^n \), \( n \neq -1 \) | \( \frac{x^{n+1}}{n+1} + C \) |
| \( \frac{1}{x} \) | \( \ln|x| + C \) |
| \( e^x \) | \( e^x + C \) |
| \( a^x \) | \( \frac{a^x}{\ln a} + C \) |
| \( \sin x \) | \( -\cos x + C \) |
| \( \cos x \) | \( \sin x + C \) |
| \( \sec^2 x \) | \( \tan x + C \) |
| \( \frac{1}{1+x^2} \) | \( \arctan x + C \) |

---

## ⚙️ Propriedades das Integrais

### 🔹 Linearidade

\[
\int (f(x) + g(x))\,dx = \int f(x)\,dx + \int g(x)\,dx
\]

---

### 🔹 Constante multiplicativa

\[
\int c \cdot f(x)\,dx = c \cdot \int f(x)\,dx
\]

---

### 🔹 Soma e subtração

\[
\int (f(x) - g(x))\,dx = \int f(x)\,dx - \int g(x)\,dx
\]

---

## 🧮 Exemplos Resolvidos

---

### 🔹 Exemplo 1

\[
\int 3x^2\,dx
\]

\[
= x^3 + C
\]

---

### 🔹 Exemplo 2

\[
\int (5x + 2)\,dx
\]

\[
= \int 5x\,dx + \int 2\,dx
\]

\[
= \frac{5x^2}{2} + 2x + C
\]

---

### 🔹 Exemplo 3

\[
\int e^x\,dx
\]

\[
= e^x + C
\]

---

### 🔹 Exemplo 4

\[
\int \frac{1}{x}\,dx
\]

\[
= \ln|x| + C
\]

---

### 🔹 Exemplo 5

\[
\int (2\sin x - 4\cos x)\,dx
\]

\[
= -2\cos x - 4\sin x + C
\]

---

## ⚠️ Erros Comuns

- ❌ Esquecer o \( +C \)  
- ❌ Aplicar regras de potência de forma incorreta  
- ❌ Erro em sinais (principalmente com seno e cosseno)  
- ❌ Integrar termo a termo de forma errada  
- ❌ Confundir derivada com integral  

---

## 🎯 Dicas para Prova

- 🔍 Sempre verifique se pode usar tabela diretamente  
- ⚡ Simplifique a expressão antes de integrar  
- 📌 Integrais de soma → separam termo a termo  
- 🧠 Confirme o resultado derivando  
- 📚 Decore bem a tabela básica  

---

## 🏁 Conclusão

As integrais indefinidas são fundamentais para reconstruir funções a partir de suas derivadas.

👉 Ideia central:

- Derivada → mostra como a função muda  
- Integral → recupera a função  

Dominar integrais é essencial para todo o Cálculo II e aplicações futuras.

📌 Sempre pergunte:

👉 *“Qual função tem essa derivada?”*