def main():
    rivi = input("Vastaa K tai E:  ")
    while rivi != 'K' and rivi != 'E' and rivi != 'k' and rivi != 'e':
        print("Virheellinen syöte.")
        rivi = input("Yritä uudelleen: ")
    print("Vastasit", rivi)
main()
