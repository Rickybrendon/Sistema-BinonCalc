import streamlit as st
import matplotlib.pyplot as plt

from binomial_model import (
    binomial_pmf,
    esperanca,
    variancia,
    distribuicao_binomial,
    simulacao_monte_carlo,
    moda_binomial,
    mediana_binomial
)

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(page_title="BinomCalc", layout="centered")

st.title("📊 BinomCalc — Análise da Distribuição Binomial")
st.write("Sistema interativo para análise teórica e simulação de experimentos binomiais.")

st.divider()

# =========================
# ENTRADAS
# =========================
st.subheader("🎛️ Parâmetros do Experimento")

n = st.slider("Número de tentativas (n)", 1, 50, 10)
p = st.slider("Probabilidade de sucesso (p)", 0.0, 1.0, 0.5)
k = st.slider("Número de sucessos (k)", 0, n, 5)

st.divider()

# =========================
# CÁLCULOS
# =========================
prob = binomial_pmf(n, k, p)
media = esperanca(n, p)
var = variancia(n, p)

k_vals, probs = distribuicao_binomial(n, p)
sim_probs = simulacao_monte_carlo(n, p)

k_pico = moda_binomial(n, p)
mediana = mediana_binomial(n, p)

# =========================
# RESULTADOS
# =========================
st.subheader("📌 Resultados Estatísticos")

col1, col2, col3 = st.columns(3)

col1.metric("Média (μ)", f"{media:.2f}")
col2.metric("Moda", f"{k_pico}")
col3.metric("Mediana", f"{mediana}")

st.write(f"📊 **P(X = {k}) = {prob:.6f}**")
st.write(f"📉 **Variância (σ²) = {var:.2f}**")

# =========================
# CLASSIFICAÇÃO
# =========================
st.subheader("🧠 Classificação do Evento")

if prob < 0.05:
    st.error("🔴 Evento raro dentro do modelo binomial")
elif prob < 0.15:
    st.warning("🟡 Evento pouco comum dentro do modelo binomial")
else:
    st.success("🟢 Evento comum dentro do modelo binomial")

st.divider()

# =========================
# GRÁFICO TEÓRICO
# =========================
st.subheader("📊 Distribuição Binomial (Teórica)")

fig1, ax1 = plt.subplots()
ax1.bar(k_vals, probs, alpha=0.85)

ax1.axvline(media, color='red', linestyle='--', linewidth=2, label=f"Média (μ={media:.2f})")
ax1.axvline(k_pico, color='orange', linestyle='--', linewidth=2, label=f"Moda = {k_pico}")
ax1.axvline(k, color='green', linestyle='--', linewidth=2, label=f"k = {k}")

ax1.set_xlabel("Número de sucessos (k)")
ax1.set_ylabel("Probabilidade")
ax1.set_title("Distribuição Binomial Teórica")
ax1.legend()

st.pyplot(fig1)

# =========================
# INTERPRETAÇÃO GRÁFICO TEÓRICO
# =========================
st.subheader("🧠 Interpretação do Gráfico Teórico")

st.write("""
O gráfico teórico representa a distribuição binomial calculada pela fórmula matemática.

📌 A maior concentração de valores ocorre próximo à média (μ), pois há mais combinações possíveis nessa região.  
📌 Os extremos (muito poucos ou muitos sucessos) possuem menor probabilidade.  
📌 A moda indica o ponto de maior probabilidade (pico da distribuição).  
""")

if k < media:
    st.info("📉 O valor escolhido (k) está à esquerda da média, indicando um resultado abaixo do esperado.")
elif k > media:
    st.info("📈 O valor escolhido (k) está à direita da média, indicando um resultado acima do esperado.")
else:
    st.success("🎯 O valor escolhido (k) está no centro da distribuição (média).")

st.divider()

# =========================
# MONTE CARLO
# =========================
st.subheader("🎲 Teórico vs Simulação (Monte Carlo)")

fig2, ax2 = plt.subplots()

ax2.bar(k_vals, probs, alpha=0.6, label="Teórico")
ax2.bar(k_vals, sim_probs, alpha=0.6, label="Monte Carlo")

ax2.axvline(media, color='red', linestyle='--', linewidth=2, label="Média")

ax2.set_xlabel("Número de sucessos (k)")
ax2.set_ylabel("Probabilidade")
ax2.set_title("Comparação: Teoria vs Simulação")
ax2.legend()

st.pyplot(fig2)

# =========================
# INTERPRETAÇÃO MONTE CARLO
# =========================
st.subheader("🧠 Interpretação da Simulação (Monte Carlo)")

st.write("""
A simulação Monte Carlo representa a repetição do experimento binomial várias vezes.

📌 Cada execução simula n tentativas com probabilidade p.  
📌 A frequência dos resultados forma uma distribuição empírica.  
📌 Quanto maior o número de simulações, mais a distribuição simulada se aproxima da teórica.  
""")

st.divider()

# =========================
# RESUMO FINAL
# =========================
st.subheader("📄 Conclusão do Sistema")

st.write(f"""
Com os parâmetros definidos (n = {n}, p = {p}), o modelo binomial apresenta:

- Média esperada: {media:.2f}
- Moda (valor mais provável): {k_pico}
- Mediana aproximada: {mediana}
- Variância: {var:.2f}

O evento analisado (k = {k}) possui probabilidade de {prob:.4f},
sendo classificado como um evento dentro do modelo binomial.

A simulação Monte Carlo confirma a coerência entre teoria e prática,
validando o modelo estatístico da distribuição binomial.
""")
