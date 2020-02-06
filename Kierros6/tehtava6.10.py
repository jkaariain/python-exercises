def laske_abbat(string):
    abba_lkm = 0

    for i in range(0, len(string)):
        if string[i] == "a" and i+3 < len(string):
            if string[i + 1] == "b" and string[i + 2] == "b" \
                    and string[i + 3] == "a":
                abba_lkm += 1
        else:
            continue

    return abba_lkm
