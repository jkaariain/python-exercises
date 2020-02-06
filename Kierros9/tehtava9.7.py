import os

TIEDOSTOPÄÄTE = ".mp3"


def korjaa_tiedostot(kansion_nimi):
    tiedostot = os.listdir(kansion_nimi)
    uudelleennimetty = []

    os.chdir(kansion_nimi)

    if len(tiedostot) > 0:
        for x in tiedostot:
            if not x.endswith(TIEDOSTOPÄÄTE):
                tiedostot.pop()

        if len(tiedostot) > 0:
            for x in tiedostot:
                osat = x.split("-")
                if len(osat) == 3:
                    artisti = osat[1]
                    nimi = (osat[2])[0:len(osat[2])-4]
                    uudelleennimetty.append(str(nimi) + '-'
                                            + str(artisti) + TIEDOSTOPÄÄTE)

            idx = 0
            for i in tiedostot:
                os.rename(i, uudelleennimetty[idx])
                idx += 1
