# 📊 BinomCalc — Analisador Interativo da Distribuição Binomial

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Concluído-green)

---

# 🧠 Sobre o Projeto

O **BinomCalc** é um sistema interativo desenvolvido em Python com interface em Streamlit que tem como objetivo principal analisar e visualizar a **distribuição binomial** de forma intuitiva, dinâmica e educativa.

A distribuição binomial é um modelo probabilístico utilizado para representar experimentos que possuem apenas dois resultados possíveis em cada tentativa: sucesso ou falha.

O sistema permite que o usuário defina dois parâmetros fundamentais:

- **n** → número de tentativas  
- **p** → probabilidade de sucesso em cada tentativa  

A partir disso, o sistema calcula automaticamente toda a estrutura estatística da distribuição, incluindo:

- Probabilidade de cada resultado possível (k sucessos)
- Média (valor esperado)
- Moda (valor mais provável)
- Mediana (valor central aproximado)
- Variância (dispersão dos dados)

Além dos cálculos matemáticos, o projeto também inclui **simulação computacional via método de Monte Carlo**, que consiste em repetir o experimento diversas vezes para gerar uma aproximação empírica da distribuição teórica.

Dessa forma, o sistema permite uma comparação direta entre:

> 📌 o comportamento teórico (modelo matemático exato)  
> 📌 o comportamento simulado (experimentos repetidos no computador)

---
# 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```text
app_BinonCalc/
│
├── app.py
│   → Arquivo principal do sistema (interface em Streamlit)
│   → Responsável pela interação com o usuário, gráficos e exibição dos resultados

├── binomial_model.py
│   → Módulo matemático do projeto
│   → Contém os cálculos da distribuição binomial, média, variância, moda, mediana e simulação Monte Carlo

├── main.py
│   → Versão alternativa do sistema em terminal (opcional)
│   → Usado para testes rápidos sem interface gráfica

├── README.md
│   → Documentação completa do projeto
│   → Explicação do funcionamento, instalação e teoria utilizada
```
# ⚙️ Funcionalidades do Sistema

O BinomCalc permite:

- 📊 Cálculo automático de probabilidades binomiais  
- 📈 Visualização gráfica da distribuição teórica  
- 🎲 Simulação de Monte Carlo  
- 🧠 Interpretação automática dos resultados  
- 📌 Identificação da média, moda e mediana  
- 🔴 Classificação de eventos (raro, comum, etc.)

---

# 📊 Funcionamento do Sistema

O sistema é dividido em três etapas principais:

## 🎛️ 1. Entrada de dados
O usuário define:
- número de tentativas (n)
- probabilidade de sucesso (p)
- número de sucessos (k)

---

## 📐 2. Cálculo matemático
O sistema utiliza a fórmula da distribuição binomial:

\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\]

E calcula também:
- média (μ = n·p)
- variância (σ² = n·p·(1-p))
- moda
- mediana

---

## 🎲 3. Simulação Monte Carlo
O sistema simula o experimento várias vezes:

- executa n tentativas repetidas
- conta sucessos
- repete milhares de vezes
- gera distribuição empírica

---

# 📊 Explicação dos Gráficos

## 📊 Gráfico 1 — Distribuição Binomial (Teórica)

Este gráfico representa a probabilidade exata de cada valor de k.

📌 Características:
- formato de “montanha”
- pico na região da média
- extremos menos prováveis

📍 Interpretação:
Mostra o comportamento matemático ideal da distribuição binomial.

---

## 🎲 Gráfico 2 — Teórico vs Monte Carlo

Este gráfico compara:

- 🔵 Teórico → fórmula matemática exata  
- 🟠 Monte Carlo → simulação computacional  

📍 Interpretação:
Quanto maior o número de simulações, mais a distribuição simulada se aproxima da teórica, validando o modelo binomial.

---

# 🧪 Tecnologias Utilizadas

- Python   
- Streamlit  
- Matplotlib   
- Estatística   
- Simulação Monte Carlo 
- Chatgpt

---

# 🚀 Como Executar o Projeto

## 📌 1. Instalar dependências

```bash
python -m pip install streamlit matplotlib numpy


