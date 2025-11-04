from flask import Flask, request, render_template_string, redirect
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

HTML_FORM = '''
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Bild-Upload</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 50px; }
    input[type=file] { margin: 20px 0; }
    input[type=submit] {
      background-color: #28a745; color: white; padding: 10px 20px;
      border: none; border-radius: 5px; font-size: 16px; cursor: pointer;
    }
    input[type=submit]:hover { background-color: #218838; }
  </style>
</head>
<body>
  <h1>📤 Bild hochladen</h1>
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="file" required><br>
    <input type="submit" value="Jetzt hochladen">
  </form>
</body>
</html>
'''

SUCCESS_PAGE = '''
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Upload erfolgreich</title>
  <style>
    body { font-family: Arial; text-align: center; margin-top: 50px; }
    a {
      display: inline-block; margin-top: 20px; text-decoration: none;
      background-color: #007bff; color: white; padding: 10px 20px;
      border-radius: 5px;
    }
    a:hover { background-color: #0056b3; }
  </style>
</head>
<body>
  <h1>✅ Datei erfolgreich hochgeladen</h1>
  <p><strong>{{ filename }}</strong></p>
  <a href="/">Zurück zur Upload-Seite</a>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template_string(SUCCESS_PAGE, filename=filename)
        return '❌ Ungültige Datei'
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)