# TODO: crie uma função que peça, nome, sobrenome
# email, senha e confirmar senha.
import re


def set_users():
    bd = {}
    nome = input('Nome: ')

    if verifica_nome(nome):
        return {'msg': f'Muito curto: {nome}'}

    sobrenome = input('Sobrenome: ')

    if verifica_sobrenome(sobrenome):
        return {'msg': f'Muito curto: {sobrenome}'}

    email = input('E-mail: ')
    if verifica_email(email):
        return {'msg': f'Email inválido: {email}'}

    senha = input('Senha: ')
    if verifica_senha(senha):
        return {'msg': f'Senha inválida: {senha}'}

    confirmar = input('Confirmar senha: ')
    if verifica_confirma(senha, confirmar):
        return {'msg': f'Senhas incompatíveis!: {senha} != {confirmar}'}

    bd.update({'nome': nome, 'sobrenome': sobrenome,
               'email': email, 'senha': senha, 'confirmar': confirmar})
    return bd


def verifica_nome(nome_user):
    if len(nome_user) < 3:
        return True


def verifica_sobrenome(sobrenome_user):
    if len(sobrenome_user) < 3:
        return True


def verifica_email(email_user):
    regex = re.match(r'^[a-z]+[0-9]*@gmail.com$', email_user)
    if regex is None:
        return True


def verifica_senha(password_user):
    regex = re.findall(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[ -\/:-@[-`{-~]+).{6,}', password_user)
    if not regex:
        return True


def verifica_confirma(password_user, confirmation):
    if password_user != confirmation:
        return True


if __name__ == '__main__':
    email_user =  'ez@gmail.com'
    regex = re.match(r'^[a-z]+[0-9]*@gmail.com$', email_user)
    print(regex)
