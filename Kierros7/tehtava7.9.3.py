def tulosta_nurinpäin_aakkostettuna(sanakirja):
    for x in sorted(sanakirja, key=lambda y: sanakirja[y]):
        print(sanakirja[x], x)
