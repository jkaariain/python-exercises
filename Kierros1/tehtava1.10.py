def main():
    rivi = input("Ostosten hinta: ")
    hinta = int(rivi)
    rivi = input("Maksettu rahasumma: ")
    maksettu_summa = int(rivi)
    vaihtoraha = maksettu_summa - hinta
    if vaihtoraha > 0:
        kymppi = vaihtoraha // 10
        vaihtoraha -= kymppi * 10
        viisi = vaihtoraha // 5
        vaihtoraha -= viisi * 5
        kaksi = vaihtoraha // 2
        vaihtoraha -= kaksi * 2
        yksi = vaihtoraha // 1
        vaihtoraha -= yksi * 1
        print("Anna vaihtorahaa:")
        if kymppi > 0:
            print(kymppi, "kymppiä")
        if viisi > 0:
            print(viisi, "vitosta")
        if kaksi > 0:
            print(kaksi, "kaksieuroista")
        if yksi > 0:
            print(yksi, "euroa")
    else:
        print("Ei vaihtorahaa")

main()
