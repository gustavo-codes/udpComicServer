import messages_pb2 as Message
from udpclient import *

class Proxy():
    udpclient = UDPClient()

    """
    Os métodos abaixo chamam remotamente os métodos com o mesmo nome no lado do servidor
    onde está o serviço, nesse caso a locadora.
    Todos eles têm a mesma estrutura que é
    (1) Empacota os argumentos
    (2) Chama o doOperation() passando os argumentos empacotados
    (3) Desempacota os argumentos da resposta e retorna-os
    """
    def takeComic(self,id):
        #Empacota os argumentos
        comic = Message.Comic()
        op = Message.ComicId()
        op.id = id

        #Envia os argumentos empacotados
        response = self.doOperation('locadora','takeComic',op.SerializeToString())
        comic.ParseFromString(response)

        return comic


    def giveComic(self,name,date,auth,price,condition):
        #Empacota os argumentos
        comic = Message.Comic()
        op = Message.Comic()
        op.name = name
        op.date = date
        op.auth = auth
        op.price = price
        op.condition = condition
        op.status = 0

        #Envia os argumentos empacotados
        response = self.doOperation('locadora','giveComic',op.SerializeToString())

        comic.ParseFromString(response)

        return comic
    
    def getComics(self):
        #Empacota os argumentos
        comics = Message.ComicList()
        op = Message.ComicList()
        op.filter = 1

        #Envia os argumentos empacotados
        response = self.doOperation('locadora','getComics',op.SerializeToString())
        comics.ParseFromString(response)

        return comics
    

    """
    doOperation() funciona em conjunto com os métodos pack e unpackMessage para
    empacotar a mensagem final com as informações:
    (1) Objeto remoto a ser chamado
    (2) Método desse objeto a ser chamado
    (3) Os argumentos de entrada dados pelos métodos anteriores que irão em (2)

    e depois desempacotar a mensagem recebida, mandando apenas os argumentos de resposta
    para a interface do usuário
    """
    def doOperation(self,objectRef,method,args):
        data = self.packMessage(objectRef,method,args)
        self.udpclient.sendRequest(data)
        response = self.unpackMessage(self.udpclient.getResponse())
        return response.arguments

    #Empacota a mensagem com os dados passados (1), (2) e (3)
    def packMessage(self,objectRef,method,args):
        message = Message.Message()
        message.type = 1
        message.id = 0
        message.obfReference = objectRef
        message.methodId = method
        message.arguments = args

        return message.SerializeToString()
    
    #Desempacota a mensagem de resposta do servidor
    def unpackMessage(self,response):  
        message = Message.Message()
        message.ParseFromString(response)
        
        return message

    def close(self):
        self.udpclient.close()