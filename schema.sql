-- todo/schema.sql

-- tabela z zadaniami
DROP TABLE IF EXISTS respondent;
DROP TABLE IF EXISTS wiedza;
DROP TABLE IF EXISTS zaufanie;
DROP TABLE IF EXISTS opinia ;
DROP TABLE IF EXISTS pracaLekarza;
CREATE TABLE respondent (
    id integer primary key autoincrement,
    wiek int,
    plec boolean,
    miejscowosc text
);
CREATE TABLE wiedza (
    wiedza_id integer primary key autoincrement,
    definicja text,
    wspomaganie_decyzji boolean,
    prognozowanie boolean,
    planowanie boolean,
    analiza_obrazow boolean,
    detekcja_regularnosci boolean,
    foreign key (wiedza_id) references respondent(id)
);
CREATE TABLE zaufanie (
    zaufanie_id integer primary key autoincrement,
    monitorowanie_zdrowia boolean,
    trafnosc_diagnoza boolean,
    wykrywanie_nieprawidlowosci boolean,
    umawianie_wizyt boolean,
    foreign key (zaufanie_id) references respondent(id)
    );
CREATE TABLE opinia (
    opinia_id integer primary key autoincrement,
    precyzyjniejsza_diagnostyka text,
    rozwiniecie_sluzby_zdrowia text,
    lepsze_leczenie text,
    diagnostyka_covid text,
    diagnostyka_nowotworow_tarczycy text,
    skracanie_kolejek text,
    przyspieszanie_pracy text,
    foreign key (opinia_id) references respondent(id)
    );
