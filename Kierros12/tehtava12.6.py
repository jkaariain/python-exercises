import json
import csv


def main():
    nimi = input("Syötä luettavan tiedoston nimi: ")
    kirj_nimi = input("Valitse kirjoitettavan tiedoston nimi: ")
    csv_sisältö = []

    try:
        json_sisältö = open(nimi, "r", encoding="utf-8").read()
        x = json.loads(json_sisältö)

        for pysäkki in x:
            string = [pysäkki["stationId"], pysäkki["name"]]
            csv_sisältö.append(string)

        with open(kirj_nimi, "w", encoding="utf-8", newline='') as csvfile:
            kirj_tiedosto = csv.writer(csvfile, delimiter=';')
            kirj_tiedosto.writerows(csv_sisältö)

        print()
        print("Tiedoston muuntaminen onnistui.")
    except OSError:
        print()
        print("Virhe tiedoston käsittelyssä.")
        return
    except json.JSONDecodeError:
        print()
        print("Virhe tiedoston käsittelyssä.")
        return
    except csv.Error:
        print()
        print("Virhe tiedoston käsittelyssä.")
        return

main()
