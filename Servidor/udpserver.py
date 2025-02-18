from socket import *
from despat import Despat
import random
import messages_pb2

#Fazer aqui o tratamento de mensagem duplicada

class UDPServer:
    def __init__(self,ip,port):
        self.despat = Despat()
        self.ip = ip
        self.port = port
        self.Socket = socket(AF_INET,SOCK_DGRAM)
        self.Socket.bind(('',50007))

        self.processed_requests = {}  # Dicionário para armazenar respostas de IDs processados

        while True:
            data, addr = self.Socket.recvfrom(1024)

            print('Connected to:', addr)

            request = self.deserialize_request(data)  # Desserializa a mensagem Protobuf
            
            if request is None:
                print("Erro ao processar a mensagem: formato inválido")
                continue
            
            request_id = request.id  # Obtendo o ID corretamente

            if request_id in self.processed_requests:
                print(f"Mensagem duplicada detectada (ID: {request_id}). Reenviando resposta.")
                self.sendResponse(self.processed_requests[request_id], addr)
            else:
                if random.randint(0, 2) > 0:  # Simula pacotes perdidos
                    response = self.getRequest(data)
                    self.processed_requests[request_id] = response  # Armazena resposta
                    self.sendResponse(response, addr)
                else:
                    self.send_timeout(request_id, addr)

    def deserialize_request(self, data):
        """ Converte os dados recebidos em um objeto Protobuf """
        try:
            request = messages_pb2.Message()
            request.ParseFromString(data)
            return request
        except Exception as e:
            print(f"Erro ao desserializar mensagem Protobuf: {e}")
            return None

        
    def getRequest(self,req):
        return self.despat.invoke(req)

    def sendResponse(self,res,addr):
        self.Socket.sendto(res,addr)

    def send_timeout(self, request_id, addr):
        timeout_response = messages_pb2.Response()
        timeout_response.id = request_id
        timeout_response.status = messages_pb2.TIMEOUT  # Usando o enum ResponseStatus
        timeout_response.data = b""  # Timeout não precisa de dados

        self.Socket.sendto(timeout_response.SerializeToString(), addr)
        print(f"Timeout enviado para {addr}, ID: {request_id}")

server = UDPServer('127.0.0.1',50007)