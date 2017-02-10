from pistola import  Pistola

class Giocatore:
    def __init__ (self, nome, vite):
        self.nome = nome
        self.vite = vite
        self.p = Pistola(10)
    def setnome(self, nome):
        self.nome = nome
    def setvite(self, vite):
        self.vite = vite
    def getnome(self):
        return self.nome
    def getvite(self):
        return self.vite

