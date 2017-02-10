from giocatore import Giocatore
from pistola import Pistola

g = Giocatore ("Antonio", 10)

while get_vite > 0 or get_munizioni > 0:
    print g.get_Nome(), "spara e ha " g.getMunizioni()
    if get_vite <=0:
        print g.get_Nome, " non ha piu' vite e quindi game over "
    

