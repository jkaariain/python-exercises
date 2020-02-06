def main():
    i = 1
    rivi = input("Syötä luku: ")
    luku = int(rivi)
    while i <= 10:
        print(i, "*", luku, "=", i*luku)
        i += 1
main()
