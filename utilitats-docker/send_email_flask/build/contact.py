# pip3 install Flask
# pip3 install uwsgi

import logging
from mailer import envia_email
from flask import Flask, redirect, request

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/')
def init():
    print("Redirecció a /contact/")
    return redirect('/contact/')

@app.route('/contact/', methods=['GET'])
def confirmation():
    return "<p>Gràcies per posar-vos en contacte amb nosaltres. En breu tindreu resposta</p>"

@app.route('/contact/', methods=['POST'])
def contact():
    # capturo dades del formulari
    formulari = request.form

    nom_client = formulari["nom_client"]
    email_client = formulari["email_client"]
    subject = formulari["subject"]
    message = formulari["message"]

    email_botiga = formulari["email_botiga"]
    titol = f"MISSATGE DE {email_client}"
    cos = f"NOM: {nom_client}\nEMAIL:{email_client}\nSUBJECT: {subject}\nMESSAGE: {message}"

    envia_email(
        email_destinatari = email_botiga,
        titol = titol,
        cos = cos
    )

    confirmacio = formulari.get("confirmacio", "/contact/")
    print(f"Redirigint a {confirmacio}")

    return redirect(confirmacio, code=303)

# Main per fer aixecar un servidor de proves amb logs
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
