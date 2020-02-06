def main():
    i = 1
    fib = 1
    luku1 = 0
    luku2 = 1
    rivi = input("Kuinka monta Fibonaccin lukua haluat: ")
    maara = int(rivi)
    while i <= maara:
        print(str(i) + '.', fib)
        fib = luku1 + luku2
        luku1 = luku2
        luku2 = fib
        i += 1
main()
