SELECT
	estado,
	nmpro,
	ROUND(AVG(qtd),4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro 
ORDER BY 1,2