# Tämä dict on globaali vakio, jota hyödynnetään tulevaisuudessa hyökkäysten
# tehokkuuksien laskemisessa. Kyseessä on dict jonka avaimina on tyyppejä ja
# arvoina dictejä, joissa avaimina hyökkäysten tyyppejä ja arvoina niiden
# tehokkuuskertoimia. Esimerkiksi Normal-tyypin Pokemoniin Ghost-tyyppinen
# isku tekee 0.8x vahinkoa, mutta Fighting-tyyppinen 1.25-kertaisesti.
TYYPIT = {"Normal": {"Fighting": 1.25, "Ghost": 0.8},
          "Fighting": {"Flying": 1.25, "Psychic": 1.25, "Fairy": 1.25,
                       "Rock": 0.8, "Bug": 0.8, "Dark": 0.8},
          "Flying": {"Electric": 1.25, "Rock": 1.25, "Ice": 1.25, "Grass": 0.8,
                     "Bug": 0.8, "Fighting": 0.8, "Ground": 0.8},
          "Poison": {"Ground": 1.25, "Psychic": 1.25, "Fighting": 0.8,
                     "Bug": 0.8, "Poison": 0.8, "Grass": 0.8, "Fairy": 0.8},
          "Ground": {"Water": 1.25, "Grass": 1.25, "Ice": 1.25, "Poison": 0.8,
                     "Rock": 0.8, "Electric": 0.8},
          "Rock": {"Fighting": 1.25, "Ground": 1.25, "Steel": 1.25,
                   "Water": 1.25, "Grass": 1.25, "Normal": 0.8, "Flying": 0.8,
                   "Poison": 0.8, "Fire": 0.8},
          "Bug": {"Flying": 1.25, "Rock": 1.25, "Fire": 1.25, "Fighting": 0.8,
                  "Ground": 0.8, "Grass": 0.8},
          "Ghost": {"Ghost": 1.25, "Dark": 1.25, "Bug": 0.8, "Poison": 0.8,
                    "Normal": 0.8, "Fighting": 0.8},
          "Steel": {"Fighting": 1.25, "Ground": 1.25, "Fire": 1.25,
                    "Normal": 0.8, "Flying": 0.8, "Rock": 0.8, "Bug": 0.8,
                    "Steel": 0.8, "Grass": 0.8, "Psychic": 0.8, "Ice": 0.8,
                    "Dragon": 0.8, "Fairy": 0.8, "Poison": 0.8},
          "Fire": {"Ground": 1.25, "Rock": 1.25, "Water": 1.25, "Bug": 0.8,
                   "Steel": 0.8, "Fire": 0.8, "Ice": 0.8, "Fairy": 0.8},
          "Water": {"Grass": 1.25, "Electric": 1.25, "Steel": 0.8, "Fire": 0.8,
                    "Water": 0.8, "Ice": 0.8},
          "Grass": {"Flying": 1.25, "Poison": 1.25, "Bug": 1.25, "Fire": 1.25,
                    "Ice": 1.25, "Ground": 0.8, "Water": 0.8, "Grass": 0.8,
                    "Electric": 0.8},
          "Electric": {"Ground": 1.25, "Flying": 0.8, "Steel": 0.8,
                       "Electric": 0.8},
          "Psychic": {"Bug": 1.25, "Ghost": 1.25, "Dark": 1.25, "Fighting": 0.8,
                      "Psychic": 0.8},
          "Ice": {"Fighting": 1.25, "Rock": 1.25, "Steel": 1.25, "Fire": 1.25,
                  "Ice": 1.25},
          "Dragon": {"Ice": 1.25, "Dragon": 1.25, "Fairy": 1.25, "Fire": 0.8,
                     "Grass": 0.8, "Water": 0.8, "Electric": 0.8},
          "Dark": {"Fighting": 1.25, "Bug": 1.25, "Fairy": 1.25, "Ghost": 0.8,
                   "Psychic": 0.8},
          "Fairy": {"Poison": 1.25, "Steel": 1.25, "Fighting": 0.8, "Bug": 0.8,
                    "Dark": 0.8, "Dragon": 0.8}}

def hae_kerroin(hyökkäyksen_tyyppi, pokemonin_tyyppi):
    """
    Etsii tietorakenteesta tiedon siitä kuinka paljon vahinkoa
    tietyn tyyppinen hyökkäys tekee Pokemonille.
    :param hyökkäyksen_tyyppi: Merkkijono
    :param pokemonin_tyyppi:   Merkkijono
    :return: Palauttaa kertoimen vahingon määrälle.
    """
    if pokemonin_tyyppi in TYYPIT:

        if hyökkäyksen_tyyppi in TYYPIT[pokemonin_tyyppi]:
            return TYYPIT[pokemonin_tyyppi][hyökkäyksen_tyyppi]

    return 1

class Pokemon:
    """ Kuvaa yhtä Pokemonia, joka koostuu nimestä, tyypeistä, osumapisteistä,
        tasosta ja liikkeistä."""

    def __init__(self, laji, tyypit, hp=50, level=20):
        """
        Luokan rakentaja. Tarkastaa että kesto ja taso ovat järkeviä, ja
        tallentaa tiedot.

        :param laji:   Pokemonin laji
        :param tyypit: Pokemonin tyypit
        :param hp:     Pokemonin kestopisteiden määrä
        :param level:  Millä tasolla Pokemon on
        """

        self.__laji = laji.capitalize()
        self.__tyypit = tyypit

        if not isinstance(hp, int) or not isinstance(level, int) \
                or hp < 0 or level < 1:
            raise ValueError

        self.__hp = hp
        self.__max_hp = hp
        self.__level = level
        self.__liikkeet = {}

        if self.__hp > 0:
            self.__fainted = False
        else:
            self.__fainted = True

    def is_fainted(self):
        return self.__fainted

    def lue_tyypit(self):
        return self.__tyypit

    def lue_level(self):
        return self.__level

    def paranna(self, hp):
        if type(hp) is not int:
            return False

        if self.__fainted:
            return False

        if hp < 0:
            return False

        if self.__hp == self.__max_hp:
            print("{:s} was healed for 0 hp.".format(self.__laji))
        elif (self.__hp + hp) > self.__max_hp:
            print("{:s} was healed for ".format(self.__laji), end="")
            print("{:d} hp.".format(self.__hp + hp - self.__max_hp))
            self.__hp = self.__max_hp
        else:
            self.__hp += hp
            print("{:s} was healed for {:d} hp.".format(self.__laji, hp))

        return True

    def vahingoita(self, hp):
        if type(hp) is not int:
            return False

        if hp < 0:
            return False

        if self.__hp - hp <= 0:
            print("{:s} lost {:d} hp.".format(self.__laji, self.__hp))
            self.__hp = 0
            self.__fainted = True
            print("{:s} fainted!".format(self.__laji))
        else:
            self.__hp -= hp
            print("{:s} lost {:d} hp.".format(self.__laji, hp))

        return True

    def tulosta(self):
        """
        Tulostaa Pokemonin muodossa laji, tyypit, jäljellä olevat osumapisteet.
        """
        print(self.__laji, ", ", self.__hp, "hp", ", Types: ",
              ", ".join(self.__tyypit), sep="")
        print()

    def lisää_tyyppi(self, tyypin_nimi):
        if str.capitalize(tyypin_nimi) in TYYPIT:
            self.__tyypit.append(str.capitalize(tyypin_nimi))
            return True
        else:
            return False

    def aseta_tyypit(self, tyypit):
        for x in tyypit:
            if str.capitalize(x) in TYYPIT:
                continue
            else:
                return False

        self.__tyypit = []
        for x in tyypit:
            self.__tyypit.append(str.capitalize(x))

        return True

    def lisää_liike(self, nimi, voimakkuus, tyyppi):
        if len(self.__liikkeet) < 2 and str.capitalize(tyyppi) in TYYPIT:
            self.__liikkeet[nimi.title()] = {}
            self.__liikkeet[nimi.title()][tyyppi] = voimakkuus
            return True
        else:
            return False

    def tulosta_liikkeet(self):
        print("{:s}'s moves:".format(self.__laji))
        for x in sorted(self.__liikkeet):
            for y in self.__liikkeet[x]:
                print(x + ", " + str(self.__liikkeet[x][y]) + ", " + y)

    def hyökkää(self, nimi, pokemon):
        if nimi.title() not in self.__liikkeet:
            return False

        if self.__fainted:
            print("Pokemon has fainted and can't attack.")
            return False

        attack_power = 0
        attack_type = ""
        for x in self.__liikkeet[nimi.title()]:
            attack_power = self.__liikkeet[nimi.title()][x]
            attack_type = x

        kerroin = 1
        for x in pokemon.lue_tyypit():
            kerroin *= hae_kerroin(attack_type, x)

        print("{:s} used {:s}.".format(self.__laji, nimi.title()))

        if kerroin > 1:
            print("It's super effective!")
            pokemon.vahingoita(int(attack_power * kerroin))
        elif kerroin < 1:
            print("It's not very effective.")
            pokemon.vahingoita(int(attack_power * kerroin))
        else:
            pokemon.vahingoita(int(attack_power))

        return True

    def level_up(self):
        if self.__level < 100:
            self.__level += 1
            print("{:s} grew to level {:d}!".format(self.__laji, self.__level))

    def __lt__(self, other_pokemon):
        if self.__level < other_pokemon.lue_level():
            return True
        else:
            return False

    def __le__(self, other_pokemon):
        if self.__level > other_pokemon.lue_level():
            return True
        else:
            return False

    def __eq__(self, other_pokemon):
        if self.__level == other_pokemon.lue_level():
            return True
        else:
            return False

    def __str__(self):
        return self.__laji + ", " + str(self.__hp) + \
               "hp, Types: " + ", ".join(self.__tyypit)


def lue_pokemonit():
    print("Syötä Pokemonien tiedot muodossa laji, tyyppi tyyppi.")
    print("Lopeta syöttämällä tyhjä rivi.")
    pokemonit = []

    while 1:
        merkkijono = input()
        if merkkijono == "":
            break
        tiedot = merkkijono.split(",")
        nimi = tiedot[0]
        tyypit = (tiedot[1].rstrip()).split(" ")
        tyypit.remove('')
        pokemonit.append(Pokemon(nimi, tyypit))

    return pokemonit


def lue_pokemon():
    merkkijono = input(
        "Syötä Pokemonin tiedot muodossa laji, tyyppi tyyppi: ")
    tiedot = merkkijono.split(",")
    nimi = tiedot[0]
    tyypit = (tiedot[1].rstrip()).split(" ")
    for i in range(0, len(tyypit)):
        tyypit[i] = tyypit[i].title()
    tyypit.remove('')

    avain = input("Syötä nimi: ")

    return avain, Pokemon(nimi, tyypit)


def tulosta(sanakirja):
    avain = input("Syötä nimi: ")

    if avain in sanakirja:
        print(sanakirja[avain])
    else:
        print("Nimeä {:s} ei ole olemassa".format(avain))


def listaa(sanakirja):
    if len(sanakirja) > 0:
        for x in sorted(sanakirja):
            print(sanakirja[x])


def lisää_liike(sanakirja):
    avain = input("Syötä Pokemonin nimi: ")

    if avain in sanakirja:
        merkkijono = input("Syötä liike muodossa nimi, voima, tyyppi: ")
        tiedot = merkkijono.split(',')
        nimi = tiedot[0].rstrip()
        voima = int(tiedot[1])
        tyyppi = tiedot[2].lstrip()
        if not sanakirja[avain].lisää_liike(nimi, voima, tyyppi):
            print("Liikkeen tai voima tyyppi on virheellinen.")


def hyökkää(sanakirja):
    hyökkäävä = input("Syötä hyökkäävän Pokemonin nimi: ")
    if hyökkäävä not in sanakirja:
        print("Nimeä {:s} ei ole olemassa".format(hyökkäävä))
        return
    puolustava = input("Syötä puolustavan Pokemonin nimi: ")
    if puolustava not in sanakirja:
        print("Nimeä {:s} ei ole olemassa".format(puolustava))
        return

    nimi = input("Syötä hyökkäyksen nimi: ")

    sanakirja[hyökkäävä].hyökkää(nimi, sanakirja[puolustava])
    print("")


def main():
    pokemonit = {}

    while 1:
        komento = input("> ")

        if komento == "lisää":
            avain, pokemon = lue_pokemon()
            pokemonit[avain] = pokemon
        elif komento == "tulosta":
            tulosta(pokemonit)
        elif komento == "listaa":
            listaa(pokemonit)
        elif komento == "lisää_liike":
            lisää_liike(pokemonit)
        elif komento == "hyökkää":
            hyökkää(pokemonit)
        elif komento == "lopeta":
            break
        else:
            print("Tuntematon komento!")

    print("Hei hei!")

main()
