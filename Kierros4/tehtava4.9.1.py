def tulosta_ruutu(leveys, korkeus, reunamerkki="#", sisämerkki=" "):
    for i in range(0, korkeus):
        if i == 0 or i == korkeus-1:
            print("{:s}".format(leveys*reunamerkki))
            continue
        print(reunamerkki, sisämerkki*(leveys-2), reunamerkki, sep="")
    print()

tulosta_ruutu(5, 4)
tulosta_ruutu(3, 8, reunamerkki="*")
tulosta_ruutu(5, 4, reunamerkki="O", sisämerkki="o")
tulosta_ruutu(6, 4, reunamerkki="O", sisämerkki=".")
