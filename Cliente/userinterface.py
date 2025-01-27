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
        condition = int(input("condicao (0-3): "))

        proxy.giveComic(name,date,auth,price,condition).display()

    if operation == 2:
        id = int(input("Qual o id da comic?"))

        proxy.takeComic(id).display()


    if operation == 3:
        for index,c in enumerate(proxy.getComics()):
            print(f"id: {index}")
            c.display()
            print()