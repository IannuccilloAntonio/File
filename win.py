from tkinter import *
from tkinter import ttk
from math import sqrt
from punto import Punto
class Mywin(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calcola la distanza di un punto dall'origine")

    
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
        p = Punto(10, 10)
        p.x = StringVar()
        p.y = StringVar()

        ttk.Label(self.mainframe, width=7, text="Punto_x:").grid(column=0, row=0, sticky=(E,))
        self.p.x = ttk.Entry( self.mainframe, textvariable=self.p.x)
        self.p.x.grid(column=1, row=0, sticky=(W,))

        ttk.Label(self.mainframe, width=7, text="Punto_y:").grid(column=0, row=1, sticky=(E,))
        self.p.y = ttk.Entry(self.mainframe, textvariable=self.p.y)
        self.p.y.grid(column=1, row=1, sticky=(W,))

        
    def start(self):
        self.mainloop()


root = Mywin()
root.start()

