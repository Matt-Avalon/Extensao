# comando input(): quero permitir que o usuário digite algo...
nome = input ("Digite o seu nome: ")
# comando de saída... exibir na tela: print (nome)

# f para colocar variáveis numa frase
# errado: print ("Boa noite, seu nome é {nome}") 
# certo
print (f"Boa noite, seu nome é {nome}")

# pede idade (colocar int antes para a variável ser inteira/numérica)
idade = int(input("Qual a sua idade?: "))
print (f"Você tem {idade} anos")

# e se eu quisesse mostrar o dobro da idade informada
dobro = idade * 2
print(f"O dobro da sua idade é: {dobro} anos")