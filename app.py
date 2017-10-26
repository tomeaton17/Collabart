from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
import base64, os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                      'store/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html', test='test')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    imgData = data['base64'].split(',')[1]
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(imgData))
    return json.dumps({'success':True}), 200,
    {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug='True')
