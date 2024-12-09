def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)

    produtos_acima_media = filter(lambda item: item[1] > media, conteudo.items())
    
    produtos_ordenados = sorted(produtos_acima_media, key=lambda item: item[1])
    
    return list(produtos_ordenados)

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

maiores_que_media(conteudo)