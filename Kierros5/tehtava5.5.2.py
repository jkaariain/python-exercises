def onko_suuruusjärjestyksessä(lista):
    for i in range(0, len(lista)-1):
        if lista[i] < lista[i+1]:
            continue
        else:
            return False
    return True
