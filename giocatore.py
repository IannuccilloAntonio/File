from pistola import  Pistola

class Giocatore:
    def __init__ (self, nome, vite):
        self.nome = nome
        self.vite = vite
        self.p = Pistola(10)
    def set_nome(self, nome):
        self.nome = nome
    def set_vite(self, vite):
        self.vite = vite
    def get_nome(self):
        return self.nome
    def get_vite(self):
        return self.vite
    def getMunizioni(self):
        return self.p.munizioni

