""" Oefening 1 (  / 2)
Los onderstaande vragen op door gebruik te maken van de geneste dictionary 'pc'.
"""

pc = {
    "processor": {
        "merk": "Intel",
        "model": "i7-12700K",
        "specificaties": {"kloksnelheid": "3.6GHz", "cores": 12, "threads": 20},
        "compatibele_sockets": ["LGA1200", "LGA1700", "LGA1800"]
    },
    "geheugen": {
        "type": "DDRM",
        "capaciteit": "32GB",
        "snelheid": "3200MHz"
    },
    "opslagmedia": {
        "HDD1": {"type": "HDD", "capaciteit": "1TB", "snelheid": "7200RPM"},
        "HDD2": {"type": "HDD", "capaciteit": "256GB", "snelheid": "7200RPM"},
        "SSD1": {"type": "NVMe", "capaciteit": "512GB", "leessnelheid": "3500MB/s"},
        "SSD2": {"type": "NVMe", "capaciteit": "256GB", "leessnelheid": "3500MB/s"}

    },
    "grafische_kaart": {
        "merk": "NVIDIA",
        "model": "RTX 3060",
        "geheugen": "12GB",
        "poorten": ["HDMI", "DisplayPort", "DVI"],
    },
    "revews": ["3/5", "7/10", "3,5 sterren"]
}

""" Vraag 1 ( /0.5) 
Print onderstaande zin. Haal het socket-type op uit bovenstaande dictionary.
'De processor ondersteunt socket-type: LGA1700'
"""
# print(f"De processor ondersteunt socket-type: {pc["processor"]["compatibele_sockets"][1]}")

""" Vraag 2 ( /0.5) 
Update de geheugencapaciteit.
Het huidige geheugentype klopt niet. Verander "DDRM" naar "DDR5".
"""
# pc["geheugen"]["type"] = "DDR5"

""" Vraag 3 ( /0.5) 
De sleutel "revews" is verkeerd gespeld. Corrigeer dit naar "reviews" in de dictionary.
Zorg ervoor dat de waarde verbonden aan deze sleutel wel hetzelfde blijft.
  TIP! Maak een nieuwe sleutel aan met de correcte naam, verwijder erna de oude sleutel.
"""
# reviews = pc["revews"]
# pc.pop("revews")
# pc["reviews"] = reviews
# print(pc)

""" Vraag 4 ( /0.5) 
Print een overzicht van alle opslagmedia en hun capaciteiten.
Het overzicht moet blijven werken ook als er honderden opslagmedia zijn.

De output moet er als volgt uitzien.
    Opslagoverzicht:
        - HDD1: 1TB
        - HDD2: 256GB
        - SSD1: 512GB
        - SSD2: 128GB
        - ... (voor ieder ander opslagmedia dat je zelf kan toevoegen)
"""
# for opslag,eig in pc['opslagmedia'].items():
#     print(opslag, eig["capaciteit"])