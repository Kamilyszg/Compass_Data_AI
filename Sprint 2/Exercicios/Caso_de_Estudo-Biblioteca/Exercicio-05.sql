SELECT DISTINCT 
	autor.nome
FROM autor
LEFT JOIN livro
	ON autor.codautor = livro.autor
LEFT JOIN editora 	
	ON livro.editora = editora.codeditora 
LEFT JOIN endereco
	ON editora.endereco = endereco.codendereco 
WHERE endereco.estado not in ('PARANÁ', 'RIO GRANDE DO SUL')
ORDER BY autor.nome
	
