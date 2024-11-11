WITH mais_vendido AS (
	SELECT 
		cdpro,
		COUNT(cdven) as contagem
		FROM tbvendas 
		WHERE dtven between DATE('2014-02-03') and DATE('2018-02-02') AND status = 'Concluído'
		GROUP BY cdpro
		ORDER BY contagem DESC
)
SELECT
	tbvendas.cdpro,
	tbvendas.nmpro
FROM tbvendas 
LEFT JOIN mais_vendido
	ON tbvendas.cdpro = mais_vendido.cdpro
GROUP BY tbvendas.cdpro
LIMIT 1
