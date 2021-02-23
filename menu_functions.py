import os
import logos


def print_title():
    indentation = ' ' * (os.get_terminal_size(1)[0]//2 - logos.title_size//2)
    title_lines = list(logos.title.split('\n'))
    for line in title_lines:
        print(f'{indentation}{line}')


def print_subtitle(mode):
    indentation = ' ' * (os.get_terminal_size(1)[0]//2 - logos.title_size//2)
    spaces = ' ' * ((logos.title_size - len(mode) - 4)//2)
    print(f'\n\n{indentation}[{spaces}{mode}{spaces}]\n\n')


def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def display_menu(menu_options):
    for i, option in enumerate(menu_options):
        print(f'[{i+1}] {option}', end='\n\n')
