# #Booleanos
# # print(1>0)
# # print(1<0)
# # print(bool("ola"))
# # print(bool(1<0))
# # print(bool(0))
# # print("A lista retorna:")
# # print(bool(["maça","pera"]))

# # print(bool(False))
# # print(bool(None))
# # print(bool(""))
# # print(bool([]))

# # operatodaores aritemitocos
# # + adição
# print(4+2)
# # - subtração
# print(4-2)
# # * multiplicação
# print(4*2)
# # / divisao
# print(4/3)
# # % modulo
# print(4%3)
# # ** exponencial 2^23 = 2**23
# print(4**3) # 4*4*4
# # // floor divison
# print(4//3)

# print("#####################")

# # operatodes de assignação
# # =
# variavel = 3
# print(variavel)
# # +=
# variavel += 3 # variavel = variavel + 3
# print(variavel)
# # -=
# variavel -= 1 # variavel = variavel - 3
# print(variavel)
# # *=
# variavel *= 2
# print(variavel)

# print("############################")
# #operadores de comparação

# # ==
# print( 8 == 9)
# # != not equal
# print( 8 != 9)
# # >
# print (8 > 9)
# # <
# print (8 < 9)
# # >=
# print (8 >= 9)
# # <=
# print (8 <= 9)
 

# print("############################")
# # operadores logicos

# # and   T          T 
# print( 8 > 0 and 8 < 9)
# # or 
# print( 8 > 10 or 1 < 9)
# # not
# print( not(8 > 10) )

# ###  Listas
lista = ["apple","banana","banana","outra coisa","carro","perna",1,True,"outro elemento"]
# print(type(lista))

# nova_lista = list(('valo2','valor3','valor4'))
# print(type(nova_lista))

# print(lista[1:3])
# print(lista[:4])
# print(lista[1:])
# print(lista[0:])

# print("carro" in lista)
# print("mota" in lista)
##### modificar a lista
# lista[0] = "maçã"
# print(lista)
# lista[2:6] = ["pera","kiwi","pessego","morango"]
# print(lista)
# # lista[1:] = ["tangerina"]
# # print(lista)
# lista.append("amora")
# print(lista)

# lista.insert(3,"franbroesa")
# print(lista)
# outralista = ["tangeria","tomate"]
# lista.extend(outralista)
# print(lista)

# isto_e_um_set = ("cenoura","os")
# lista.extend(isto_e_um_set)
# print(lista)

# lista.remove("banana")
# print(lista)
# lista.pop(3)
# print(lista)
# lista.pop()
# print(lista)
# del lista[2]
# print(lista)
# lista.clear()
# print(lista)

for x in lista:
    print(x)


tamanho = len(lista)
print(tamanho)
#range(numero) []
# print("#####")
# for i in range(tamanho):
#     print(lista[i])


# for x in range(tamanho):
#     print(lista[x])
print("WHILE")
posicao = 0
while posicao < tamanho: # true
    print(lista[posicao]) # lista[0]
    posicao = posicao + 1 # 1  + 1  = 0