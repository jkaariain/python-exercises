BUSSIAIKATAULU = [630, 1015, 1415, 1620, 1720, 2000]


def main():
    syöte = int(input("Mitä kello on nyt? (kokonaislukuna): "))
    idx = -1

    print("Seuraavat bussivuorot lähtevät:")
    for i in range(len(BUSSIAIKATAULU)-1, -1, -1):
        if syöte < BUSSIAIKATAULU[0]:
            idx = 0
        elif syöte <= BUSSIAIKATAULU[i]:
            continue
        else:
            idx = i+1
            break

    for i in range(idx, idx+3):
        print(BUSSIAIKATAULU[i % len(BUSSIAIKATAULU)])

main()
