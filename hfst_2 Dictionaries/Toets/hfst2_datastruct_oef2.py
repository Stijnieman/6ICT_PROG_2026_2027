""" Oefening 2 (   / 3)
Onderstaande structuur geeft per persoon het aantal gemaakte doelpunt over 5 wedstrijden.
Print wie gemiddeld de meeste doelpunten heeft gemaakt, en hoeveel er dit waren.
Print wie gemiddeld de minste doelpunten heeft gemaakt, en hoeveel er dit waren.
De code moet blijven werken, ook als er later meer personen bijkomen.

Voor de start-datastructuur is dit het correcte antwoord.
    Meest: Sarah (2.6 doelpunten per match)
    Minst: Kiana (1.2 doelpunten per match)

"""

sport_uitslagen = {
    'Emma': [2, 3, 1, 4, 2],  # Aantal doelpunten per wedstrijd
    'Liam': [1, 2, 1, 3, 0],
    'Noah': [0, 1, 2, 1, 3],
    'Sarah': [3, 3, 4, 2, 1],
    'Kiana': [1, 0, 2, 1, 2],
    'Lucas': [2, 1, 3, 1, 0],
    'Stijn': [0, 0, 0, 1, 0]
}
naam_hoogste = ""
naam_laagste = ""
totaal = 0
hoogste = 0
laagste = 1000
for sleutel,score in sport_uitslagen.items():
    for getal in score:
        totaal += getal
        print(totaal)
    totaal = totaal/5
    if totaal > hoogste:
        hoogste = totaal
        naam_hoogste = sport_uitslagen[sleutel]
    elif totaal < laagste:
        laagste = totaal
        naam_hoogste = sport_uitslagen[sleutel]
    totaal = 0
# print(f"{naam_hoogste} heeft het hoogste gem: {hoogste}")
# print(f"{naam_laagste} heeft het laagste gem: {laagste}")