from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', test='test')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)
    return json.dumps({'success':True}), 200,
    {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug='True')
