def isot_alkukirjaimet(sana):
    a = ""
    kirjaimet = list(sana)
    idx = 0

    for i in kirjaimet:
        if idx > 0 and kirjaimet[idx-1] == " ":
            i = i.upper()
        elif idx > 0:
            i = i.lower()
        else:
            i = i.upper()
        idx += 1
        a += i

    return a


print(isot_alkukirjaimet("lEntäVÄ kaLaKUKko"))