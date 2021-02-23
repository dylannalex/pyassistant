import encryption


def encrypt(txt, pwd):
    pin = ''.join([i for i in pwd if i.isdigit()])
    encryptor = encryption.Encryptor(pwd, pin)
    return encryptor.encrypt(txt)


if __name__ == '__main__':
    txt = 'example'
    pwd = 'test123'
    print(f'txt: {txt}\npwd: {pwd}')
    print(f'Encryption:{encrypt(txt, pwd)}')
