from functools import reduce

numeros_mistos = [2, 4, 6, 8, 10]
filtrados_e_dobrados = list(map(lambda x: x * 2, filter(lambda x: x > 5, numeros_mistos)))