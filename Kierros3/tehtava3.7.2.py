def ahaa(toisto):
    for i in range(0, toisto):
        print("ahaa")


def säkeistö(eka, toinen):
    print(eka)
    ahaa(2)
    print(eka)
    ahaa(2)
    print(eka)
    print(toinen)
    ahaa(3)
    print()


def main():
    säkeistö("saku sammakko kosiomatkallaan", "hän lauleli kauniita laulujaan")
    säkeistö("hän hillevi hiiren tavatessaan",
             "pyysi mukanaan tulemaan pappilaan")
    säkeistö("mikset kultasein kosinut aikanaan",
             "minut matias myyrälle naitetaan")
    säkeistö("sulle matias sovi ei laisinkaan",
             "sillä multaa on myyrällä varpaissaan")

main()
