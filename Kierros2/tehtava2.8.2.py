def main():
    day = 3
    month = 1
    while month <= 12:
        print(day, ".", month, ".", sep="")
        day += 7
        # JAN
        if month == 1 and day > 31:
            month += 1
            day = abs(day - 31)
        # FEB
        elif month == 2 and day > 28:
            month += 1
            day = abs(day - 28)
        # MAR
        elif month == 3 and day > 31:
            month += 1
            day = abs(day - 31)
        # APR
        elif month == 4 and day > 30:
            month += 1
            day = abs(day - 30)
        # MAY
        elif month == 5 and day > 31:
            month += 1
            day = abs(day - 31)
        # JUN
        elif month == 6 and day > 30:
            month += 1
            day = abs(day - 30)
        # JUL
        elif month == 7 and day > 31:
            month += 1
            day = abs(day - 31)
        # AUG
        elif month == 8 and day > 31:
            month += 1
            day = abs(day - 31)
        # SEP
        elif month == 9 and day > 30:
            month += 1
            day = abs(day - 30)
        # OCT
        elif month == 10 and day > 31:
            month += 1
            day = abs(day - 31)
        # NOV
        elif month == 11 and day > 30:
            month += 1
            day = abs(day - 30)
        # DEC
        elif month == 12 and day > 31:
            month += 1

main()
