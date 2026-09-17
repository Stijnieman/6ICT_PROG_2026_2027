# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
#niveau 1
# keuze_geb = input("geef me een sleutel: ")
# print(fruitmand[keuze_geb])

#niveau 2
keuze_geb = input("geef me een sleutel: ")
if keuze_geb in fruitmand:
    print(fruitmand[keuze_geb])
else:
    print("Deze sleutel bestaat niet")