def ovatko_kaikki_alkiot_samoja(lista):
    if not lista:
        return True

    i = lista[0]
    for x in lista:
        if x == i:
            continue
        else:
            return False
    return True

asd = []

ovatko_kaikki_alkiot_samoja(asd)
