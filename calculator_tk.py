from tkinter import *

cal = Tk()

cal.iconbitmap("calc.ico")
cal.geometry("250x250")
cal.config(bg="blue")
miFrame = Frame(cal)

miFrame.pack()

operacion = ""

reset_screen = False

resultado = 0

numPa = StringVar()

screen = Entry(miFrame, textvariable=numPa)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="white", fg="red", justify="right")
# -------------------Function-----------------------


def numberPuls(num):

    global operacion

    if operacion != "":

        numPa.set(num)

    else:

        numPa.set(numPa.get() + num)
# ----------------------------------------------------------------------------


def suma(num):
    global operacion
    global reset_screen
    global resultado

    resultado = resultado+int(num)
    operacion = "suma"

    reset_screen = True

    numPa.set(resultado)


# -----------------------------------------------------------------------------
num1 = 0

contador_resta = 0


def scadere(num):

    global operacion

    global reset_screen

    global resultado

    global num1

    global contador_resta

    if contador_resta == 0:

        num1 = int(num)

        resultado = num1

    else:

        if contador_resta == 1:

            resultado = num1-int(num)

        else:

            resultado = int(resultado)-int(num)

            numPa.set(resultado)

            resultado = numPa.get()

    contador_resta = contador_resta+1

    operacion = "scadere"

    reset_screen = True

# ---------------------------------------------------------------------------------------


contador_multi = 0


def inmultire(num):

    global operacion

    global resultado

    global num1

    global contador_multi

    global reset_screen

    if contador_multi == 0:

        num1 = int(num)

        resultado = num1

    else:

        if contador_multi == 1:

            resultado = num1*int(num)

        else:

            resultado = int(resultado)*int(num)

        numPa.set(resultado)

        resultado = numPa.get()

    contador_multi = contador_multi+1

    operacion = "inmultire"

    reset_screen = True

# ---------------------------------------------------------------------------------------


contador_divi = 0


def impartire(num):

    global operacion

    global resultado

    global num1

    global contador_divi

    global reset_screen

    if contador_divi == 0:

        num1 = float(num)

        resultado = num1

    else:

        if contador_divi == 1:

            resultado = num1/float(num)

        else:

            resultado = float(resultado)/float(num)

        numPa.set(resultado)

        resultado = numPa.get()

    contador_divi = contador_divi+1

    operacion = "impartire"

    reset_screen = True

# ---------------------------------------------------------------------------------------


def res():

    global reset_screen

    global resultado

    global operacion

    global contador_resta

    global contador_multi

    global contador_divi

    if operacion == "suma":

        numPa.set(resultado + int(numPa.get()))

        resultado = 0

    elif operacion == "scadere":

        numPa.set(int(resultado)-int(numPa.get()))

        resultado = 0

        contador_resta = 0

    elif operacion == "inmultire":

        numPa.set(int(resultado)*int(numPa.get()))

        resultado = 0

        contador_multi = 0

    elif operacion == "impartire":

        numPa.set(int(resultado)/int(numPa.get()))

        resultado = 0

        contador_divi = 0


# --------------go 1-----------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numberPuls("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numberPuls("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numberPuls("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3,
                  command=lambda: impartire(numPa.get()))
botonDiv.grid(row=2, column=4)


# --------------go 2-----------------------

boton4 = Button(miFrame, text="4", width=3, command=lambda: numberPuls("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numberPuls("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numberPuls("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=3,
                   command=lambda: inmultire(numPa.get()))
botonMult.grid(row=3, column=4)


# --------------go 3-----------------------

boton1 = Button(miFrame, text="1", width=3, command=lambda: numberPuls("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numberPuls("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numberPuls("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3,
                   command=lambda: scadere(numPa.get()))
botonRest.grid(row=4, column=4)


# --------------go 4-----------------------

boton0 = Button(miFrame, text="0", width=3, command=lambda: numberPuls("0"))
boton0.grid(row=5, column=1)
botonVirgula = Button(miFrame, text=",", width=3,
                      command=lambda: numberPuls(","))
botonVirgula.grid(row=5, column=2)
botonEgal = Button(miFrame, text="=", width=3, command=lambda: res())
botonEgal.grid(row=5, column=3)
botonAdd = Button(miFrame, text="+", width=3,
                  command=lambda: suma(numPa.get()))
botonAdd.grid(row=5, column=4)

# ----------------------------------------------
botonReset = Button(miFrame, text="C", width=3,
                    command=lambda: numberPuls("0"))
botonReset.grid(row=6, column=1)


cal.mainloop()
