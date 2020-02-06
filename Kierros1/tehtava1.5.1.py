indeksikorotus = 1.17
rivi = input("Syötä opintotuen määrä: ")
opintotuki = float(rivi)
korotus = opintotuki * (indeksikorotus * 0.01 + 1)

print("Indeksikorotuksen ollessa", indeksikorotus, "prosenttia")
print("olisi opintotuki korotuksen jälkeen", korotus, "euroa")
print("ja jos sattuisi tulemaan vielä toinen indeksikorotus")
print("olisi opintotuki sen jälkeen jo", korotus * (indeksikorotus * 0.01 + 1)
      , "euroa")
