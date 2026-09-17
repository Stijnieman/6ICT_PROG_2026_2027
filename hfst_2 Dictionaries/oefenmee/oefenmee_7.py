# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
naam = ""
while naam != "STOP":
    naam = input("Geef me een naam: ")
    if naam in gasten:
        print(f"Welkom {gasten[naam]} {naam}. Kom binnen.")
        gasten.pop(naam)
    elif naam == "STOP":
        break
    else:
        print(f"De naam {naam} staat niet in de lijst.")