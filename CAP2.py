import math

# 1
#nome = input("Digite seu nome: ")
#print(nome.upper())
#print(nome.lower())
#print("Seu nome tem", len(nome), "letras.")

#modNome = nome.split()
#modNome[-1] = "do Inatel"
#print(" ".join(modNome))

#2
#num = input("Escolha um número para ditar a tabuada: ")
#limite = input("Até que número deseja esta tabuada: ")
#for i in range(1, int(limite)+1):
#    print(int(num)*int(i))

#3
#sexo = input("Digite seu sexo: ")

#while sexo != "M" and sexo != "F":
#    print("Inválido, digite 'M'  ou 'F'.")
#    sexo = input("Digite seu sexo: ")

#if sexo=="M":
#    print("Homem")

#if sexo=="F":
#    print("Mulher")

#4
#distancia = input("Qual a distancia da viagem em km: ")
#if int(distancia)<=200:
#    print("Valor :", int(distancia)*0.5)
#else:
#    print("Valor :", int(distancia)*0.45)

#5
#numero = int(input("Digite um número entre 1000 e 9999: "))

#if 1000 <= numero <= 9999:
#    milhar = numero // 1000
#    centena = (numero // 100) % 10
#    dezena = (numero // 10) % 10
#    unidade = numero % 10
    
#    print("Milhar: ", milhar)
#    print("Centena: ", centena)
#    print("Dezena: ", dezena)
#    print("Unidade: ", unidade)
#else:
#    print("Digite um número entre 1000 e 9999: ")

#6
numero = float(input("Digite um numero decimal: "))

print("Raiz quadrada: ", math.sqrt(numero))
print("Teto: ",math.ceil(numero))
print("Chão: ",math.floor(numero))
print("Parte inteira: ",int(numero))