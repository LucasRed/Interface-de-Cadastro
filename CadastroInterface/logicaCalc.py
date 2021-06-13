n1 = list()
n2 = list()


def getnum(numero, lista=None, jump=True):
    if lista is None:
        lista = n1
    lista.append(numero)
    g = ''.join(lista)

    if jump:
        return f'{g}\n'
    else:
        return g


def inteirar(n):
    return int(n)


def juntar(n):
    return ''.join(n)
