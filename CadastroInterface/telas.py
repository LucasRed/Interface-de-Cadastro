import PySimpleGUI as sg


def menu():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Text('                           Menu        ')],
        [sg.Text('')],
        [sg.Button('Login', size=(30, 0))],
        [sg.Text('')],
        [sg.Button('Novo Cadastro', size=(30, 0))],
        [sg.Text('')],
        [sg.Button('Mudar Login/Senha', size=(30, 0))],
        [sg.Text('')],
        [sg.Button('Sair', size=(30, 0))],
        [sg.Text('', size=(30, 2))],
    ]
    return sg.Window('Menu', layout=layout, finalize=True)


def login():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Text('Login:', size=(5, 0)), sg.Input(size=(27, 0), key='login')],
        [sg.Text('Senha:', size=(5, 0)), sg.Input(size=(27, 0), key='senha', password_char='*')],
        [sg.Text('')],
        [sg.Button('Entrar', size=(30, 0))],
        [sg.Button('Voltar', size=(30, 0))],
        [sg.Text('', size=(30, 2))],
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def cadastro():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Text('Novo login:', size=(10, 0)), sg.Input(size=(23, 0), key='novo_login')],
        [sg.Text('Nova senha:', size=(10, 0)), sg.Input(size=(23, 0), key='nova_senha', password_char='*')],
        [sg.Text('')],
        [sg.Button('Cadastrar', size=(30, 0))],
        [sg.Button('Voltar', size=(30, 0))],
        [sg.Text('', size=(30, 2))]
    ]
    return sg.Window('Cadastro', layout=layout, finalize=True)


def calculadora():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Output(size=(30, 0))],
        [sg.Button('7', size=(5, 3)), sg.Button('8', size=(5, 3)), sg.Button('9', size=(5, 3)),
         sg.Button('X', size=(2, 3)), sg.Button('/', size=(2, 3))],
        [sg.Button('4', size=(5, 3)), sg.Button('5', size=(5, 3)), sg.Button('6', size=(5, 3)),
         sg.Button('+', size=(2, 3)), sg.Button('-', size=(2, 3))],
        [sg.Button('1', size=(5, 3)), sg.Button('2', size=(5, 3)), sg.Button('3', size=(5, 3)),
         sg.Button('C', size=(6, 3))],
        [sg.Button('0', size=(12, 0)), sg.Button('LogOut', size=(14, 0))]
    ]
    return sg.Window('Calculadora', layout=layout, finalize=True)


def mudar_login():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Text('Troca de login e senha')],
        [sg.Text('Login atual:', size=(10, 0)), sg.Input(size=(23, 0), key='login_atual')],
        [sg.Text('Senha atual', size=(10, 0)), sg.Input(size=(23, 0), key='senha_atual')],
        [sg.Text('')],
        [sg.Text('Novo Login:', size=(10, 0)), sg.Input(size=(23, 0), key='new_login')],
        [sg.Text('Nova Senha', size=(10, 0)), sg.Input(size=(23, 0), key='new_senha')],
        [sg.Button('OK', size=(30, 0))],
        [sg.Button('Voltar', size=(30, 0))]
    ]
    return sg.Window('Troca de senha', layout=layout, finalize=True)
