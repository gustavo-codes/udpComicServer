from service import Locadora, Comic
import messages_pb2 as Message
class Skeleton:
    def __init__(self):
        self.locadora = Locadora()

    def giveComic(self,args):
        comic = Message.Comic()

        #Desempacota os argumentos recebidos
        comic.ParseFromString(args)

        #Chama o serviço
        self.locadora.giveComic(Comic(comic.name,comic.date,comic.auth,comic.price,comic.condition))

        #Nesse caso o retorno são os prórpios argumentos recebido (echo)
        return args
    
    def takeComic(self,args):
        comic = Message.Comic()
        comicId = Message.ComicId()

        #Desempacota o argumento recebido
        comicId.ParseFromString(args)
        
        #Chama o serviço
        c:Comic = self.locadora.takeComic(comicId.id)
        #Empacota os argumentos de resposta
        comic.name = c.name
        comic.date = c.date
        comic.auth = c.auth
        comic.price = c.price
        comic.condition = c.condition
        comic.status = c.status
        return comic.SerializeToString()
    
    def getComics(self,args):
        comics = Message.ComicList()

        #Desempacota o argumento recebido
        comics.ParseFromString(args)

        #Chama o serviço
        comicList = self.locadora.getComics()
        
        #Empacota os argumentos de resposta
        for c in comicList:
            comic = Message.Comic()
            comic.name = c.name
            comic.date = c.date
            comic.auth = c.auth
            comic.price = c.price
            comic.condition = c.condition
            comic.status = c.status

            comics.comics.append(comic)

        return comics.SerializeToString()