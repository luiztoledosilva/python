def ano_bissexto(ano):
	if ano%4==0:
		return 'ano bissexto'
	else:
		return 'nao eh ano bissexto'
a=2024
print(ano_bissexto(a))
