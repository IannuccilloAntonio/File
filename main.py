from giocatore import Giocatore
from pistola import Pistola

g = Giocatore ("Antonio", 10)
g1= Giocatore2 ("Mister", 10)
while g.get_vite() > 0 or g.get_munizioni() > 0 and g1.get_vite < 0 or g1:
    print g.get_nome(), "spara e ha ", g.getMunizioni()
    if g.get_vite() <= 0:
        print g.get_nome(), " non ha piu' vite e quindi game over\n "
        break
    elif g.getMunizioni() == 0:
        print "GAMEOVER visto che ", g.getMunizioni() 
        break
    else:
        print "continua"
