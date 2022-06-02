# pip3 install flask
# pip3 install lxml
# pip3 install uwsgi

from flask import Flask, redirect, request, render_template
from lxml import etree
from io import StringIO
import logging
from enum import IntEnum, unique

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

class ValidationState:

    def __init__(self):
        self.__state = "init"
        self.__msgs = list()

    def is_init(self):
        return self.__state == "init"

    def name(self):
        return self.__state;

    def msgs(self):
        return self.__msgs;

    def __change_state(self, new_state: str, msgs: list):
        assert self.is_init(), "ValidatorMsg is not in init"
        self.__state = new_state
        self.__msgs.extend(msgs)

    def success(self, msg: str):
        self.__change_state("success", [msg])

    def warning(self, msgs: list):
        self.__change_state("warning", msgs)

    def error(self, msgs: list):
        self.__change_state("error", msgs)


@app.route('/')
def init():
    app.logger.info("Redirecció a /validador/")
    return redirect('/validador/')


@app.route('/validador/')
def show_form():
    # mostro la pantalla sense cap dada, cap error i amb DTD com a opció seleccionada
    app.logger.info(
        f"Entrada al formulari de validació des de {request.remote_addr}")
    return render_template('formulari.html', state=ValidationState(), xml="", validator="", validator_type="DTD")


@app.route('/validador/', methods=['POST'])
def upload_xmls():
    app.logger.info(f"Upload de dades des de {request.remote_addr}")

    # capturo dades del formulari
    formulari = request.form
    xml = formulari["xml"]
    app.logger.info(f"xml: {xml}")

    validator = formulari["validator"]
    app.logger.info(f"validator: {validator}")

    validator_type = formulari["validator_type"]
    app.logger.info(f"validator_type: {validator_type}")

    state = ValidationState()
    try:
        xml_loaded = __parse_xml(xml)
    except etree.LxmlError as e:
        state.error([f"XML / Error de format: {e}"])

    if state.is_init():
        if validator_type == "DTD":
            __validate_dtd(state=state, xml_loaded=xml_loaded, dtd=validator)
        else:
            __validate_xsd(state=state, xml_loaded=xml_loaded, xsd=validator)

    return render_template('formulari.html', state=state, xml=xml, validator=validator, validator_type=validator_type)

def __validate_dtd(state, xml_loaded, dtd):
    try:
        dtd_loaded = etree.DTD(StringIO(dtd))
    except etree.LxmlError as e:
        state.error([f"DTD / Error de format: {e}"])
        return;

    if dtd_loaded.validate(xml_loaded):
        state.success("XML vàlidat amb DTD")
    else:
        state.warning([str(log) for log in dtd_loaded.error_log.filter_from_errors()])

    return;

def __validate_xsd(state, xml_loaded, xsd):

    try:
        xsd_loaded = etree.XMLSchema(__parse_xml(xsd))
    except etree.LxmlError as e:
        state.error([f"XSD / Error de format: {e}"])
        return;

    if xsd_loaded.validate(xml_loaded):
        state.success("XML vàlidat amb XSD")
    else:
        state.warning([str(log) for log in xsd_loaded.error_log.filter_from_errors()])

    return;

def __parse_xml(xml):
    # per evitar un error de codificació si l'XML té un paràmetre d'encoding
    # https://stackoverflow.com/a/59215281
    return etree.XML(xml.encode())


# Main per fer aixecar un servidor de proves amb logs
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
