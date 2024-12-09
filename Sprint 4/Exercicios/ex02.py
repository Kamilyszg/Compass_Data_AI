def conta_vogais(texto:str)-> int:
    vogais = filter(lambda i: i in 'aeiouAEIOU', texto)
    contagem = len(list(vogais))
    return contagem
                       
texto = 'Hello word!'            
resultado = conta_vogais(texto)            
print(resultado)