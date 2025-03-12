import numpy as np

dataset = np.loadtxt("space.csv",delimiter=  ';',dtype=str, encoding='utf-8')

#1
print("QUESTAO 1)")

print(dataset[1:,7][dataset[1:,7]=="Success"].size, "Success")
print(dataset[1:,7].size, "Total")
print(f"Success rate: {dataset[1:,7][dataset[1:,7]=='Success'].size/dataset[1:,7].size*100:.2f}%")
print()

#2
print("QUESTAO 2)")
prices = dataset[1:, 6].astype(float)
cond = prices > 0
print(f"Média de : {prices[cond].mean():.2f} zilhões de dólares")
print()

#3
print("QUESTAO 3)")
arr = dataset[1:,1]
print(arr[np.char.find(dataset[1:,2], 'USA' )>=0].size)
print()

#4
print("QUESTAO 4)")
print(f"O maior custo da SpaceX foi de : {prices[dataset[1:,1]=="SpaceX"].max()} zilhões de dólares")
print()


#5
print("QUESTAO 5)")
nomes = np.unique(dataset[1:,1])
for nome in nomes:
    print(f"{nome} tem {dataset[1:,1][dataset[1:,1]==nome].size} missões")
print()   

