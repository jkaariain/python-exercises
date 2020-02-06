def tee_lista(kpl):
    lista = []
    print("Syötä {:d} kpl lukuja:".format(kpl))
    for i in range(0, kpl):
        rivi = int(input())
        lista.append(rivi)
    return lista


def main():
    rivi = int(input("Kuinka monta lukua haluat käsitellä: "))
    lukulista = tee_lista(rivi)
    rivi = int(input("Syötä etsittävä luku: "))
    kuinka_monta = lukulista.count(rivi)
    if kuinka_monta > 0:
        print("{:d} esiintyy syöttämiesi lukujen joukossa {:d} kertaa.".format
              (rivi, kuinka_monta))
    else:
        print("{:d} ei esiinny syöttämiesi lukujen joukossa.".format(rivi))

main()
