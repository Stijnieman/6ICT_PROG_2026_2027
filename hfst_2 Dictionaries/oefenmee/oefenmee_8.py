# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad_geb = input("In welke stad bent u? : ")
if stad_geb in steden_temp:
    temp = steden_temp.get(stad_geb)
    print(f"Het is hier {temp}°C")
else:
    print("Het is hier ??? °C.")