import time
import os
import menu_functions
from encryption import encryption
from encryption import passwords
import utn_bot

### set up ###
encryptor = encryption.Encryptor()

### MENUS ###
MAIN_OPTS = ['UTN websites', 'Exit']
UTN_OPTS = ['Auto gestion', 'Mail UTN', 'Back']


### Functions ###
def menu(mode, menu_options):
    while True:
        os.system('cls')
        # display title and menu
        menu_functions.print_title()
        menu_functions.print_subtitle(mode)
        menu_functions.display_menu(menu_options)
        option = input('\nEnter option: ')
        # validate option inputted
        if menu_functions.is_integer(option):
            if int(option) > 0 and int(option) <= len(menu_options):
                return int(option) - 1


def ask_password(encrypted_pwd):
    mode = 'Password Required'
    while True:
        os.system('cls')
        # display title and menu
        opt = menu(mode, ('Enter password', 'Back'))
        if opt == 0:
            password = input('\nEnter password: ')
            decrypted_pwd = validate_password(encrypted_pwd, password)
            if decrypted_pwd:
                return decrypted_pwd
            else:
                mode = 'Invalid Password'
        else:
            return False


def validate_password(encrypted_pwd, pwd):
    pin = ''.join([i for i in pwd if i.isdigit()])
    encryptor.password = pwd
    encryptor.pin = pin
    try:
        return encryptor.decrypt(encrypted_pwd)
    except Exception:
        return False


while True:
    os.system('cls')
    index = menu('Menu', MAIN_OPTS)

    ### UTN menu ###
    if MAIN_OPTS[index] == 'UTN websites':
        pwd = ask_password(passwords.utn_pwd)
        '''
        options [opt]:
        1 -> Auto Gestion
        2 -> Mail
        '''
        if pwd:
            os.system('cls')
            bot = utn_bot.UTNBot('44147413', pwd)
            while True:
                opt = menu(MAIN_OPTS[index], UTN_OPTS)
                if opt == 0:
                    bot.auto_gestion()
                elif opt == 1:
                    bot.mail_login()
                else:
                    break
    else:
        break
