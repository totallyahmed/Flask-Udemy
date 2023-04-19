from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/result')
def result():
    dict = {'chem':60, 'bio':90, 'phy':75, 'eng':99}
    return render_template('index.html', result = dict)

if __name__ == '__main__':
    app.run(debug=True)