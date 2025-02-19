# 1
print("EX 1")
print()
times = ['Corinthians', 'Grêmio', 'Cruzeiro', 'Atlético-MG', 'Barcelona']

print("Top 3 colocados: ", times[:3])

print("Últimos 2 colocados: ", times[-2:])

print(f"Times em ordem alfabética: ", sorted(times))


print("O Barcelona está na posição: ", times.index('Barcelona') + 1)


print()
#2
print("EX 2")
print()

loja1 = {'iPhone', 'Samsung Galaxy', 'Nokia', 'Motorola'}
loja2 = {'Samsung Galaxy', 'Xiaomi', 'Motorola', 'OnePlus'}



print("Modelos disponíveis na loja 1: ", loja1)
print("Modelos disponíveis na loja 2: ", loja2)
print("Modelos disponíveis em ambas as lojas: ", loja1.intersection(loja2))
print("Modelos disponíveis no total: ", loja1.union(loja2))


print()
#3
print("EX 3")
print()

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

aluno = {'nome': nome, 'média': media}

if media >= 50:
    aluno['situação'] = 'AP'
else:
    aluno['situação'] = 'RP'

print(aluno)


print()
#4
print("EX 4")
print()

pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    peso = float(input(f"Digite o peso da {i+1} pessoa: "))
    pessoas.append({'nome': nome, 'peso': peso})

for i in range(3):
    if i == 0:
        maisPesada = pessoas[i]
        maisLeve = pessoas[i]
    elif pessoas[i]['peso'] > maisPesada['peso']:
        maisPesada = pessoas[i]
    elif pessoas[i]['peso'] < maisLeve['peso']:
        maisLeve = pessoas[i]


print("A pessoa mais pesada é ", maisPesada['nome'])
print("A pessoa mais leve é ", maisLeve['nome'])


print()
#5
print("EX 5")
print()

n = int(input("Quantas pessoas você quer cadastrar? "))
pessoas = []

for i in range(n):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    idade = int(input(f"Digite a idade da {i+1} pessoa: "))
    sexo = input(f"Digite o sexo da {i+1} pessoa (M/F): ").upper()
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

mediaIdade = sum(p['idade'] for p in pessoas) / n

print("A média de idade do grupo é: ",mediaIdade," anos.")

mulheresMenos20 = sum(1 for p in pessoas if p['sexo'] == 'F' and p['idade'] < 20)
print("Existem ", mulheresMenos20, " mulheres com menos de 20 anos.")

