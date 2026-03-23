# 📘 Primitivas - Cálculo II  

---

## 📚 Introdução  

As **primitivas**, também chamadas de **integrais indefinidas**, são o processo de encontrar uma função original a partir de sua derivada.

Em outras palavras, se sabemos como uma função varia (sua derivada), queremos descobrir **qual função gerou essa variação**.

A integral indefinida é representada por:

\[
\int f(x)\,dx
\]

Ela nos fornece **todas as funções cuja derivada é f(x)**.

---

## 🔁 Relação entre Derivada e Integral  

A **integral é o processo inverso da derivada**.

- Derivar → encontrar a taxa de variação  
- Integrar → reconstruir a função original  

### 💡 Ideia principal:

Se:

\[
f'(x) = g(x)
\]

Então:

\[
\int g(x)\,dx = f(x) + C
\]

---

### 📌 Exemplos

- Se:
  \[
  \frac{d}{dx}(x^2) = 2x
  \]

  Então:
  \[
  \int 2x\,dx = x^2 + C
  \]

---

- Se:
  \[
  \frac{d}{dx}(\sin x) = \cos x
  \]

  Então:
  \[
  \int \cos x\,dx = \sin x + C
  \]

---

👉 Ou seja: **integrar é "voltar" a função antes da derivada**.

---

## 🧠 Definição de Primitiva  

Uma função \( F(x) \) é chamada de **primitiva** de \( f(x) \) se:

\[
F'(x) = f(x)
\]

A integral indefinida é escrita como:

\[
\int f(x)\,dx = F(x) + C
\]

---

### 🔹 Constante de integração (+C)

Sempre adicionamos uma constante \( C \) porque:

- A derivada de uma constante é zero  
- Diferentes funções podem ter a mesma derivada  

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

## 📊 Exemplos Simples  

### 🔹 Exemplo 1

\[
\int x\,dx
\]

Sabemos que:

\[
\frac{d}{dx}\left(\frac{x^2}{2}\right) = x
\]

Então:

\[
\int x\,dx = \frac{x^2}{2} + C
\]

✔ Verificação:

\[
\frac{d}{dx}\left(\frac{x^2}{2}\right) = x
\]

---

### 🔹 Exemplo 2

\[
\int x^2\,dx
\]

Sabemos que:

\[
\frac{d}{dx}\left(\frac{x^3}{3}\right) = x^2
\]

Então:

\[
\int x^2\,dx = \frac{x^3}{3} + C
\]

✔ Verificação:

\[
\frac{d}{dx}\left(\frac{x^3}{3}\right) = x^2
\]

---

### 🔹 Exemplo 3

\[
\int \cos(x)\,dx
\]

Sabemos que:

\[
\frac{d}{dx}(\sin x) = \cos x
\]

Então:

\[
\int \cos(x)\,dx = \sin(x) + C
\]

✔ Verificação:

\[
\frac{d}{dx}(\sin x) = \cos x
\]

---

## ⚠️ Observações Importantes  

- ✅ Sempre adicionar **+C** na integral indefinida  
- ✅ Integração depende diretamente das **derivadas conhecidas**  
- ✅ A integral não é única (por causa da constante)  
- ⚠️ Esquecer o **+C** é um erro muito comum em provas  

---

## 🏁 Conclusão  

A ideia central é:

👉 **Integrar é desfazer uma derivada**

- Derivada → reduz a função  
- Integral → reconstrói a função  

Se você domina derivadas, então já tem a base para resolver integrais.

👉 Pense sempre assim:  
**"Qual função, quando derivada, gera isso aqui?"**