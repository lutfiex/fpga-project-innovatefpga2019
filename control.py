import serial.tools.list_ports as port_list
from tkinter import *
from tkinter.ttk import Combobox
import os

window=Tk()
window.geometry("500x500")
def getport():
    os.system("python play.py" + " " + cb.get() )
    
ports = list(port_list.comports())
lport = []
for p in ports:
    lport.append(p.device)

var = StringVar()
cb=Combobox(window, values = lport)
cb.place(x=10, y=10)

B = Button(window, text = "Play", command = getport)
B.place(x = 50,y = 50)
c = str(cb.get)



window.mainloop()

def start():
    sr.readline()
