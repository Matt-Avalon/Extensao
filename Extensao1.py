# Meu primeiro Python!!!
#
# print() = comando de saida
print("Alo mundo!")

# Quando quiser guardar uma String! (frase)
nome = "Vinicius Lotto"
#Quando quiser guardar um número inteirp
idade = 19

#Exibir o meu nome (que está dentro da variável nome)
print(nome)

#Quando quiser exibir a frase "Minha idade é " completando com o conteúdo da variável idade
#print("Minha idade é "+idade)
print("Minha idade é "+str(idade))
print(f"Minha idade é {idade}")
print("Minha idade é {}".format(idade))

#Quando quiser exibir "Meu nome é ... e tenho ... anos..." trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))