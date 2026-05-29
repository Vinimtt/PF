from functools import reduce

nomes = ["Ana", "Bruno", "Alice", "Beatriz", "Carlos", "Amanda",
         "Cláudio", "Débora", "Daniel", "Eduardo", "Elaine", "Fernanda"]

pares = list(map(lambda nome: (nome[0].upper(), nome), nomes))

agrupado = reduce(
    lambda acc, par: {**acc, par[0]: acc.get(par[0], []) + [par[1]]},
    pares,
    {}
)

print(agrupado)

tuplas = sorted(pares, key=lambda t: t[0])
print(tuplas)