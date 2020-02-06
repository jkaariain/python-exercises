def lue_tiedosto(tiedostonimi):
    Puhelinluettelo = {}

    try:
        tiedosto = open(tiedostonimi, "r", encoding="utf-8")

        for rivi in tiedosto:
            if rivi == "työhuone;henkilön nimi;sisäinen puhelinnumero\n":
                continue

            try:
                # tiedot[0] = huone, tiedot[1] = nimi, tiedot[2] = puh
                tiedot = rivi.split(";")
                Puhelinluettelo[tiedot[1]] = {}
                Puhelinluettelo[tiedot[1]]["huone"] = tiedot[0]
                Puhelinluettelo[tiedot[1]]["nimi"] = tiedot[1]
                Puhelinluettelo[tiedot[1]]["puh"] = tiedot[2].strip()
            except ValueError:
                print("Virhe tiedoston lukemisessa!")

        tiedosto.close()
    except OSError:
        print("Virhe tiedoston lukemisessa!")

    return Puhelinluettelo
