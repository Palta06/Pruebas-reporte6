import time
import random
import matplotlib.pyplot as plt

# -------------------------------
# Algoritmo principal (Mochila)
# -------------------------------
def max_happiness(m, x, costs, happiness):
    total_money = m * x
    dp = [0] * (total_money + 1)

    for i in range(m):
        c, h = costs[i], happiness[i]
        for money in range(total_money, c - 1, -1):
            dp[money] = max(dp[money], dp[money - c] + h)

    return max(dp)


# -------------------------------
# Casos de prueba
# -------------------------------
test_cases = [
    (1, 10, [1], [5], "Caso 1"),
    (2, 80, [0, 200], [10, 100], "Caso 2"),
    (3, 100, [70, 100, 150], [100, 200, 150], "Caso 3"),
    (5, 50, [0, 120, 60, 200, 90], [30, 100, 70, 150, 90], "Caso 4"),
]

print("Resultados de los casos de prueba:\n")
for m, x, costs, happiness, name in test_cases:
    result = max_happiness(m, x, costs, happiness)
    print(f"{name}:")
    print(f" m = {m}, x = {x}")
    print(f" costs = {costs}")
    print(f" happiness = {happiness}")
    print(f" -> Máxima felicidad = {result}\n")


# -------------------------------
# Análisis de tiempo de ejecución
# -------------------------------
sizes = list(range(5, 55, 5))  # m = 5, 10, ..., 50
times = []

for m in sizes:
    x = 100
    costs = [random.randint(1, 200) for _ in range(m)]
    happiness = [random.randint(1, 500) for _ in range(m)]

    start = time.time()
    max_happiness(m, x, costs, happiness)
    end = time.time()

    times.append(end - start)

# -------------------------------
# Gráfico
# -------------------------------
plt.plot(sizes, times, marker="o")
plt.title("Tiempo de ejecución vs. tamaño de la entrada (m)")
plt.xlabel("Número de meses (m)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.grid(True)
plt.show()
