def arquivo_existe(nome='cadastrados.txt'):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome='cadastrados.txt'):
    a = open(nome, 'w')
    a.close()


def cadastro_login(login, senha, nome='cadastrados.txt'):
    a = open(nome, 'a')
    a.write(f'{login};{senha}\n')
    a.close()


def validacao(login, senha, nome='cadastrados.txt'):
    a = open(nome, 'r')
    ret = f'{login};{senha}\n'
    if ret in a:
        a.close()
        return True
    else:
        a.close()
        return False


def change(login_atual, senha_atual, login_novo, senha_nova, nome='cadastrados.txt'):
    ret = f'{login_atual};{senha_atual}\n'

    a = open(nome, 'r')
    lido = a.readlines()
    lido.pop(lido.index(ret))
    a.close()

    a = open(nome, 'w')
    a.writelines(lido)
    a.close()

    cadastro_login(login_novo, senha_nova)
