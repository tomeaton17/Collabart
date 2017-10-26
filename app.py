from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
import base64, os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                      'store/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Painting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Painting %r>' % self.name

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
