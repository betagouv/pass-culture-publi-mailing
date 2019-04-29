import re
from mailjet_rest import Client
import os
from datetime import datetime
import requests
from mails import make_mail_test, make_mail_test2, make_sms
from gsheet import write_gsheet, read_gsheet
from pprint import pprint

## MAILS

def check_mail_regex(mail):
    if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail):    
        return False
    return True
                
def send_mails_table(table):
    a = len(table)
    statut=read_gsheet('Feuille 1!D1:D')
    date=read_gsheet('Feuille 1!G1:G')
    canal=read_gsheet('Feuille 1!F1:F')
    message_ID=read_gsheet('Feuille 1!H1:H')
    for i in range(1,a):
        print(statut[i])
        if statut[i]==['à envoyer'] and canal[i]==['Mail']:
          #print(table[i][0])  
          recipient = table[i][0]
          print(recipient)
          prenom = table[i][1]
          #print(prenom)
          message_ID[i]= send_mail_API(recipient,prenom)
          statut[i]=['envoyé']        
          date[i]= [datetime.today().strftime("%d/%m/%y %H:%M")]
    write_gsheet(statut, 'Feuille 1!D1:D')
    write_gsheet(date, 'Feuille 1!G1:G') 
    write_gsheet(message_ID, 'Feuille 1!H1:H') 
            
def send_mail(recipient, mail_maker):
    email = mail_maker

    recipients = [recipient]
    for r in recipients:
        if not check_mail_regex(r):
            return "erreur dans le mail : {}".format(r)

    email['Html-part'], email['To'] = compute_email_html_part_and_recipients(email['Html-part'], recipients)

    mail_result = Client(auth=(os.environ.get("MAILJET_API_KEY"), os.environ.get("MAILJET_API_SECRET")), version='v3').send.create(data=email)
    if check_if_email_sent(mail_result):
        return str(datetime.utcnow())
    return "n/a"
    
def send_mail_API(destinataire, prenom):
    
    destinataires = [destinataire]
    for d in destinataires :
        if not check_mail_regex(d):
            return "erreur dans le mail : {}".format(d)
    
    mailjet = Client(auth=(os.environ.get("MAILJET_API_KEY"), os.environ.get("MAILJET_API_SECRET")), version='v3.1')

    data = make_mail_test2(destinataire, prenom)
    
    result = mailjet.send.create(data=data)
    print([result.json()['Messages'][0]['To'][0]['MessageID']])
    return [result.json()['Messages'][0]['To'][0]['MessageID']]
    #if check_if_email_sent(result):
    #    return str(datetime.utcnow())
    #return "n/a"

def check_if_email_sent(mail_result):
    if mail_result.status_code != 200:
        print ("mail KO :(")
        return False
    return True

def compute_email_html_part_and_recipients(email_html_part, recipients):
    recipients_string = ", ".join(recipients)
    email_to = recipients_string
    return email_html_part, email_to

def is_mail_opened():
    endpoint = "https://api.mailjet.com/v3/REST/messageinformation/288230376948536000"
    result = requests.get(endpoint, auth=(os.environ.get("MAILJET_API_KEY"), os.environ.get("MAILJET_API_SECRET")))

    print(result)
 #   print(result.json())


## SMS

def send_sms_table(table):
    a = len(table)
    statut=read_gsheet('Feuille 1!D1:D')
    date=read_gsheet('Feuille 1!G1:G')
    message_ID = read_gsheet('Feuille 1!H1:H')
    canal=read_gsheet('Feuille 1!F1:F')
    for i in range(1,a):
        print(statut[i])
        if statut[i]==['à envoyer'] and canal[i]==['SMS']:
          #print(table[i][0])  
          numero = "+"+table[i][2]
          print(numero)
          prenom = table[i][1]
          #print(prenom)
          pprint(send_sms(numero, prenom).json())
          statut[i]=['envoyé']        
          date[i]= [datetime.today().strftime("%d/%m/%y %H:%M")]
    write_gsheet(statut, 'Feuille 1!D1:D')
    write_gsheet(date, 'Feuille 1!F1:F') 
    write_gsheet(message_ID, 'Feuille 1!G1:G') 


def send_sms(numero, prenom):
    api_token = os.environ.get('MAILJET_TOKEN')
    headers = {
        "Authorization":"Bearer {api_token}".format(api_token=api_token),
        "Content-Type": "application/json"
    }   
    endpoint = "https://api.mailjet.com/v4/sms-send"
    
    data = make_sms(numero, prenom)
    print(data)

    responses = requests.post(endpoint, headers=headers, json=data)
    return responses
    





