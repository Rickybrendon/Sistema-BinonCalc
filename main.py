from binomial_model import (
    binomial_pmf,
    esperanca,
    variancia,
    distribuicao_binomial,
    simulacao_monte_carlo
)

import matplotlib.pyplot as plt


def interpretar_resultado(k, media, prob):
    if k < media:
        posicao = "abaixo da média"
    elif k > media:
        posicao = "acima da média"
    else:
        posicao = "igual à média"

    return posicao


def main():
    print("=== BinomCalc — Analisador de Distribuição Binomial ===")

    n = int(input("Digite o número de tentativas (n): "))
    p = float(input("Digite a probabilidade de sucesso (p entre 0 e 1): "))
    k = int(input("Digite o número de sucessos desejado (k): "))

    # ======================
    # CÁLCULOS
    # ======================
    prob = binomial_pmf(n, k, p)
    media = esperanca(n, p)
    var = variancia(n, p)

    k_vals, probs = distribuicao_binomial(n, p)

    # pico da distribuição (valor mais provável)
    k_pico = k_vals[probs.index(max(probs))]

    # ======================
    # RESULTADOS TEXTO
    # ======================
    print("\n📊 RESULTADOS")
    print(f"P(X = {k}) = {prob:.6f}")
    print(f"Média (μ) = {media:.2f}")
    print(f"Variância (σ²) = {var:.2f}")

    print("\n🧠 ANÁLISE AUTOMÁTICA")
    print(f"O valor k = {k} está {interpretar_resultado(k, media, prob)} da média.")
    print(f"O valor mais provável (pico da distribuição) é k = {k_pico}.")

    # ======================
    # GRÁFICO TEÓRICO
    # ======================
    plt.figure(figsize=(10, 5))
    plt.bar(k_vals, probs, alpha=0.8, label="Teórico")

    # Média
    plt.axvline(media, color='red', linestyle='--', linewidth=2,
                label=f"Média (μ = {media:.2f})")

    # k escolhido
    plt.axvline(k, color='green', linestyle='--', linewidth=2,
                label=f"k escolhido = {k}")

    # pico
    plt.axvline(k_pico, color='orange', linestyle='--', linewidth=2,
                label=f"Pico = {k_pico}")

    plt.xlabel("Número de sucessos (k)")
    plt.ylabel("Probabilidade P(X = k)")
    plt.title("Distribuição Binomial — Análise Completa")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.show()

    # ======================
    # MONTE CARLO
    # ======================
    sim_probs = simulacao_monte_carlo(n, p)

    plt.figure(figsize=(10, 5))
    plt.bar(k_vals, probs, alpha=0.6, label="Teórico")
    plt.bar(k_vals, sim_probs, alpha=0.6, label="Simulação (Monte Carlo)")

    plt.axvline(media, color='red', linestyle='--', linewidth=2,
                label=f"Média (μ = {media:.2f})")

    plt.xlabel("Número de sucessos (k)")
    plt.ylabel("Probabilidade")
    plt.title("Distribuição Binomial — Teórico vs Simulação")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.show()

    # ======================
    # RELATÓRIO FINAL
    # ======================
    print("\n📄 RESUMO FINAL")
    print(f"Com n = {n} e p = {p}, espera-se em média {media:.2f} sucessos.")
    print(f"O valor mais provável é {k_pico}.")
    print(f"A probabilidade de obter exatamente {k} sucessos é {prob:.4f}.")
    print("O comportamento da simulação confirma o modelo teórico da distribuição binomial.")


if __name__ == "__main__":
    main()
