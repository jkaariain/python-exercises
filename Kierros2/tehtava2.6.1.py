def main():
    print("Anna sademaaria, lopeta luvulla 999999.")
    kok_sademaara = 0
    lkm = 0
    rivi = 0
    while float(rivi) != 999999:
        rivi = input("Anna sademaara: ")
        sademaara = float(rivi)
        if sademaara >= 0 and sademaara != 999999:
            kok_sademaara += sademaara
            lkm += 1
    if lkm > 0:
        print("Sademaarien keskiarvo on ", kok_sademaara/lkm)
    else:
        print("Yhtaan sademaaraa ei syotetty.")

main()
