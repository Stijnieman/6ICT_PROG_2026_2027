""" OEFENING 3 (  / 5)
Onderstaande datastructuur bevat als elementen de vragen/antwoorden van een quiz-spel.
Hiernaast bevat het ook hoeveel geld iedere vraag waard is.
Sommige vragen hebben ook een hint. Die hint mag enkel getoond worden als ze aanwezig is.

Stel iedere vraag aan de deelnemer (via de functie input).
Toon eerst de hint als deze bestaat (ZIE VOORBEELD).

Controleer het antwoord en print of de deelnemer het juist/fout had.
 - Heeft de deelnemer het juist? Voeg het gewonnen geld dan toe aan een prijzenpot.
 - Heeft de deelnemer het fout? Print dan ook wat het juiste antwoord was.
Na het overlopen van alle elementen print je hoeveel geld de deelnemer gewonnen heeft.

De code moet blijven werken, ook als er later vragen bijkomen of weggaan.
"""

""" VOORBEELD:
Hint: Tussen 3 en 5
Wat is 2+2? 4
Correct! Je verdient €200.

Hint: denk aan 'for' en 'while'
Hoe kan je code meermaals herhalen? if
Fout! Het juiste antwoord is loops

Welk datatype stelt een kommagetal voor? float
Correct! Je verdient €400.

De quiz is afgelopen. Je hebt €600 gewonnen!
"""

quiz = [
    {"vraag":"Wat is 2+2?", "antwoord":"4", "geld":200, "hint":"Tussen 3 en 5"},
    {"vraag":"Hoe kan je code meermaals herhalen?", "antwoord":"loops", "geld":300, "hint":"Denk aan 'for' en 'while'"},
    {"vraag":"Welk datatype stelt een kommagetal voor?", "antwoord":"float", "geld":400},
    {"vraag":"Hoe noemt Stijn zijn oudste nichtje?", "antwoord": "piske floor", "geld": 10000000000000},
]
index = 0
totaal_geld = 0
for vraag in quiz:
    if "hint" in vraag:
        print(f"Hint: {vraag["hint"]}")
    geb = input(f"{quiz[index]["vraag"]} ")
    if geb == vraag["antwoord"]:
        print(f"Correct! Je verdient {vraag["geld"]}€.")
        totaal_geld += vraag["geld"]
    else:
        print(f"Fout! Het atwoord was {vraag["antwoord"]} ")
    index += 1
print(f"De quiz is afgelopen. Je hebt {totaal_geld}€ gewonnen!")