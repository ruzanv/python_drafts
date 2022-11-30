from encrypt import encrypt_pdf
from decrypt import decrypt_pdf


def choose_encrypt_decrypt():
    choose = input('Enter 0 to encrypt the file, enter 1 to decrypt: ')
    if choose == 0:
        encrypt_pdf()
    elif choose == 1:
        decrypt_pdf()
    else:
        print('Incorrect value')
