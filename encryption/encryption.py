hexa_values = {'10': 'A', '11': 'B',
               '12': 'C', '13': 'D',
               '14': 'E', '15': 'F'}


def decimal_to_hexa(n, sign=False):
    '''
    ### Param ###
    n: decimal number

    ### Return ###
    n in base 16
    '''

    if sign:
        if n < 0:
            return '1' + decimal_to_hexa(n * -1)
        else:
            return '0' + decimal_to_hexa(n)

    if n < 16:
        if str(n) in hexa_values:
            return hexa_values[str(n)]
        return str(n)

    else:
        value = str(n - 16 * (n // 16))
        if value in hexa_values:
            return decimal_to_hexa(n // 16) + hexa_values[value]
        else:
            return decimal_to_hexa(n // 16) + value


def hexa_to_decimal(n, sign=False):
    '''
    ### Param ###
    n: hexadecimal number

    ### Return ###
    n in base 10
    '''
    result, s = 0, 1
    if sign:
        # if number contains sign bits, remove first digit
        if str(n)[0] == '1':
            s = -1
        n = str(n)[1:]

    hexa = str(n[::-1])
    for i in range(len(hexa)):
        if hexa[i] in hexa_values.values():
            v = int(list(hexa_values.keys())[
                list(hexa_values.values()).index(hexa[i])])
        else:
            v = int(hexa[i])
        result += v * (16 ** i)
    return result * s


class Encryptor:
    def __init__(self, password=None, pin=None):
        '''
        ### PARAMS ###

        password:       [str]
        pin:            [int]

        ### WARNINGS ###

        If hexa is true while encrypting, hexa must be true for decrypting!
        '''
        self.password = password
        self.pin = str(pin)

    @property
    def pin_values(self):
        return [ord(i) for i in self.pin]

    @property
    def password_values(self):
        return [ord(i) for i in self.password]

    def encrypt(self, txt):
        key = self._key(len(txt))
        encrypted = []
        for i in range(len(txt)):
            letter_value = ord(txt[i])
            pass_value = ord(self.password[i % len(self.password)])

            if key[i] % 2 == 0 or pass_value % 2 == 0:
                sign = -1
            else:
                sign = 1
            encrypted.append(
                (sign * (letter_value + key[i] + pass_value) - sum(self.password_values)))

        return tuple([decimal_to_hexa(i, 1) for i in encrypted])

    def decrypt(self, enc_list):
        '''
        enc_list:    [list/tuple]
        '''
        key = self._key(len(enc_list))
        encrypted = [hexa_to_decimal(i, 1) for i in enc_list]
        decrypted = []
        for i in range(len(encrypted)):
            pass_value = ord(self.password[i % len(self.password)])

            if key[i] % 2 == 0 or pass_value % 2 == 0:
                sign = -1
            else:
                sign = 1

            letter_value = sign * (encrypted[i] + sum(self.password_values))\
                - (key[i] + pass_value)
            decrypted.append(chr(letter_value))

        return ''.join(decrypted)

    def _key(self, len_txt):
        key = []
        for i in range(1, len_txt + 1):
            x = self.password_values[i % len(self.password_values)]
            y = self.pin_values[i % len(self.pin_values)]
            if x % 2 == 0:
                key.append((x + i) * y)

            elif y % 2 == 0:
                key.append((y + i) * x)

            else:
                key.append((x + y) * i)
        return key
