# Johdatus ohjelmointiin
# Koodipohja pinta-alalaskuihin


def pinta_ala(sivu, sivu2=None):
    if sivu > 0 and sivu2 is None:
        return sivu * sivu
    elif sivu > 0 and sivu2 is not None:
        return sivu * sivu2


def main():
    print("Neliön pinta-ala on {:.1f}".format(pinta_ala(3)))
    print("Suorakaiteen pinta-ala on {:.1f}".format(pinta_ala(4, 3)))


main()
