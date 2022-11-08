from tkinter import Tk, Button, Entry, END

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=1)

# Funciones
def get(int):
    pantalla.insert(END,int)
    
def calcular():
    resultado = eval(pantalla.get())
    pantalla.delete(0,END)
    pantalla.insert(END,resultado)

# Configuración botones
boton_1 = Button(root, text = "1", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(1)).grid(row = 1, column = 0, padx = 1, pady = 1 )
boton_2 = Button(root, text = "2", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(2)).grid(row = 1, column = 1, padx = 1, pady = 1 )
boton_3 = Button(root, text = "3", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(3)).grid(row = 1, column = 2, padx = 1, pady = 1 )
boton_4 = Button(root, text = "4", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(4)).grid(row = 2, column = 0, padx = 1, pady = 1 )
boton_5 = Button(root, text = "5", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(5)).grid(row = 2, column = 1, padx = 1, pady = 1 )
boton_6 = Button(root, text = "6", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(6)).grid(row = 2, column = 2, padx = 1, pady = 1 )
boton_7 = Button(root, text = "7", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(7)).grid(row = 3, column = 0, padx = 1, pady = 1 )
boton_8 = Button(root, text = "8", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(8)).grid(row = 3, column = 1, padx = 1, pady = 1 )
boton_9 = Button(root, text = "9", width = 9, height = 3, bg = "white", fg = "red", borderwidth = 0, cursor = "hand2", command = lambda: get(9)).grid(row = 3, column = 2, padx = 1, pady = 1 )
boton_igual = Button(root, text = " = ", width = 20, height = 3, bg = "red", fg = "white", borderwidth = 0, cursor = " hand2", command = lambda: calcular()).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
boton_punt  = Button(root, text = ".", width = 9, height = 3, bg = "spring green", fg = "black",borderwidth = 0, cursor = "hand2", command = lambda: get(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
boton_mas = Button(root, text = "+", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: get("+")).grid(row = 1, column = 3, padx = 1, pady = 1)
boton_menos = Button(root, text = "-", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: get("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
boton_multiplicacion = Button(root, text = "*",  width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: get("*")).grid(row = 3, column = 3, padx = 1, pady = 1)
boton_division = Button(root, text = "/", width = 9, height = 3, bg = "deep sky blue", fg = "black", borderwidth = 0, cursor = "hand2", command = lambda: get("/")).grid(row = 4, column = 3, padx = 1, pady = 1)


root.mainloop()
