import sqlite3

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash
from flask import Flask, g
from flask import render_template
from werkzeug.datastructures import ImmutableMultiDict
import os
from Respondent import Respondent

app = Flask(__name__)

import sqlite3

respondent = Respondent()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        odebrane = request.form
        if len(odebrane.getlist("wiek"))==1:
            respondent.wpisz_dane(odebrane)
            if odebrane.get("2") == 'Nigdy nie zetknałem sie z tym pojeciem':
                return render_template('index3.html')
            else:
                return render_template('index2.html')
        else:
            odebrane2 = request.form
            respondent.dopisz_dane(odebrane2)
            respondent.wywietl_dane()
            respondent.zapis_do_bazy()
            return render_template('index4.html')


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
