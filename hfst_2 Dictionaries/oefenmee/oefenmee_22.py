lijst = [ [4, 5, 1, 9, 3],
          [4, 6, 1],
          [8, 3, 5, 0],
          [7] ]
som = 0
gem = 0

for index_hoofd, sublijst in enumerate(lijst):
    for waarde in sublijst:
        som += waarde
print(som)