
def make_mail_test():
    return {
        'FromName': 'Pass Culture',
        'FromEmail': 'support.passculture@beta.gouv.fr',
        'Subject': "[pass Culture pro] [TEST]",
        'Html-part': ("<p>Cher partenaire du pass Culture,</p>"
                      "<p>Ceci est un test</p>"
                      "<p>Très cordialement,</p>"
                      "<p>L’équipe du pass Culture</p>"
                      "<p>Si vous avez reçu cet e-mail par erreur, ou si vous y avez déjà répondu, merci de ne pas en tenir compte.</p>"
                      )
    }
