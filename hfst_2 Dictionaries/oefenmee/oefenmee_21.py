lijst_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for rijnummer, sublijst in enumerate(lijst_2D):
    for index_sub, waarde in enumerate(sublijst):
        print(f"{rijnummer},{index_sub}: {waarde}")