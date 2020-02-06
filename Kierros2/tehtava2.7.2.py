# Johdatus ohjelmointiin
# Koodipohja piin likiarvon tulostamiseen muotoilulla

def main():
    pii = 3.14159265358979323846
    print("Piin likiarvo on {:.0f} tai jos tarkkoja halutaan olla"
          ", niin {:.4f}".format(pii, pii))
main()
