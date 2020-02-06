def main():
    rivi = input("Mikä fiilis? (1-10) ")
    mieliala = int(rivi)
    if mieliala >= 1 and mieliala <= 10:
        if mieliala == 10:
            print("Tunnelmaan sopiva hymiö voisi olla :-D")
        elif mieliala > 7:
            print("Tunnelmaan sopiva hymiö voisi olla :-)")
        elif mieliala == 1:
            print("Tunnelmaan sopiva hymiö voisi olla :'(")
        elif mieliala < 4:
            print("Tunnelmaan sopiva hymiö voisi olla :-(")
        else:
            print("Tunnelmaan sopiva hymiö voisi olla :-|")
    else:
        print("Virheellinen syöte!")

main()
