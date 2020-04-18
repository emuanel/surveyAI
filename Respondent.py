import sqlite3
class Respondent():
    wiek = ""
    plec = ""
    miejscowosc = ""
    definicja = ""
    wspomaganie_decyzji = ""
    prognozowanie = ""
    planowanie = ""
    analiza_obrazow = ""
    detekcja_regularnosci = ""
    monitorowanie_zdrowia = ""
    trafnosc_diagnoza = ""
    wykrywanie_nieprawidlowosci = ""
    umawianie_wizyt = ""
    precyzyjniejsza_diagnostyka = ""
    rozwiniecie_sluzby_zdrowia = ""
    lepsze_leczenie = ""
    diagnostyka_covid = ""
    diagnostyka_nowotworow_tarczycy = ""
    skracanie_kolejek = ""
    przyspieszanie_pracy = ""

    def wpisz_dane(self, dane, dane2):
        self.wiek = dane.get("wiek")
        self.plec = dane.get("0")
        self.miejscowosc = dane.get("1")
        self.definicja = dane.get("2")
        self.wspomaganie_decyzji = dane2.get("3")
        self.prognozowanie = dane2.get("4")
        self.planowanie = dane2.get("5")
        self.analiza_obrazow = dane2.get("6")
        self.detekcja_regularnosci = dane2.get("7")
        self.monitorowanie_zdrowia = dane2.get("8")
        self.trafnosc_diagnoza = dane2.get("9")
        self.wykrywanie_nieprawidlowosci = dane2.get("10")
        self.umawianie_wizyt = dane2.get("11")
        self.precyzyjniejsza_diagnostyka = dane2.get("12")
        self.rozwiniecie_sluzby_zdrowia = dane2.get("13")
        self.lepsze_leczenie = dane2.get("14")
        self.diagnostyka_covid = dane2.get("15")
        self.diagnostyka_nowotworow_tarczycy = dane2.get("16")
        self.skracanie_kolejek = dane2.get("17")
        self.przyspieszanie_pracy = dane2.get("18")

    def wywietl_dane(self):
        print(self.wiek, self.plec, self.miejscowosc, self.definicja, self.wspomaganie_decyzji, self.prognozowanie, self.planowanie, self.analiza_obrazow, self.detekcja_regularnosci, self.monitorowanie_zdrowia, self.trafnosc_diagnoza, self.wykrywanie_nieprawidlowosci, self.umawianie_wizyt, self.precyzyjniejsza_diagnostyka, self.rozwiniecie_sluzby_zdrowia, self.lepsze_leczenie, self.diagnostyka_covid, self.diagnostyka_nowotworow_tarczycy, self.skracanie_kolejek, self.przyspieszanie_pracy)

    def zapis_do_bazy(self):
        con = sqlite3.connect('wyniki.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('INSERT INTO respondent VALUES(NULL, ?, ?, ?);', (self.wiek, self.plec, self.miejscowosc))
        cur.execute('INSERT INTO wiedza VALUES(NULL, ?, ?, ?, ?, ?, ?);', (self.definicja, self.wspomaganie_decyzji, self.prognozowanie, self.planowanie, self.analiza_obrazow,self.detekcja_regularnosci))
        cur.execute('INSERT INTO zaufanie VALUES(NULL, ?, ?, ?, ?);', (self.monitorowanie_zdrowia, self.trafnosc_diagnoza, self.wykrywanie_nieprawidlowosci, self.umawianie_wizyt))
        cur.execute('INSERT INTO opinia VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);', (self.precyzyjniejsza_diagnostyka, self.rozwiniecie_sluzby_zdrowia, self.lepsze_leczenie, self.diagnostyka_covid, self.diagnostyka_nowotworow_tarczycy, self.skracanie_kolejek, self.przyspieszanie_pracy))
        con.commit()
        cur.close()


