# Vul eerst aan. Daarna pas uitvoeren!
dictionary = {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

""" Geef aan wat volgende code print"""
#" Vul aan: {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}"
print(dictionary)

#" Vul aan: a
#           b
#           c
#           d
#           e
for x in dictionary:
    print(x)

#" Vul aan: ['a', 'b', 'c', 'd', 'e'] "
print( list(dictionary.keys()))

#" Vul aan: 3"
print( dictionary.get("e", 4))

#" Vul aan: [0, 1, 1, 2, 3] "
print( list(dictionary.values()))

#" Vul aan: 4"
print( dictionary.get("q", 4))

#" Vul aan: 0 a
#           1 b
#           1 c
#           2 d
#           3 e"
for x, y in dictionary.items():
    print(y, x)

#" Vul aan: "
for x in dictionary.values():
    print(x)

#" Vul aan: "
print( dictionary.pop("c"))

#"Vul aan: [('a', 0), ('b', 1), ('d', 2), ('e', 3)]"
print( list(dictionary.items()) )
