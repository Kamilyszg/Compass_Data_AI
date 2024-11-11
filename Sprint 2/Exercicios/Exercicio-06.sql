SELECT 
	DISTINCT autor.codautor, 
	autor.nome,
	COUNT(livro.publicacao) AS quantidade_publicacoes
FROM autor
LEFT JOIN livro
	ON autor.codautor = livro.autor
GROUP BY autor.codautor, autor.nome 
ORDER BY quantidade_publicacoes DESC 
LIMIT 1


	
