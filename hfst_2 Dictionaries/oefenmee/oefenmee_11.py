# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 8,
    "Werk":  8,
    "Ontspanning": 8
}
tot_uur = 0
max_uur = 0
print("Planning van morgen")
for sleutel, waarde in planner.items():
    tot_uur += waarde
    print(f"-{sleutel}: {waarde} u.")
max_uur = 24 - tot_uur
print(f"U heeft {max_uur} u over")

