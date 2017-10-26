from flask import Flask, render_template, request, json
import base64, sqlite3
app = Flask(__name__)

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
