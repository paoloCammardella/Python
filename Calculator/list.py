lista = [3, "c", 'hello']
lista2 = ['a', 'b', 'c']

for i in range(len(lista)):
    print (lista[i])

lista.append(4)

lista[0:len(lista)] = []

for i in range(len(lista)):
    print (lista[i])

print ("ciao")

lista.insert(0, "ciao")
lista.insert(0, 4)
lista.extend(lista2)

for i in range(len(lista)):
    print (lista[i])

lista.clear()

print(len(lista))
