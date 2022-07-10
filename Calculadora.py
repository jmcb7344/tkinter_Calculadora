from tkinter import *

contador = 0
c = []

def igual():
    global contador
    contador = contador + 1
    n = resultado.get()
    if n == "":
        m = resultado.set("0")
        historial(n, m)
    else:
        m =  eval(n)
        resultado.set(m)
        historial(n, m)
    
def bot(num):
    if resultado.get() == "0":
        resultado.set(num)
    else:
        resultado.set(resultado.get()+num)

def borrar(evente=None):
    resultado.set("0")

def borra(event=None):
    c = resultado.get()
    resultado.set(c.rstrip(resultado.get()[-1]))

def historial(num1=None, num2=None, num3=contador):
    global c
    num3 = Button(cuadro3, text= "{} = \n {}".format(num1,num2), width=40,height=2
                    ,bg="plum1", fg="black", anchor="e", command=lambda:his(num2)).pack()
 

def his(num2=None):
    resultado.set(num2)

#Root es para crear la Raiz grafica madre
root = Tk()
root.title("Calculadora")
root.geometry("420x317")
root.resizable(0,0)
root.config(bd=1, relief = "solid")

#variables
resultado = StringVar()
res = StringVar()


cuadro1 = Frame(root)
cuadro1.place(x=2, y=2,width=210)
pantalla = Entry(cuadro1, textvariable=resultado)
pantalla.pack()
pantalla.insert(0, "0")
pantalla.config(bd=1, font=("Arial",16), justify="right", state="disabled",relief = "solid")

#Memoria
cuadro3 = Frame(root)
cuadro3.place(x=215, y=2,width=199,height=311)
cuadro3.config(bd=1, relief = "solid", bg="lightblue")
b = Button(cuadro3, text="Borrar", bg="plum1", fg="black").pack(anchor=NE)



#Botones con clic
cuadro2 = Frame(root)
cuadro2.place(x=2, y=31,width=210,height=282)
cuadro2.config(bd=1, relief = "solid")

B1 = Button(cuadro2, text="1",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("1")).grid(row=1, column=0,)
B2 = Button(cuadro2, text="2",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("2")).grid(row=1, column=1)
B3 = Button(cuadro2, text="3",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("3")).grid(row=1, column=2)
B4 = Button(cuadro2, text="4",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("4")).grid(row=2, column=0)
B5 = Button(cuadro2, text="5",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("5")).grid(row=2, column=1)
B6 = Button(cuadro2, text="6",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("6")).grid(row=2, column=2)
B7 = Button(cuadro2, text="7",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("7")).grid(row=3, column=0)
B8 = Button(cuadro2, text="8",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("8")).grid(row=3, column=1)
B9 = Button(cuadro2, text="9",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("9")).grid(row=3, column=2)
B0 = Button(cuadro2, text="0",width=6,height=3,
            bg = "gray", fg = "purple", command=lambda:bot("0")).grid(row=4, column=1)
B0 = Button(cuadro2, text=".",width=6,height=3,
            bg = "lightblue", fg = "purple", command=lambda:bot(".")).grid(row=4, column=2)
B0 = Button(cuadro2, text="=",width=6,height=3,
            bg = "lightblue", fg = "purple", command=igual).grid(row=4, column=3)
B0 = Button(cuadro2, text="+",width=6,height=3,
            bg = "lightblue", fg = "purple", command=lambda:bot("+")).grid(row=3, column=3)
B0 = Button(cuadro2, text="-",width=6,height=3,
            bg = "lightblue", fg = "purple", command=lambda:bot("-")).grid(row=2, column=3)
B0 = Button(cuadro2, text="*",width=6,height=3,
            bg = "lightblue", fg = "purple", command=lambda:bot("*")).grid(row=1, column=3)
B0 = Button(cuadro2, text="/",width=6,height=3,
            bg = "lightblue", fg = "purple", command=lambda:bot("/")).grid(row=0, column=3)
B0 = Button(cuadro2, text="%",width=6,height=3,
            bg = "lightblue", fg = "purple").grid(row=0, column=2)
B0 = Button(cuadro2, text=u"\u232B", command=borra ,width=6,height=3,
            bg = "lightblue", fg = "purple").grid(row=0, column=1)
B0 = Button(cuadro2, text="CE",width=6,height=3,
            bg = "lightblue", fg = "purple", command = borrar).grid(row=0, column=0)
B0 = Button(cuadro2, text="+/-",width=6,height=3,
            bg = "lightblue", fg = "purple").grid(row=4, column=0)

#botones de teclado
root.bind("1",lambda _:bot("1"))
root.bind("2",lambda _:bot("2"))
root.bind("3",lambda _:bot("3"))
root.bind("4",lambda _:bot("4"))
root.bind("5",lambda _:bot("5"))
root.bind("6",lambda _:bot("6"))
root.bind("7",lambda _:bot("7"))
root.bind("8",lambda _:bot("8"))
root.bind("9",lambda _:bot("9"))
root.bind("0",lambda _:bot("0"))
root.bind("+",lambda _:bot("+"))
root.bind("-",lambda _:bot("-"))
root.bind("*",lambda _:bot("*"))
root.bind("/",lambda _:bot("/"))
root.bind("<Return>",igual)
root.bind("<Delete>",borrar)
root.bind("<Escape>",borrar)


#Root es para cerrar la Raiz grafica madre
root.mainloop()
