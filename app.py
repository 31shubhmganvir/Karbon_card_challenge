from flask import Flask, render_template, request, redirect, url_for
#import jsonpy
from model import probe_model_5l_profit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        content = file.read()
        data = json.loads(content)
        result = probe_model_5l_profit(data["data"])
        return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
