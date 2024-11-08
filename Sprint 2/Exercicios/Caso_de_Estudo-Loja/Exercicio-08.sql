WITH agrupamento AS(
	SELECT
		cdvdd,
		COUNT(cdven) as contagem
	FROM tbvendas t 
	WHERE status = 'Concluído'
	GROUP BY cdvdd
	ORDER BY contagem
)
SELECT
	tbvendedor.cdvdd,
	tbvendedor.nmvdd 
FROM tbvendedor
LEFT JOIN agrupamento
	ON tbvendedor.cdvdd = agrupamento.cdvdd
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd 
ORDER BY agrupamento.contagem DESC
LIMIT 1