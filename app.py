from pprint import pprint
import random
from gsheet import read_gsheet, write_gsheet
from mailjet import send_mail, send_sms_table, send_mails_table, send_mail_API, is_mail_opened
from mails import make_mail_test, make_sms
from datetime import datetime, timedelta, time

from statuts import futur_status

def main():
   
#UPDATE STATUS
    futur_status()
    
#SEND MAIL
    #print(send_mails_table(read_gsheet('Feuille 1!A1:D')))
    
# SEND SMS
    #print(send_sms_table(read_gsheet('Feuille 1!A1:D')))

# CHECK IF MAILS READ
    # A VENIR

  
if __name__ == '__main__':
    main()