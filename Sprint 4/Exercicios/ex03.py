from functools import reduce

def calcula_saldo(lancamentos)-> float:
    conversao = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    soma_lancamentos = reduce(lambda soma, lancamento: soma + lancamento, conversao, 0)
    return soma_lancamentos
    
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

resultado = calcula_saldo(lancamentos)
print(resultado)