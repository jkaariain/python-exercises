def main():
    vokaalit = "AEIOUYÅÄÖaeiouyåäö"
    vokaalit_lkm = 0
    syöte = input("Syötä sana: ")

    for i in syöte:  # Iteroi jokainen merkki syötteessä
        for j in vokaalit:  # Iteroi jokainen merkki vokaaleissa
            if i == j:
                vokaalit_lkm += 1

    konsonantit_lkm = len(syöte) - vokaalit_lkm

    print("Sana {:s} sisältää {:d} vokaalia ja {:d} konsonanttia"
          .format(syöte, vokaalit_lkm, konsonantit_lkm))

main()
