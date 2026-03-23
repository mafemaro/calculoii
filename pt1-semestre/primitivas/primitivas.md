# 📘 Primitivas - Cálculo II

---

## 📚 Introdução

As **primitivas** são funções que representam o processo inverso da derivada.

Dada uma função $f(x)$, queremos encontrar uma função $F(x)$ tal que:

$F'(x) = f(x)$

Ou seja, buscamos uma função cuja derivada é a função dada.

As primitivas estão diretamente relacionadas às integrais indefinidas:

$\int f(x)\,dx = F(x) + C$

---

## 🔁 Relação entre Derivada e Primitiva

A ideia central é:

👉 Derivada e primitiva são operações inversas.

- Derivar → “desmonta” a função  
- Integrar → “reconstrói” a função  

### 💡 Relação formal

Se:

$F'(x) = f(x)$

Então:

$\int f(x)\,dx = F(x) + C$

---

### 📌 Exemplos

#### Exemplo 1

$\frac{d}{dx}(x^2) = 2x$

Logo:

$\int 2x\,dx = x^2 + C$

---

#### Exemplo 2

$\frac{d}{dx}(\sin x) = \cos x$

Logo:

$\int \cos x\,dx = \sin x + C$

---

👉 Primitiva é simplesmente **encontrar a função original**.

---

## 🧠 Definição de Primitiva

Uma função $F(x)$ é chamada de **primitiva** de $f(x)$ se:

$F'(x) = f(x)$

---

### 🔹 Família de Primitivas

Uma função não possui apenas uma primitiva, mas várias:

$F(x) + C$

Isso ocorre porque:

- A derivada de qualquer constante é zero  
- Logo, várias funções diferentes possuem a mesma derivada  

Exemplo:

$F(x) = x^2 + 1$  
$F(x) = x^2 + 5$

Ambas têm derivada:

$2x$

---

## 📊 Tabela de Primitivas Básicas

| Função $f(x)$ | Primitiva $F(x)$ |
|--------------|-----------------|
| $x^n$, $n \neq -1$ | $\frac{x^{n+1}}{n+1}$ |
| $\frac{1}{x}$ | $\ln|x|$ |
| $e^x$ | $e^x$ |
| $a^x$ | $\frac{a^x}{\ln a}$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\sec^2 x$ | $\tan x$ |
| $\frac{1}{1+x^2}$ | $\arctan x$ |

---

## ⚙️ Propriedades das Primitivas

### 🔹 Linearidade

$\int (f(x) + g(x))\,dx = \int f(x)\,dx + \int g(x)\,dx$

---

### 🔹 Constante multiplicativa

$\int c \cdot f(x)\,dx = c \cdot \int f(x)\,dx$

---

### 🔹 Soma e subtração

$\int (f(x) - g(x))\,dx = \int f(x)\,dx - \int g(x)\,dx$

---

## 🧮 Exemplos Resolvidos

---

### 🔹 Exemplo 1

$\int 4x^3\,dx$

$= x^4 + C$

✔ Verificação:

$\frac{d}{dx}(x^4) = 4x^3$

---

### 🔹 Exemplo 2

$\int (2x + 6)\,dx$

$= x^2 + 6x + C$

✔ Verificação:

$\frac{d}{dx}(x^2 + 6x) = 2x + 6$

---

### 🔹 Exemplo 3

$\int e^x\,dx$

$= e^x + C$

✔ Verificação:

$\frac{d}{dx}(e^x) = e^x$

---

### 🔹 Exemplo 4

$\int \cos x\,dx$

$= \sin x + C$

✔ Verificação:

$\frac{d}{dx}(\sin x) = \cos x$

---

### 🔹 Exemplo 5

$\int (3\sin x - 2\cos x)\,dx$

$= -3\cos x - 2\sin x + C$

---

## ⚠️ Erros Comuns

- ❌ Esquecer o $+C$  
- ❌ Confundir derivada com primitiva  
- ❌ Erros de sinal (principalmente em trigonometria)  
- ❌ Aplicar regra de potência incorretamente  
- ❌ Não verificar o resultado derivando  

---

## 🎯 Dicas para Prova

- 🔍 Sempre pense: *“qual função gera isso ao derivar?”*  
- 📌 Use a tabela como base  
- ⚡ Simplifique antes de integrar  
- 🧠 Confira sempre derivando o resultado  
- 📚 Memorize as primitivas mais importantes  

---

## 🏁 Conclusão

As **primitivas** são fundamentais para entender integrais.

👉 Ideia central:

- Derivada → transforma a função  
- Primitiva → reconstrói a função  

Dominar primitivas é essencial para resolver integrais com segurança.

📌 Sempre questione:

👉 *“Qual função tem essa derivada?”*