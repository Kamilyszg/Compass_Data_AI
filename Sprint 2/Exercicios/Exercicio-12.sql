SELECT
	tbdependente.cddep,
	tbdependente.nmdep,
	tbdependente.dtnasc,
	SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas
FROM tbvendas
LEFT JOIN tbvendedor
	ON tbvendas.cdvdd =  tbvendedor.cdvdd
INNER JOIN tbdependente
	ON tbvendedor.cdvdd = tbdependente.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
HAVING valor_total_vendas > 0
ORDER BY valor_total_vendas
LIMIT 1  