from proxy import *
from datetime import datetime

proxy = Proxy()

def displayMenu():
    print("0 -- Sair")
    print("1 -- Entregar uma comic")
    print("2 -- Pegar uma comic")
    print("3 -- Ver todas as comics")
  
operation = -1

while operation != 0:

    displayMenu()

    try:
        operation = int(input("Qual opção? "))
    except:
        print("Erro: A opção deve ser um número inteiro válido.")
        continue  # Retorna ao início do loop

    if operation == 0:
        proxy.close()

    elif operation == 1:
        try:
            # Coleta e valida os dados de entrada
            name = input("Nome: ").strip()
            if not name:
                raise ValueError("O nome não pode estar vazio.")

            date = input("Data (DD-MM-AAAA): ").strip()
            from datetime import datetime
            datetime.strptime(date, "%d-%m-%Y")  # Validação de formato

            auth = input("Autor: ").strip()
            if not auth:
                raise ValueError("O autor não pode estar vazio.")

            
            price_string = input("Preço: ")

            if not price_string.replace(".", "", 1).isdigit():
                raise ValueError("O preço deve ser um valor numérico.")
            
            price = float(price_string)
            if price < 0:
                raise ValueError("O preço não pode ser negativo.")

            condition = int(input("Condição (0-3): "))
            if condition not in range(0, 4):
                raise ValueError("A condição deve estar entre 0 e 3.")

            # Se todas as validações passaram, executa a 

        
            comic:Comic = Comic(name, date, auth, price, condition)
            returnedComic = proxy.giveComic(comic)

            if returnedComic.tittle == "Timeout": 
                print("Não foi possível falar com o servidor!")
            else:
                returnedComic.display()

        except ValueError as e:
            print(f"Erro: {e}")

    elif operation == 2:
        try:
            id = int(input("Qual o id da comic? "))
            comic = proxy.takeComic(id)

            comic = proxy.takeComic(id)

            if comic == "Timeout":
                print("Operação demorou muito. Tente novamente.")
            else:
                print("Quadrinho recebido:", comic)
        except ValueError:
            print("Erro: O ID deve ser um número inteiro válido.")

    elif operation == 3:
        comics = proxy.getComics()

        if comics == "Timeout":
            print("Não foi possível falar com o servidor!")
            
        else:
            for index, c in enumerate(comics):
                print(f"id: {index}")
                c.display()
                print() 