from socket import *
import messages_pb2 as Message

class UDPClient:
    def __init__(self,timeout):
        self.sock = socket(AF_INET,SOCK_DGRAM)
        self.sock.settimeout(timeout)
    def sendRequest(self,req):
        self.sock.sendto(req,('127.0.0.1',50007))
    def getResponse(self):
        try:
            data, addr = self.sock.recvfrom(1024)
            return data
        except timeout:
            return "Timeout"
    def close(self):
        self.sock.close()
        