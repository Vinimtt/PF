from functools import reduce

numeros_produto = [2, 3, 4]
produto = reduce(lambda x, y: x * y, numeros_produto)