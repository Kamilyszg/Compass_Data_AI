SELECT 
	COUNT(livro.cod) AS quantidade,
    editora.nome, 
    ende.estado,
    ende.cidade
FROM editora
LEFT JOIN livro 
    ON editora.codeditora = livro.editora
LEFT JOIN endereco AS ende 
    ON editora.endereco = ende.codendereco
GROUP BY editora.nome, ende.estado, ende.cidade
HAVING COUNT(livro.cod) > 0
ORDER BY quantidade DESC

