# TIE-02100
# Kulujen tasaus
# Jaakko Kääriäinen


def main():
    tiedosto_nimi = input("Anna tiedoston nimi: ")
    jatka = True
    kokonaiskustannukset = 0.0
    sanakirja = {}

    try:
        tiedosto = open(tiedosto_nimi, "r")

        for rivi in tiedosto:
            if jatka:
                try:
                    nimi, kulut = rivi.split(":")
                    kulut = float(kulut)
                    kokonaiskustannukset += kulut

                    if nimi not in sanakirja:
                        sanakirja[nimi] = kulut
                    else:
                        sanakirja[nimi] += kulut
                except ValueError:
                    jatka = False
                    print("Virhe! Tiedoston rivien pitää olla muotoa "
                          "nimi:summa.")

        tiedosto.close()
    except OSError:
        jatka = False
        print("Virhe! Tiedostoa " + tiedosto_nimi + " ei voida lukea.")

    # Jatka ohjelman suoritusta, jos virheitä ei ole tapahtunut.
    if jatka and len(sanakirja) > 0:
        print("Kokonaiskustannukset ovat: {:.2f}e".
              format(kokonaiskustannukset))
        # Tasatun kulun määrä maksajien kesken.
        tasaus = kokonaiskustannukset / len(sanakirja)

        for avain in sorted(sanakirja):
            print("{:s} on maksanut {:.2f}e, ".format(avain, sanakirja[avain]),
                  end="")
            if sanakirja[avain] > tasaus:  # Jos henkilön kulut ylittävät
                # tasauksen
                refund = sanakirja[avain] - tasaus
                # Maksua ei suoriteta, jos saatavaa on alle 5 senttiä
                if refund <= 0.05:
                    print("eikä hänellä ole maksettavaa tai saatavaa.")
                else:
                    print("hänen pitää saada takaisin {:.2f}e.".format(refund))
            elif sanakirja[avain] == tasaus:
                print("eikä hänellä ole maksettavaa tai saatavaa.")
            else:
                maksettava = tasaus - sanakirja[avain]
                # Maksua ei suoriteta, jos saatavaa on alle 5 senttiä
                if maksettava <= 0.05:
                    print("eikä hänellä ole maksettavaa tai saatavaa.")
                else:
                    print("hänen pitää maksaa vielä {:.2f}e.".format
                          (maksettava))


main()
