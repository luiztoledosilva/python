def eleitor(idade):
	if idade>=18 and idade<70:
		print("Voto obrigatório pois idade é %d " %idade)
	elif idade==16 or idade==17 or idade>70:
		print("Voto não obrigatório idade = %d "  %idade)
	else:
		print("Você não tem idade para votar, tem %d " %idade)
id=int(input("Qual a sua idade: "))
print(eleitor(id))


