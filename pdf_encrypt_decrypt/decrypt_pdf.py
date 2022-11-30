from PyPDF2 import PdfFileWriter, PdfFileReader
import sys


def decrypt_pdf():
    file_path = input('Enter file path: ')
    password = input('Enter password: ')
    new_file_name = input('Enter a name for the new decrypted file: ')

    file_writer = PdfFileWriter()
    try:
        file_reader = PdfFileReader(file_path)
    except FileNotFoundError:
        print('[INFO] File not found')
        sys.exit()

    if file_reader.isEncrypted:
        file_reader.decrypt(password)

    for page in range(file_reader.numPages):
        file_writer.addPage(file_reader.getPage(page))

    with open(new_file_name, "wb") as file:
        file_writer.write(file)

    print(f'Success for creating - {new_file_name}')