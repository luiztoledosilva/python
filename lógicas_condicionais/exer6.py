##imc
def imc(a):
    if a<18.5:
        return 'Abaixo do peso'
    elif a>18.6 and a<=24.9:
        return 'Saudavel'
    elif a>25.0 and a<=29.9:
        return  'Peso em excesso'
    elif a>30 and a<=34.9:
        return 'Obesidade Grau 1'
    elif a>35 and a<=39.9:
        return 'Obesidade Grau 2(severa)'
    else:
        return 'Obesidade Grau 3(mórbida)'
numero=20.0
print(imc(numero))
    