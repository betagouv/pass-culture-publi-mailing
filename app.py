from gsheet import read_gsheet
from mailjet import send_mail
from mails import make_mail_test

def main():
    print(send_mail("romain.chaffalpassculture.app", make_mail_test()))
    print(read_gsheet('Feuille 1!A1:B2'))

if __name__ == '__main__':
    main()