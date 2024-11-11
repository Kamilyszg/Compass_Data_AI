SELECT 
	cdpro,
	nmcanalvendas,
	nmpro,
	SUM(qtd) AS quantidade_vendas
FROM tbvendas
WHERE nmcanalvendas IN ('Ecommerce', 'Matriz') AND status = 'Concluído'
GROUP BY cdpro, nmcanalvendas, nmpro 
ORDER BY quantidade_vendas
