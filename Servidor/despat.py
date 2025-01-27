from skeleton import Skeleton
import messages_pb2 as Message

class Despat:
    skeleton = Skeleton()
    message = Message.Message()
    def invoke(self,msg):
        #Desempacota a mensagem a fim de checar qual método do esqueleto deve chamar
        self.message.ParseFromString(msg)
        print(self.message)
        if(self.message.methodId == 'giveComic'):
            res = self.skeleton.giveComic(self.message.arguments)
        elif(self.message.methodId == 'takeComic'):
            try:
                res = self.skeleton.takeComic(self.message.arguments)
            except Exception as exc:
                res = exc.args
        elif(self.message.methodId == 'getComics'):
            res = self.skeleton.getComics(self.message.arguments)
        else:
            res = "Bad Request"

        #Colocar os argumentos de resposta na mensagem
        self.message.arguments = res
        self.message.type = 2
        return self.message.SerializeToString()
        