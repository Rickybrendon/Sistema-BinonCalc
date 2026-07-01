import math
import random

# =========================
# BINOMIAL (PMF)
# =========================
def binomial_pmf(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


# =========================
# MÉDIA
# =========================
def esperanca(n, p):
    return n * p


# =========================
# VARIÂNCIA
# =========================
def variancia(n, p):
    return n * p * (1 - p)


# =========================
# DISTRIBUIÇÃO COMPLETA
# =========================
def distribuicao_binomial(n, p):
    k_vals = list(range(n + 1))
    probs = [binomial_pmf(n, k, p) for k in k_vals]
    return k_vals, probs


# =========================
# MODA (valor mais provável)
# =========================
def moda_binomial(n, p):
    k_mode = math.floor((n + 1) * p)
    return k_mode


# =========================
# MEDIANA (aproximação)
# =========================
def mediana_binomial(n, p):
    return round(n * p)


# =========================
# MONTE CARLO
# =========================
def simulacao_monte_carlo(n, p, simulacoes=10000):
    resultados = [0] * (n + 1)

    for _ in range(simulacoes):
        sucessos = sum(1 for _ in range(n) if random.random() < p)
        resultados[sucessos] += 1

    return [r / simulacoes for r in resultados]
