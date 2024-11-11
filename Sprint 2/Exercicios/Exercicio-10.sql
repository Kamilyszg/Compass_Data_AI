SELECT 
	tbvendedor.nmvdd AS vendedor,
	SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
	ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao/100,2) as comissao
FROM tbvendas 
LEFT JOIN tbvendedor 
	ON tbvendas.cdvdd = tbvendedor.cdvdd 
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.nmvdd
ORDER BY comissao DESC




