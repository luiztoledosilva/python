soma=0
cont=0
media=0
for i in range(1,11):
    num=float(input("Digite um numero: "))
    if num>=0:
        cont +=1
        soma +=num
        media=soma/cont
print("Media = %.2f " %media)