from pprint import pprint

from gsheet import read_gsheet
from mailjet import send_mail, send_sms
from mails import make_mail_test


def main():
    sms = {
        "Text": "Yo Florent; a priori ça fonctionne \\o/ !",
        "To": "+330000000000",
        "From": "passCulture"
    }
    pprint(send_sms(sms).json())
    # print(send_mail("romain.chaffalpassculture.app", make_mail_test()))
    # print(read_gsheet('Feuille 1!A1:B2'))

if __name__ == '__main__':
    main()