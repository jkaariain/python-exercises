def main():
    fib = 1
    luku1 = 0
    luku2 = 1
    rivi = input("Kuinka monta Fibonaccin lukua haluat: ")
    maara = int(rivi)
    for i in range(1, maara+1):
        print(str(i) + '.', fib)
        fib = luku1 + luku2
        luku1 = luku2
        luku2 = fib
main()
