CREATE TABLE datorii(
    id INTEGER PRIMARY KEY,
    nume_datorie TEXT NOT NULL,
    valoare_datorie INTEGER,
    datorie_incheiata BOOLEAN,
    data_creare_datorie DATETIME,
    data_incheiere_datorie DATETIME
);