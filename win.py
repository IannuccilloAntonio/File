from tkinter import *
from tkinter import ttk
import math
class Mywin(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calcola la distanza di un punto dall'origine")
        
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
        self.punto_x =StringVar()
        self.punto_y =StringVar()
        self.risultato = StringVar()

        ttk.Label(self.mainframe, width=7, text="Punto_x:").grid(column=0, row=0, sticky=(E,))
        self.punto_x_entry = ttk.Entry( self.mainframe, textvariable=self.punto_x)
        self.punto_x_entry.grid(column=1, row=0, sticky=(W,))

        ttk.Label(self.mainframe, width=7, text="Punto_y:").grid(column=0, row=1, sticky=(E,))
        self.punto_y_entry = ttk.Entry(self.mainframe, textvariable=self.punto_y)
        self.punto_y_entry.grid(column=1, row=1, sticky=(W,))

        
    def distanza(self):
        self.risultato.set(float
    def start(self):
        self.mainloop()


root = Mywin()
root.start()

