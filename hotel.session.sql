WITH agenzie_per_citta AS(
    SELECT Citta_Indirizzo, COUNT(*) AS NAgenzie
    FROM agenzia
    GROUP BY Citta_Indirizzo
)
SELECT Citta_Indirizzo
FROM agenzie_per_citta
WHERE NAgenzie = (SELECT MAX(NAgenzie)
                  FROM agenzie_per_citta);

SELECT Latitudine, Longitudine FROM citta, agenzia WHERE citta.Nome=agenzia.Citta_Indirizzo;