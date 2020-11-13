import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

def init_window():
    window = tk.Tk()
    window.title("Mi primera aplicación")
    window.geometry("450x250")

    label = tk.Label(window, text="Calculadora", font=("Arial bold", 15))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text="Ingrese primer número", font=("Arial bold", 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text="Ingrese segundo número", font=("Arial bold", 10))
    label_entrada2.grid(column = 0, row = 2)

    label_operador = tk.Label(window, text="Escoja un operador", font=("Arial bold", 10))
    label_operador.grid(column = 0, row = 3)

    combo_operador = ttk.Combobox(window)
    combo_operador["values"] = ["+", "-", "*", "/", "pow"]
    combo_operador.current(None) #En este valor puse None ya que me parecía más apropiado que la combobox estuviera vacía al inicio como es normal en la mayoría de los casos
    combo_operador.grid(column = 1, row = 3)
    
    label_resultado = tk.Label(window, text = "Resultado: ", font = ("Arial bold", 15))
    label_resultado.grid(column = 0, row = 5)

    boton = tk.Button(window, command = lambda: click_calcular(label_resultado, entrada1.get(), entrada2.get(), combo_operador.get(), seleccion(decimales), decinum(opcion)), text = "Calcular", bg = "blue", fg = "white")
    boton.grid(column = 1, row = 4)

    decimales = tk.IntVar()
    check = tk.Checkbutton(window, text="Incluir decimales", variable=decimales, onvalue=1, offvalue=0, command= lambda: seleccion(decimales))
    check.grid(column = 3, row = 1)

    opcion = tk.IntVar() # Como StrinVar pero en entero

    decimal1 = tk.Radiobutton(window, text="1 decimal", variable=opcion, value=1, command=lambda: decinum(opcion))
    decimal2 = tk.Radiobutton(window, text="2 decimales", variable=opcion, value=2, command=lambda: decinum(opcion))
    decimal3 = tk.Radiobutton(window, text="3 decimales", variable=opcion, value=3, command=lambda: decinum(opcion))
    
    decimal1.grid(column = 3, row = 2)
    decimal2.grid(column = 3, row = 3)
    decimal3.grid(column = 3, row = 4)

    window.mainloop()

def decinum(opcion):
    dec = 0
    if opcion.get() == 1:
        dec = 1
    elif opcion.get() == 2:
        dec = 2
    elif opcion.get() == 3:
        dec = 3
    return dec

def seleccion(decimales):
    if decimales.get() == 1:
        return True
    else:
        return False

def calculadora(num1, num2, operador):
    if operador == "+":
        ans = num1 + num2
    elif operador == "-":
        ans = num1 - num2
    elif operador == "*":
        ans = num1 * num2
    elif operador == "/":
        ans = round(num1 / num2, 2)
    elif operador == "pow":
        ans = num1 ** num2

    return ans

def click_calcular(label, num1, num2, operador, decimales, numdec):
    if num1 == '' or num2 == '' or (num2 == '0' and operador == '/') or f:
        msg.showerror("Error", "Error, intente de nuevo... o no :)")
    valor1 = float(num1)
    valor2 = float(num2)
    if decimales == True:
        if numdec == 1:
            ans = round(calculadora(valor1, valor2, operador), 1)
        elif numdec == 2:
            ans = round(calculadora(valor1, valor2, operador), 2)
        elif numdec == 3:
            ans = format(calculadora(valor1, valor2, operador), ".3f")
        else:
            ans = int(calculadora(valor1, valor2, operador))
    else:
        ans = int(calculadora(valor1, valor2, operador))

    label.configure(text = "Resultado: " + str(ans))

        
def main():
    init_window()

main()
