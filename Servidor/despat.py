from skeleton import Skeleton
import messages_pb2 as Message

class Despat:
    skeleton = Skeleton()
    message = Message.Message()
    def invoke(self,msg):
        try:
            #Desempacota a mensagem a fim de checar qual método do esqueleto deve chamar
            self.message.ParseFromString(msg)
            print(self.message)
            if(self.message.methodId == 'giveComic'):
                res = self.skeleton.giveComic(self.message.arguments)
            elif(self.message.methodId == 'takeComic'):
                    res = self.skeleton.takeComic(self.message.arguments)
            elif(self.message.methodId == 'getComics'):
                res = self.skeleton.getComics(self.message.arguments)
            else:
                res = "Bad Request"
            
            self.message.type = 2
        except Exception as exc:
            err = Message.Error()
            err.err = exc.args[0]
            res = err.SerializeToString()
            self.message.type = 3

        #Colocar os argumentos de resposta na mensagem
        self.message.arguments = res
        return self.message.SerializeToString()
        