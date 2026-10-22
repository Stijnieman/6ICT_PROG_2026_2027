# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
geb_mensen = int(input("Hoeveel mensen zijn er? : "))
print("Recept voor worst met wortelen en erwten.")
for sleutel, waarde in recept.items():
    waarde = int((waarde/4) *geb_mensen)
    print(f"-{sleutel}: {waarde}")