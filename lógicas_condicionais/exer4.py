###tempo de aposentadoria 

def aposentadoria(idade, tempo):
    if idade>=65 or tempo>=30:
        return "Aposentadoria concedida"
    elif idade>=60 and tempo>=25:
        return "Aposentadoria concedida"
    else:
        return "Aposentadoria nao concedida"
idade=62
tempo=27

print(aposentadoria(idade,tempo))
    
        