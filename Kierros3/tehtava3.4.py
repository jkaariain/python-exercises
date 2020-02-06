def main():
    mittaus_lkm = int(input("Syötä mittausten lukumäärä: "))
    pilalla = False
    oikea_syote = True

    # Mittaustulokset tallennetaan listaan
    mittaus_tulos = []
    kaymis_ulkpl_lkm = 0

    if mittaus_lkm <= 0:
        oikea_syote = False
        print("Mittausten lukumäärän tulee olla positiivinen kokonaisluku.")
    else:
        for i in range(1, mittaus_lkm+1):
            mittaus_tulos.append(float(input(
                "Syötä {:d}. mittaustulos: ".format(i))))

            if i == 1:
                continue

            # Onko kaksi peräkkäistä tulosta käymislämpötilan ulkopuolella?
            if (mittaus_tulos[i-1] < 20.0 or mittaus_tulos[i-1] > 25.0) and \
                    (mittaus_tulos[i-2] < 20.0 or mittaus_tulos[i-2] > 25.0):
                pilalla = True
                break

    if oikea_syote:
        # Kuinka monta tulosta on käymislämpötilan ulkopuolella?
        for i in mittaus_tulos:
            if i < 20.0 or i > 25.0:
                kaymis_ulkpl_lkm += 1

        # Onko yli 10% mittaustuloksista käymislämpötilan ulkopuolella?
        if (kaymis_ulkpl_lkm / (mittaus_lkm+1)) * 100 > 10.0:
            pilalla = True

        if pilalla:
            print("Viinisi on pilalla.")
        else:
            print("Viinisi on hyvää.")

main()
