SELECT 
	cdven
FROM tbvendas
WHERE deletado > 0
GROUP BY cdven 
ORDER BY cdven
