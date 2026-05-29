import csv

emprestimos = []
with open("emprestimos.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        emprestimos.append({
            "id": int(row["id"]),
            "valor": float(row["valor"]),
            "quantidade": int(row["quantidade"])
        })

acima_1000 = list(filter(lambda e: e["valor"] > 1000, emprestimos))

com_juros = list(map(lambda e: {
    "id": e["id"],
    "valor_original": e["valor"],
    "juros_10pct": round(e["valor"] * 0.10, 2),
    "valor_total": round(e["valor"] * 1.10, 2)
}, acima_1000))

for e in com_juros:
    print(e)