from flask import request
from flask import Flask
from flask import render_template
from Respondent import Respondent

app = Flask(__name__)

respondent = Respondent()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('part1.html')

@app.route('/czesc1', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        odebrane = request.form
        respondent.wpisz_dane(odebrane)
        if odebrane.get("2") == 'Nigdy nie zetknałem sie z tym pojeciem':
            return render_template('end1.html')
        else:
            return render_template('part2.html')


@app.route('/czesc2', methods=['GET', 'POST'])
def index3():
    if request.method == 'POST':
        odebrane = request.form
        respondent.dopisz_dane(odebrane)
        respondent.wywietl_dane()
        respondent.zapis_do_bazy()
        return render_template('end2.html')

if __name__ == '__main__':
    app.run(debug=True)
