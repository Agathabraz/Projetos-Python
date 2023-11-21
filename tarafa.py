def knapsack_problem(items, capacity):
    # Cria uma matriz para armazenar os valores máximos alcançados para cada subproblema
    num_items = len(items)
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]
  
    for i in range(1, num_items + 1):
        weight, value = items[i - 1]
        for j in range(1, capacity + 1):
            if weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    
    # Reconstrói a solução a partir da matriz dp
    solution = []
    w = capacity
    for i in range(num_items, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            weight, value = items[i - 1]
            solution.append((weight, value))
            w -= weight
  
    return dp[num_items][capacity], solution

# Exemplo de utilização
items = [(2, 10), (3, 15), (5, 20), (7, 25)]  # (peso, valor)
capacity = 10

max_value, selected_items = knapsack_problem(items, capacity)

print("Valor máximo:", max_value)
print("Itens selecionados:")
for item in selected_items:
    print("Peso:", item[0], "Valor:", item[1])
