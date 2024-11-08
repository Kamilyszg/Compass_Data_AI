SELECT
	editora.codeditora AS CodEditora,
	editora.nome AS NomeEditora,
	COUNT(livro.editora) AS QuantidadeLivros
FROM editora
LEFT JOIN livro
	ON livro.editora = editora.codeditora
GROUP BY editora.codeditora, editora.nome
HAVING QuantidadeLivros > 0
ORDER BY QuantidadeLivros DESC
LIMIT 5


	