#from termcolor import colored
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Comic:
    def __init__(self,name:str,date:str,auth:str,price:float,condition:int,status:int=1):
        self.name = name
        self.date = date
        self.auth = auth
        self.price = price
        self.condition = condition
        self.status = status
    def display(self):
        print(f"{bcolors.BOLD}{self.name}{bcolors.ENDC} - by {self.auth}")
        print(f"{bcolors.HEADER}{self.date}{bcolors.ENDC}")
        print(f"Price: {bcolors.OKGREEN}${self.price}{bcolors.ENDC}")
        print(f"{bcolors.HEADER}{self.condition}{bcolors.ENDC}")
        print(f"{bcolors.HEADER}{self.status}{bcolors.ENDC}")

class Locadora:
    def __init__(self):
        self.comics = []
        self.giveComic(Comic("Batman", '15/03/1985', 'DC Comics', 25, 3))
        self.giveComic(Comic("Batman", '15/03/1985', 'DC Comics', 25, 3))
        self.giveComic(Comic("Spider-Man", '07/07/1990', 'Marvel Comics', 30, 4))
        self.giveComic(Comic("X-Men", '10/11/1995', 'Marvel Comics', 35, 2))
        self.giveComic(Comic("The Flash", '01/01/2000', 'DC Comics', 40, 5))
        self.giveComic(Comic("Iron Man", '20/06/1988', 'Marvel Comics', 28, 4))
        self.giveComic(Comic("Wonder Woman", '25/08/1992', 'DC Comics', 22, 3))
        self.giveComic(Comic("Superman", '12/02/1992', 'Haaper Colins', 20, 0))
        self.giveComic(Comic("Green Lantern", '03/05/1999', 'DC Comics', 24, 2))
        self.giveComic(Comic("Thor", '18/09/1994', 'Marvel Comics', 27, 4))
        self.giveComic(Comic("Hulk", '22/10/1987', 'Marvel Comics', 26, 1))
    def giveComic(self,comic:Comic):
        self.comics.append(comic)
    def takeComic(self,id:int):
        if self.comics[id].status == 1:
            self.comics[id].status = 2
            return self.comics[id]
        else:
            raise Exception('comic já reservada')

    def getComics(self):
        return self.comics


