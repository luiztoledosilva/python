###verificar se um numero eh divisivel por 3 e 5 ao mesmo tempo

def EhDivisivel(a):
    if a%3==0 or a%5==0:
        return 'Eh divisivel por 3 ou 5'
    else:
        return 'Nao eh divisivel por nenhum ou eh divisivel por dois(3 e 5)'

numero=45

print(EhDivisivel(numero))