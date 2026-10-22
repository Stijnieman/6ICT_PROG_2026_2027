# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for waarde, sleutel in fruitmand.items():
    aantal = int(input(f"Hoeveel {sleutel} bijkopen (huidig aantal is {waarde}): "))
    fruitmand[sleutel] += aantal
