from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('select.html')


@app.route('/stamp', methods=['POST'])
def stamp():
    opzione1_selezionata = request.form['opzione1']
    opzione2_selezionata = request.form['opzione2']
    return f"Hai selezionato le opzioni: {opzione1_selezionata}, {opzione2_selezionata}"


if __name__ == '__main__':
    app.run()