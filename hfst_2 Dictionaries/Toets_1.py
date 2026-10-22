""" Oefening 1 (  / 4)
Er is een beveiligingsinbreuk vastgesteld in ons systeem. Uit voorzorg
zal de IT-afdeling de wachtwoorden van een specifieke groep wijzigen. 

Het gaat om alle gebruikers waarvan de gebruikersnaam GEEN punt ('.') bevat.
Pas de wachtwoorden van deze accounts aan. Zet een ! achter hun huidig wachtwoord.
Print op het einde de gewijzigde dictionary, en hoevaak je een wachtwoord hebt gewijzigd.

BELANGRIJK:
De code moet ook werken als de dictionary later uitgebreid wordt.
Doe maar alsof er duizenden gebruikers in de dictionary staan.
"""

""" VERWACHTE OUTPUT NA OVERLOPEN DICTIONARY:
-------------------------------------------------------------------------------
{'hendrik.clijsters': 'SteDri39', 
 'spma300906': 'MauSpi21!',         --> GEWIJZIGD
 'bija080714': 'BirJal08!',         --> GEWIJZIGD
 'johan.colson': 'ColHan44',        
 'momo250308': 'SerRam26!'          --> GEWIJZIGD
}
Aantal gewijzigde wachtwoorden: 3
-------------------------------------------------------------------------------
"""

gew_ww = 0
gebruikers = {
    'hendrik.clijsters': 'SteDri39',
    'spma300906': 'MauSpi21',
    'bija080714': 'BirJal08',
    'johan.colson': 'ColHan44',
    'momo250308': 'SerRam26'
}
for naam, sleutel in gebruikers.items():
    if "." not in naam:
        gebruikers[naam] += "!"
        gew_ww += 1
        print(f"{naam}: {sleutel}   --> GEWIJZIGD")
    else:
        print(f"{naam}: {sleutel}")
print(f"Aantal gewijzigde wachtwoorden: {gew_ww}")
print(gebruikers)

