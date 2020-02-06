def tulosta_säkeistö(rikki, toimenpide):
    for i in range(0, 3):
        print("pikku-matin autosta on", rikki)
    print(toimenpide)
    print()


def main():
    tulosta_säkeistö("kumi puhjennut", "purukumilla me paikkaamme sen")
    tulosta_säkeistö("lasi särkynyt", "muovipussilla me korjaamme sen")
    tulosta_säkeistö("ovi irronnut", "jeesusteipillä me kiinnitämme sen")
    tulosta_säkeistö("vilkku rikkunut", "taskulampulla me korvaamme sen")

main()
