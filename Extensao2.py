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

# estrutura condicional (if... ou se...)
# se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóven ainda, xóven ainda...")

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")
print("vai ser executada de qualquer jeito")