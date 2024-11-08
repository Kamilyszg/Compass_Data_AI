SELECT DISTINCT  
	autor.nome
FROM autor
LEFT JOIN livro
	ON autor.codautor = livro.autor
GROUP BY autor.nome 
HAVING COUNT(livro.publicacao) = 0
ORDER BY COUNT(livro.publicacao) DESC 


	
