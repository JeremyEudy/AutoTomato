import os
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__, instance_path='/home/devinmknights/web-app/instance/')
UPLOAD_FOLDER = app.root_path + '/files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']

        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], "script.txt"))
            os.system("python3 AutoTomato.py")

            return redirect("/results", code=302)

        else:
            return render_template('Autotomato_Fail.html')
    elif request.method == 'GET':
        return render_template('Autotomato.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/instance')
def instance():
    return send_from_directory(app.root_path + '/static/', "Results.csv")

if __name__ == '__main__':
  app.run(debug=True, port=80, host="0.0.0.0")
