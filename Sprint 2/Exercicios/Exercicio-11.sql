SELECT 
	cdcli,
	nmcli,
	SUM(vrunt * qtd) AS gasto 
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdcli, nmcli
ORDER BY gasto DESC 
LIMIT 1
