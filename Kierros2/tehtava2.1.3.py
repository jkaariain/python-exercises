def main():
    rivi = ""
    while rivi != 'K' and rivi != 'k':
        rivi = input("Onko tylsää? (k/e) ")
        while rivi != 'E' and rivi != 'e' and rivi != 'K' and rivi != 'k':
            print("Virheellinen syöte.")
            rivi = input("Yritä uudelleen: ")
    print("Noh, lopetetaan sitten.")
main()
