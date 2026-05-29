from functools import reduce

numeros_soma = [1, 2, 3, 4, 5]
somatorio = reduce(lambda x, y: x + y, numeros_soma)