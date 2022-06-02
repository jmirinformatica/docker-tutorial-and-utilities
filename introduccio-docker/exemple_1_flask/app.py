#pip3 install Flask

from flask import Flask
app = Flask(__name__)

UPLOAD_FOLDER = './static/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

import os
from flask import Flask, redirect, url_for, request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():

    image_tags = list()
    for file_name in os.listdir(UPLOAD_FOLDER):
        image_tags.append(f"<div><img src='{UPLOAD_FOLDER + file_name}'></div>")

    return f"""
<html>
<head><title>Prova de flask</title></head>
<body>
{''.join(image_tags)}
<form method="post" action="/" enctype="multipart/form-data">
    <dl>
        <p>
            <input type="file" name="file" autocomplete="off" required>
        </p>
    </dl>
    <p>
        <input type="submit" value="Submit">
    </p>
</form>
</body>
"""

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        print("Error: no file part")
    else:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            print(f"Error. Invalid filename: {file.filename}")

    return redirect(request.url)

#https://roytuts.com/upload-and-display-image-using-python-flask/
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80, debug = True)