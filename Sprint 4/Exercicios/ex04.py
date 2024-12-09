def calcular_valor_maximo(operadores,operandos):
    juntos = zip(operadores,operandos)
    calculo = map(lambda x: x[1][0] + x[1][1] if x[0] == '+'
                    else x[1][0] - x[1][1] if x[0] == '-'
                    else x[1][0] / x[1][1] if x[0] == '/'
                    else x[1][0] * x[1][1] if x[0] == '*'
                    else x[1][0] % x[1][1] if x[0] == '%' else 0, 
                    juntos
    )
    return max(calculo)
    
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)