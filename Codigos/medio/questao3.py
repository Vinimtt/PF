from functools import reduce

numeros_maior = [10, 45, 2, 88, 3]
maior_numero = reduce(lambda a, b: a if a > b else b, numeros_maior)