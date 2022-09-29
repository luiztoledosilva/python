###transformar quilometros por hora em metros por segundos
###k=m*3.6

###http://www.bosontreinamentos.com.br/programacao-em-python/entrada-de-dados-em-python-com-funcao-input/

####casas decimais com format abaixo:

# :~:text=Formatando%20N%C3%BAmeros%20em%20Python&text=O%20correto%20%C3%A9%20ter%20apenas,a%20forma%20como%20%C3%A9%20exibido).
##https: // www.pythonprogressivo.net/2018/02/Formatando-Numeros-Funcao-Print.html

def metrosporsegundo(kmh):
    conta=kmh*3.6;
    ##print("{} kms por segundo é equivalente a {%.2f} " format(kmh, conta))
    print("%.2f kms por hora é equivalente a %.2f metros por segundos" %(kmh,conta))
a=float(input("Digite o kms por hora: "))
metrosporsegundo(a)