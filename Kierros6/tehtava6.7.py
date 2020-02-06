def käännä_nimi(nimi):
    if nimi == "," or nimi == "":
        return ""

    nimet = []
    yksi_väli = False

    if nimi.count(" ", 0, len(nimi)) == 1 and nimi.count(",", 0, len(nimi))\
            == 0:
        nimet = nimi.split(" ")
        yksi_väli = True
    elif nimi.count(",", 0, len(nimi)) >= 1:
        nimet = nimi.split(",")

    if yksi_väli:
        return str(nimet[1]) + " " + str(nimet[0])

    for i in range(0, len(nimet)):
        nimet[i] = nimet[i].strip()

    if nimet[1] == "":
        result = nimet[0]
    elif nimet[0] == "":
        result = nimet[1]
    else:
        result = str(nimet[1]) + " " + str((nimet[0]))

    result.strip()

    return result
