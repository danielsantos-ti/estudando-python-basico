# João e Maria gostam de filmes diferentes. João gosta de 'Inception', 'Interstellar' e 'The Dark Knight', enquanto Maria gosta de 'Inception', 'Titanic' e 'Avatar'. Usando conjuntos, encontre:
# 1. Quais filmes ambos gostam.
filmes_joao = {'Inception', 'Interstellar', 'The Dark Knight'}
filmes_maria = {'Inception', 'Titanic', 'Avatar'}

# Filmes que ambos gostam
filmes_comuns = filmes_joao.intersection(filmes_maria)

# Filmes que joão gosta, mas Maria não
filmes_joao_exclusivos = filmes_joao.difference(filmes_maria)

# Filmes que Maria gosta, mas João não
filmes_maria_exclusivos = filmes_maria.difference(filmes_joao)

# Imprime os resultados
print(filmes_comuns)
print(filmes_joao_exclusivos)
print(filmes_maria_exclusivos)