
contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 # contador += 1

# Laço for {python for = for each}
fruta = "morango"
print (fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

# Lista {entre colchetes}
frutas = ["morango", "laranja", "pêra"]

# quero exibir apenas a 3a. fruta {pêra}
print(frutas[2])
print(frutas[1])

# Exibir quantas frutas tem na minha lista
print(len(frutas)) # length = tamanho

#colocar 4a fruta
frutas.append("manga")
print(frutas[3])

print("Exemplo das frutas com while...")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for f in frutas:
  print(f)
