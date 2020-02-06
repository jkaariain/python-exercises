def main():
    edel_mittaustulos = 0
    ulkopuolella_lkm = 0
    pilalla = False
    mittaustulos_lkm = int(input("Syötä mittausten lukumäärä: "))
    if mittaustulos_lkm <= 0:
        print("Mittausten lukumäärän tulee olla positiivinen kokonaisluku.")
    else:
        for i in range(1, mittaustulos_lkm+1):
            mittaustulos = int(input("Syötä {:d}. mittaustulos: ".format(i)))
            if mittaustulos < 20 or mittaustulos > 25:
                ulkopuolella_lkm += 1

            if edel_mittaustulos != 0:
                if (edel_mittaustulos < 20 and mittaustulos < 20) or \
                        (edel_mittaustulos > 25 and mittaustulos > 25) or \
                        (edel_mittaustulos < 20 and mittaustulos > 25) or \
                        (edel_mittaustulos > 25 and mittaustulos < 20):
                    pilalla = True
                    break

            edel_mittaustulos = mittaustulos

            if (ulkopuolella_lkm / mittaustulos_lkm) * 100 > 10.0:
                pilalla = True
                break

        if pilalla:
            print("Viinisi on pilalla")
        else:
            print("Viinisi on hyvää")

main()
