# pip3 install Flask
# pip3 install uwsgi

import logging
from flask import Flask, redirect, request, escape, render_template

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/')
def init():
    app.logger.info("Redirecció a /dump/")
    return redirect('/dump/')


@app.route('/dump/', methods=['POST', 'GET'])
def dump():
    app.logger.info(f"Formulari enviat des de {request.remote_addr} amb {request.method}")

    # capturo dades del formulari
    sections = list()
    sections.append(__to_html("GET", request.args))
    sections.append(__to_html("POST", request.form))
    sections.append(__to_html("COOKIES", request.cookies))
    sections.append(__to_html("FILES", request.files))
    sections.append(__to_html("HEADERS", request.headers))

    return render_template('result.html', sections = "\n".join(sections))

def __to_html(title: str, d: dict):
    html = list()
    
    html.append("<section>")
    html.append(f"<h3>{title}</h3>")
    html.append("<dl>")
    for key, value in d.items():
        html.append(f"<dt>{escape(key)}</dt>")
        html.append(f"<dd>{escape(value)}</dd>")
    html.append("</dl>")
    html.append("</section>")
    
    return "\n".join(html)

# Main per fer aixecar un servidor de proves amb logs
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
