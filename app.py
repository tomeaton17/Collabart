from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', test='test')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.args
    print(data)
    return data

if __name__ == '__main__':
    app.run(debug='True')
