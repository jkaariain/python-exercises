from math import sqrt


def pinta_ala(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return sqrt(s*(s-s1)*(s-s2)*(s-s3))


def main():
    sivu1 = float(input("Syötä ensimmäinen sivun pituus: "))
    sivu2 = float(input("Syötä toinen sivun pituus: "))
    sivu3 = float(input("Syötä kolmas sivun pituus: "))
    print("Kolmion pinta-ala on {:.1f}".format(pinta_ala(sivu1, sivu2, sivu3)))

main()
