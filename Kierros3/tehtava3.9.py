MAX_ANNOS_D = 4000


def laske_annos(p, aika, annos24):
    annos = annos24 + 15 * p
    annos -= (aika // 6) * 15 * p
    if annos < 0:
        annos = 0

    if annos + 15*p > MAX_ANNOS_D and (aika // 6) >= 1:
        return abs(annos - MAX_ANNOS_D)
    elif annos24 + 15*p - ((aika // 6) * 15 * p) < 0:
        return 15 * p
    elif annos + 15*p < MAX_ANNOS_D:
        return annos
    elif annos > MAX_ANNOS_D:
        return 0
    elif annos == 0:
        return 15 * p


def main():
    paino = int(input("Potilaan paino (kg): "))
    t = int(input("Kauanko aikaa edellisestä annoksesta (tasatunteina): "))
    a24 = int(input("Kokonaisannos viimeisen 24 tunnin aikana (mg): "))
    print("Potilaalle voi antaa parasetamolia:", laske_annos(paino, t, a24))

main()
