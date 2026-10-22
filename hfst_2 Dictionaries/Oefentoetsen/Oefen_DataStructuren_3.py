# """ OEFENING 3 (  / 5)
# Onderstaande datastructuur is een vereenvoudigde weergave van het asset-management binnen de school.

# De sleutel van de hoofd-dictionary is het SPB-nummer van de asset.
# De waarde is een sub-dictionary met erin volgende informatie:
#     - serial         (verplicht, altijd ingevuld)
#     - categorie      (optioneel, kan None zijn als de asset niet in een categorie geplaatst is)
#     - toegewezen_aan (optioneel, komt niet voor als de asset niet toegewezen is)

# Maak een overzicht van alle assets die toegewezen zijn aan een bepaalde gebruiker (naam_gebruiker). 
# Voor elk toegewezen asset moet je volgende informatie printen:
#     - SPB-nummer
#     - Serial
#     - Categorie (alleen als deze niet None is)
# Print tenslotte het totaal aantal assets dat aan deze gebruiker is toegewezen.

# De code moet correct blijven werken als er in de toekomst meer assets worden toegevoegd of gewijzigd.
# """

# """ VOORBEELD (naam_gebruiker = jan.janssen)
# Overzicht van assets toegewezen aan jan.janssen...
#     - spb2021-098817 met serial 5CD133BZBC en categorie Huur100
#     - spb2021-100101 met serial 5CD133FEED
# Totaal aantal toegewezen assets: 2
# """

assets = {
    "spb2021-098817": {
        "serial": "5CD133BZBC",
        "categorie": "Huur100",
        "toegewezen_aan": "jan.janssen"
    },
    "spb2023-092814": {
        "serial": "5CD235BZBC",
        "categorie": "Overgekocht",
        "toegewezen_aan": "piet.pieters"
    },
    "spb2022-043299": {
        "serial": "5CD183BADC",
        "categorie": "Huur100",
    },
    "spb2021-100101": {
        "serial": "5CD133FEED",
        "categorie": None,
        "toegewezen_aan": "jan.janssen"
    },
}

naam_gebruiker = "jan.janssen"
aantal_assets = 0
for subdictionary,info in assets.items():
    if "toegewezen_aan" in info:
        if info["toegewezen_aan"] == naam_gebruiker:
            aantal_assets += 1
            if info["categorie"] != None:
                print(f"{subdictionary} met serial {info["serial"]} en categorie {info["categorie"]}")
            else:
                print(f"{subdictionary} met serial {info["serial"]}")
print(f"Totaal aantal assets: {aantal_assets}")
