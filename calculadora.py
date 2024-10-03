from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadera")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def adicao(*args):
    n1 = float(number1.get())
    n2 = float(number2.get())
    soma = n1 + n2
    result.set(soma)
def sub(*args):
    n1 = float(number1.get())
    n2 = float(number2.get())
    subitra = n1 - n2
    result.set(subitra)
def multi(*args):
    n1 = float(number1.get())
    n2 = float(number2.get())
    multiplica = n1 * n2
    result.set(multiplica)
def div(*args):
    n1 = float(number1.get())
    n2 = float(number2.get())
    divide = n1 / n2
    result.set(divide)

number1 = IntVar()
number2 = IntVar()
number1_entry = ttk.Entry(mainframe, width=7, textvariable=number1)
number1_entry.grid(column=2, row=1, sticky=(W, E))
number2_entry = ttk.Entry(mainframe, width=7, textvariable=number2)
number2_entry.grid(column=2, row=2, sticky=(W, E))

result = StringVar()
result.set("Resultado!")
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=(W, E))

#=
ttk.Button(mainframe, text="+", command=adicao).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="-", command=sub).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="*", command=multi).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="/", command=div).grid(column=4, row=2, sticky=W)

root.mainloop()
