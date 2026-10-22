dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]

tot_rij = 0
tot_kolom = 0
for aantal in dambord_2D:
    tot_rij += 1
rij = int(input("Geef me een rij: "))
kolom = int(input("Geef me een kolom: "))

if tot_rij < rij:
    print("Dit kan niet")
else:
    print(f"Op deze index staat {dambord_2D[rij][kolom]}")