from proxy import *

proxy = Proxy()

def displayMenu():
    print("1 -- Entregar uma comic")
    print("2 -- Pegar uma comic")
    print("3 -- Ver todas as comics")
    print("0 -- Sair")

operation = -1

while operation != 0:

    displayMenu()
    operation = int(input("Qual opção? "))

    if operation == 0:
        proxy.close()

    if operation == 1:
        name = input("nome: ")
        date = input("data: ")
        auth = input("autor: ")
        price = float(input("preco: "))
        condition = int(input("condicao (0-5): "))

        print(proxy.giveComic(name,date,auth,price,condition))

    if operation == 2:
        id = int(input("Qual o id da comic?"))

        print(proxy.takeComic(id))


    if operation == 3:
        print(proxy.getComics())