from flask import Flask, request, render_template, session
from Respondent import Respondent

app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
    return render_template('stronaglowna.html')


@app.route('/part1')
def index2():
    return render_template('part1.html')

@app.route('/stronaglowna')
def index3():
    return render_template('stronaglowna.html')

@app.route('/czesc1', methods=['POST'])
def czesc1():
    if request.form.get("2") == 'Nigdy nie zetknałem sie z tym pojeciem':
        respondent1 = Respondent()
        respondent1.wpisz_dane1(request.form)
        respondent1.zapis_do_bazy()
        return render_template('end1.html')
    else:
        session['form1'] = request.form
        return render_template('part2.html')

@app.route('/czesc2', methods=['POST'])
def czesc2():
    odebrane = request.form
    respondent = Respondent()
    respondent.wpisz_dane(session['form1'], odebrane)
    respondent.wywietl_dane()
    respondent.zapis_do_bazy()
    return render_template('end2.html')

if __name__ == '__main__':
    app.run(debug=True)
