from socket import *

class UDPClient:
    def __init__(self):
        self.sock = socket(AF_INET,SOCK_DGRAM)
    def sendRequest(self,req):
        self.sock.sendto(req,('127.0.0.1',50007))
    def getResponse(self):
        data, addr = self.sock.recvfrom(1024)
        return data
    def close(self):
        self.sock.close()
        