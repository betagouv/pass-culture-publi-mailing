#### MODELES DE MAILS

def make_mail_test(prenom):
    return {
        'FromName': 'Pass Culture',
        'FromEmail': 'support.passculture@beta.gouv.fr',
        'Subject': "[pass Culture pro]",
        'Html-part': (  
                      "<p>Bonjour {prenom},</p>"
                      "<p><strong>Ceci est un test</p></strong>"
                      "<p>Très cordialement,</p>"
                      "<p>L’équipe du pass Culture</p>"
                      "<p>Si vous avez reçu cet e-mail par erreur, ou si vous y avez déjà répondu, merci de ne pas en tenir compte.</p>"
                      ).format(prenom=prenom),
        'Mj-TemplateID' : '778900',
        'TemplateLanguage' : True,
        'Variables': {
            prenom: 'Florent',
            }
    }
    
def make_mail_test2(destinataire, prenom):
    return {
        'Messages': [
		    {
			    "From": {
				    "Email": "support.passculture@beta.gouv.fr",
				    "Name": "pass Culture"
			    },
			    "To": [
				    {
					    "Email": destinataire,
				        "Name": ""
				    }
			    ],
			    "TemplateID": 778900,
			    "TemplateLanguage": True,
			    "Subject": "Hello",
			    "Variables": {
                    "prenom": prenom
                }
		    }
	    ]
            
    }
    
## MODELES DE SMS    

def make_sms(numero, prenom):
    return {
         "Text": ("{prenom}, votre prochaine sortie pass Culture arrive à grands pas : retrouvez la directement dans votre appli !").format(prenom=prenom),
         "To": numero,
         "From": "passCulture"
    }
    