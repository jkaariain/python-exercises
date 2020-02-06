def permutaatio(n):
    if n < 0:
        return 1

    tulos = 1
    while n > 0:
        tulos *= n
        n -= 1
    return tulos


def kombinaatio(n_alkioita, k_alkioita):
    """
    Funktio laskee kombinaation.
    :param n_alkioita: n alkioiden määrä
    :param k_alkioita: k alkioiden määrä
    :return: kombinaation arvo
    """
    if n_alkioita >= k_alkioita:
        return permutaatio(n_alkioita) // \
           (permutaatio(n_alkioita-k_alkioita) * permutaatio(k_alkioita))
    else:
        return 0


def main():
    lottopallot = int(input("Syötä lottopallojen kokonaismäärä: "))
    arvottavat = int(input("Syötä arvottavien pallojen määrä: "))

    if lottopallot < 0:
        print("Pallojen määrän oltava positiivinen luku.")
        return
    elif lottopallot < arvottavat:
        print("Arvottavia palloja saa olla enintään pallojen "
              "kokonaismäärän verran.")
        return

    print("Kun pelataan yksi rivi, todennäköisyys saada ", arvottavat,
          " oikein on 1/", kombinaatio(lottopallot, arvottavat), sep="")

main()
