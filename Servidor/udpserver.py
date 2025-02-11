from socket import *
from despat import Despat
import random

#Fazer aqui o tratamento de mensagem duplicada

class UDPServer:
    def __init__(self,ip,port):
        self.despat = Despat()
        self.ip = ip
        self.port = port
        self.Socket = socket(AF_INET,SOCK_DGRAM)
        self.Socket.bind(('',50007))

        while 1:
            data, addr = self.Socket.recvfrom(1024)
            
            print('Connected to: ')
            print(addr)
            
            """
            Tratatamento de falha

            """
            if random.randint(0, 2) > 0: #Simula pacotes perdidos
                self.sendResponse(self.getRequest(data),addr)
            

            

    def getRequest(self,req):
        return self.despat.invoke(req)
    def sendResponse(self,res,addr):
        self.Socket.sendto(res,addr)
server = UDPServer('127.0.0.1',50007)