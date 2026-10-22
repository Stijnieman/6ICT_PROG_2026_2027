""" OEFENING 1 (  / 3)
Gegeven is een grote datastructuur over de band Queen.
Los de vragen onder deze datastructuur op.

Je moet voor iedere vraag springen in de datastructuur!
"""

band = {
    "algemene_info": {
        "naam": "Queen",
        "opgericht": 1970,
        "leden": [
            {
                "naam": "Freddie Mercury",
                "rol": "zanger",
                "instrumenten": ["zang", "piano"],
                "liedjes": [
                    {"titel": "Bohemian Rhapsody", "jaar": 1975, "album": "A Night at the Opera"},
                    {"titel": "Don't Stop Me Now", "jaar": 1978, "album": "Jazz"}
                ]
            },
            {
                "naam": "Brian May",
                "rol": "gitarist",
                "instrumenten": ["gitaar", "zang"],
                "liedjes": [
                    {"titel": "We Will Rock You", "jaar": 1977, "album": "News of the World"}
                ]
            },
            {
                "naam": "Roger Taylor",
                "rol": "zanger",
                "instrumenten": ["drums", "bass"],
                "liedjes": [
                    {"titel": "Radio Ga Ga", "jaar": 1984, "album": "The Works"}
                ]
            }
        ]
    },
    "awards": ["Brit Award", "Grammy Lifetime Achievement Award", "Best Song of All Time"],
    "tour": {
        "naam": "A Night at the Opera Tour", 
        "jaar": 1975, 
        "locaties": ["Londen", "New York", "Tokyo"]
    }
}

# Vraag 1: print de award "Best Song of All Time" door in de structuur te springen. (0.5)
print(band["awards"][2])
# Vraag 2: Voeg "Sydney" toe aan de locaties waar hun toer is doorgegaan. (0.5)
band["tour"]["locaties"].append("Sydney") 
# Vraag 3: Wijzig de rol van Roger Taylor naar "drummer". (0.5)
band["algemene_info"]["leden"][2]["rol"] = "drummer"
# Vraag 4: print alle awards die de band behaald heeft. Gebruik hiervoor de for-loop. (0.5)
for award in band["awards"]:
    print(award)
# Vraag 5: Print de titel van ieder liedje in de datastructuur. Gebruik hiervoor de for-loop. (1)
#          !! Opgelet: dit is een lastige vraag !!