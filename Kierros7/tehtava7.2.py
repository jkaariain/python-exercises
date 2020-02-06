# TIE-02100
# Hirsipuu
# Jaakko Kääriäinen


def putsaa_näyttö():
    """
    Putsaa näytön tulostamalla 10 tyhjää riviä.
    :return:
    """
    print("Putsataan näyttö...")
    for i in range(0, 10):
        print()


def vastaanota_arvaus(arvatut):
    """
    Vastaanottaa pelaajalta kirjaimen ja tarkistaa sen kelvollisuuden.
    :param arvatut:
    :return:
    """
    arvaus = input("Arvaa kirjain: ").upper()

    if len(arvaus) > 1:  # Jos syötteenä on useampi kuin yksi kirjain.
        print("Virhe: syötä yksi kirjain.")
        return ""
    elif arvaus in arvatut:  # Jos kirjain on jo arvattujen listalla
        print("Hölmö arvaus, {:s} on jo arvattu.".format(arvaus))
        return ""

    return arvaus.upper()


def hirsipuu():
    """
    Itse pelifunktio
    :return:
    """
    arvattava_sana = input("Syötä arvuuteltava sana: ").upper()
    arvattu_sana = "_" * len(arvattava_sana)
    arvatut_kirjaimet = []
    arvauskerta = 1
    sana_arvattu = False

    putsaa_näyttö()

    print("Peli alkakoon! Saat arvata 10 kirjainta. Mikä sana on kyseessä?")
    while arvauskerta <= 10 and arvattu_sana != arvattava_sana:
        print(arvattu_sana)
        arvaus = vastaanota_arvaus(arvatut_kirjaimet)

        arvatut_kirjaimet.append(arvaus.upper())  # Lisää kirjain arvattujen
        # joukkoon.
        for i in range(0, len(arvattava_sana)):
            if arvattava_sana[i] == arvaus:
                sana = list(arvattu_sana)  # Muuta arvattu sana listaksi
                # jotta merkkijonon sisältöä voidaan muuttaa.
                sana[i] = arvattava_sana[i] # Korvaa ne alaviivat arvatulla
                # kirjaimella, joka esiintyy arvattavassa sanassa.
                arvattu_sana = ''.join(sana) # Muuta arvattu sana takaisin
                # listasta merkkijonoksi.

        if arvattu_sana == arvattava_sana:
            sana_arvattu = True

        arvauskerta += 1

    print(arvattu_sana)
    if sana_arvattu:
        print("Hyvä! Arvasit koko sanan!")
    else:
        print("Arvauskerrat loppuivat kesken. Sana olisi ollut {:s}"
              .format(arvattava_sana))
    pass


def main():
    hirsipuu()


main()
