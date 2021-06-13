import logicaCalc as lc
from telas import *
from arquivos import *

r = 0

if not arquivo_existe():
    criar_arquivo()

janela_menu, janela_login, janela_cadastro, janela_calculadora, janela_troca = menu(), None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Login':
        janela_menu.hide()
        janela_login = login()

    if window == janela_login and event == 'Entrar':
        if validacao(values['login'], values['senha']):
            janela_login.hide()
            janela_calculadora = calculadora()
        else:
            sg.popup('Login Invalido')

    if window == janela_login and event == 'Voltar':
        janela_login.hide()
        janela_menu.un_hide()

    if event == 'Novo Cadastro':
        janela_cadastro = cadastro()
        janela_menu.hide()

    if window == janela_cadastro and event == 'Cadastrar':
        if not validacao(values['novo_login'], values['nova_senha']):
            cadastro_login(values['novo_login'], values['nova_senha'])
            sg.popup('Cadastro efetuado com sucesso')
        else:
            sg.popup('Esse login/senha ja existe!')

    if window == janela_cadastro and event == 'Voltar':
        janela_cadastro.hide()
        janela_menu.un_hide()

    if window == janela_calculadora and event == 'Voltar':
        janela_calculadora.hide()
        janela_login.un_hide()

    if event == 'Mudar Login/Senha':
        janela_menu.hide()
        janela_troca = mudar_login()

    if window == janela_troca and event == 'OK':
        if validacao(values['login_atual'], values['senha_atual']):
            change(values['login_atual'], values['senha_atual'], values['new_login'], values['new_senha'])
            sg.popup('Troca realizada com sucesso!')
        else:
            sg.popup('Não foi possivel realizar a troca')

    if window == janela_troca and event == 'Voltar':
        janela_troca.hide()
        janela_menu.un_hide()

    if window == janela_calculadora:
        if event == 'LogOut':
            lc.n1.clear()
            lc.n2.clear()
            r = 0
            janela_calculadora.hide()
            janela_login.un_hide()
        if event == '1':
            print(lc.getnum('1'))
        if event == '2':
            print(lc.getnum('2'))
        if event == '3':
            print(lc.getnum('3'))
        if event == '4':
            print(lc.getnum('4'))
        if event == '5':
            print(lc.getnum('5'))
        if event == '6':
            print(lc.getnum('6'))
        if event == '7':
            print(lc.getnum('7'))
        if event == '8':
            print(lc.getnum('8'))
        if event == '9':
            print(lc.getnum('9'))
        if event == '0':
            print(lc.getnum('0'))
        if event == '+':
            if lc.n1:
                lc.n2 = lc.n1[:]
                lc.n1.clear()
                if r == 0:
                    r = int(lc.juntar(lc.n2))
                else:
                    print(f'{r}+\n')
                    r += int(lc.juntar(lc.n2))
                    print(r)
        if event == 'X':
            if lc.n1:
                lc.n2 = lc.n1[:]
                lc.n1.clear()
                if r == 0:
                    r = int(lc.juntar(lc.n2))
                else:
                    print(f'{r}x\n')
                    r *= int(lc.juntar(lc.n2))
                    print(r)
        if event == '/':
            if lc.n1:
                lc.n2 = lc.n1[:]
                lc.n1.clear()
                if r == 0:
                    r = int(lc.juntar(lc.n2))
                else:
                    print(f'{r}/\n')
                    r /= int(lc.juntar(lc.n2))
                    print(r)
        if event == '-':
            if lc.n1:
                lc.n2 = lc.n1[:]
                lc.n1.clear()
                if r == 0:
                    r = int(lc.juntar(lc.n2))
                else:
                    print(f'{r}-\n')
                    r -= int(lc.juntar(lc.n2))
                    print(r)
        if event == 'C':
            lc.n1.clear()
            lc.n2.clear()
            r = 0
            print('\n', r)
