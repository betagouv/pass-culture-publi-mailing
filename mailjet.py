import re
from mailjet_rest import Client
import os
from datetime import datetime
import requests

def check_mail_regex(mail):
    if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mail):    
        return False
    return True


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


def check_if_email_sent(mail_result):
    if mail_result.status_code != 200:
        print ("mail KO :(")
        return False
    return True


def compute_email_html_part_and_recipients(email_html_part, recipients):
    recipients_string = ", ".join(recipients)
    email_to = recipients_string
    return email_html_part, email_to


def send_sms(data):
    api_token = os.environ.get('MAILJET_TOKEN')
    headers = {
        "Authorization":"Bearer {api_token}".format(api_token=api_token),
        "Content-Type": "application/json"
    }   
    endpoint = "https://api.mailjet.com/v4/sms-send"

    responses = requests.post(endpoint, headers=headers, json=data)
    return responses


