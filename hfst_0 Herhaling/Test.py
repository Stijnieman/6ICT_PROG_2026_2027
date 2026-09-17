# nummers = ["+32 470 998301", "+32 483 313220", "+32 453 231456"]
# namen = ["jan", "Piet", "Kapper Korneel"]

# geg_naam = input("Geef me een naam: ")
# for index, naam in enumerate(namen):
#     if geg_naam == naam:
#         print(nummers[index])
#         print(namen[index])

telefoonboek = {
    "Jan": "+32 470 998301",
    "Piet": "+32 483 313220",
    "Kapper Korneel": "+32 453 231456"
}

naam_gbr = input("Geef een naam: ")
if naam_gbr in telefoonboek:
    print(telefoonboek[naam_gbr])
else:
    print("Naam zit niet in telefoonboek")