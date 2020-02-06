def main():
    i = 1
    rivi = input("Syötä luku: ")
    luku = int(rivi)
    tulos = 0
    while tulos <= 100:
        tulos = i*luku
        print(i, "*", luku, "=", tulos)
        i += 1
main()
