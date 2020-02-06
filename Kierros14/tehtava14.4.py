def tee_laskuri():
    luku = [0]

    def laskuri():
        luku[0] += 1
        return luku[0]

    return laskuri
