""" OEFENING 2 (  / 2)
Onderstaande structuur bevat score/level behaald in het spel brickbreaker voor meerdere personen.

Print de naam van de speler met de hoogste score. Op het moment is dit Jan.
De code moet correct blijven werken, ook als er in de toekomst iemand anders een hogere score haalt.
Je kan dit zelf testen door de scores in de datastructuur aan te passen.
"""

brickbreaker = [
    {"speler": "Eva", "score": 1500, "level": 5},
    {"speler": "Jan", "score": 2300, "level": 7},
    {"speler": "Lotte", "score": 1800, "level": 6},
    {"speler": "Pieter", "score": 900, "level": 3},
    {"speler": "Sofie", "score": 2000, "level": 7},
]
hoogste_score = 0
naam = ""
for index, dictionary in enumerate(brickbreaker):
    if dictionary["score"] > hoogste_score:
        hoogste_score = dictionary["score"]
        naam = dictionary["speler"]
print(f"{naam} heeft de hoogste score :{hoogste_score}")