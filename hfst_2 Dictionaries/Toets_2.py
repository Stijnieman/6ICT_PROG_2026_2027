""" Oefening 2 (  / 6)
Het kassasysteem van een bistro houdt de openstaande rekeningen per tafel bij.
In deze oefening ga je bestellingen toevoegen of tafels laten afrekenen.

Herhaal het volgende tot de gebruiker 'STOP' ingeeft bij de tafelnaam:
    - Vraag naar de tafelnaam (bv. 'Tafel 1').
    - Vraag welke actie de kelner wil uitvoeren: 'bestellen' of 'afrekenen'.

bestellen:
    - Vraag naar het bedrag van de nieuwe bestelling.
    - Als de tafel AL bestaat: tel het bedrag op bij de huidige rekening.
    - Als de tafel NOG NIET bestaat: voeg de tafel toe met dit bedrag.
    - Print de nieuwe totale rekening voor deze tafel.

afrekenen:        
    - Als de tafel AL bestaat: verwijder de tafel uit de dictionary met .pop()
      en print het totaal afgerekende bedrag.
    - Als de tafel NOG NIET bestaat: print een foutmelding dat er geen 
      openstaande rekening is voor deze tafel.

Print na het stoppen van de loop een overzicht van alle nog openstaande tafels.
"""
    

""" VOORBEELD:
-------------------------------------------------------------------------------
Voer tafelnaam in: Tafel 1
Welke actie ('bestellen' of 'afrekenen')? bestellen
Voer het bedrag in: 12.50
Nieuw totaal voor Tafel 1: €58.0

Voer tafelnaam in: Tafel 3
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Tafel 3 heeft €22.0 afgerekend en is nu vrij.

Voer tafelnaam in: Tafel 2
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Fout: Tafel 2 heeft geen openstaande rekening!

Voer tafelnaam in: STOP

Nog openstaande rekeningen:
{'Tafel 1': 58.0, 'Tafel 4': 87.1}
-------------------------------------------------------------------------------
"""


tafels = {
    'Tafel 1': 45.50,
    'Tafel 3': 22.00,
    'Tafel 4': 87.10
}
while True:
    tafel = input("Voer tafelnaam in: ")

    if tafel == "STOP":
        break

    keuze = input("Bestellen of afrekenen? ")

    if keuze == "Bestellen":
        bedrag = float(input("Voer het bedrag in: "))
        if tafel in tafels:
            tafels[tafel] += bedrag
        else:
            tafels[tafel] = bedrag
            print(f"Niew totaal voor {tafel}: {bedrag}")
    
    elif keuze == "afrekenen":
        if tafel in tafels:
            print(f"{tafel} heeft {tafels[tafel]}€ afgerekent en is nu vrij")
            tafels.pop(tafel)
        else:
            print(f"Fout: {tafel} heeft geen openstaande rekening")
print("Nog openstaande rekeningen:")
print(tafels)