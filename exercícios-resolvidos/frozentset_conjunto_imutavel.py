cores = frozenset(['vermelho', 'verde', 'azul'])
cores.add('amarelo')  # Isso causará um erro, pois frozenset é imutável
print(cores)
