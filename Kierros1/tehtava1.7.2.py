def main():
    rivi = input("Pelaaja 1, syötä valintasi (K/P/S): ")
    pelaaja1 = rivi
    rivi = input("Pelaaja 2, syötä valintasi (K/P/S): ")
    pelaaja2 = rivi
    if pelaaja1 == pelaaja2:
        print("Tuli tasapeli.")
    elif pelaaja1 == 'P' and pelaaja2 == 'S':
        print("Pelaaja 2 voitti!")
    elif pelaaja1 == 'S' and pelaaja2 == 'P':
        print("Pelaaja 1 voitti!")
    elif pelaaja1 == 'P' and pelaaja2 == 'K':
        print("Pelaaja 1 voitti!")
    elif pelaaja1 == 'K' and pelaaja2 == 'P':
        print("Pelaaja 2 voitti!")
    elif pelaaja1 == 'K' and pelaaja2 == 'S':
        print("Pelaaja 1 voitti!")
    elif pelaaja1 == 'S' and pelaaja2 == 'K':
        print("Pelaaja 2 voitti!")

main()
