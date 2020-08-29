from tkinter import *
import random
import webbrowser

#cantidad de items (el event activa el Enter)
def cantidad_items(event = None):
    
    global x
    
    x= int(texto1.get())
    texto1.delete(0, END)
    
    texto1.bind("<Return>",añadir)
    label1.configure(text = "Ingrese el título de los ítems")
    boton1.configure(text = "Ingresar", command=añadir)
    
#nombre de los items e impresión
def añadir(event = None): #No entiendo, explicación: bind() runs with argument, command= runs without argument

    new=2
    tabUrl = "http://google.com/?#q="
    item = texto1.get()
    
    lista.append(item)
    texto1.delete(0, END)
    
    if len(lista)== x:
        
        texto1.destroy()
        boton1.destroy()
        label1.destroy()
        
        rando = random.choice(lista)
        
        if ("coger" in lista):
            resultado = Label(window, text="Toca coger", font= "Helvetica 30")
            resultado.place(relx=0.5, rely=0.5, anchor= CENTER)
        elif ("Coger" in lista):
            resultado = Label(window, text="Toca coger", font= "Helvetica 30")
            resultado.place(relx=0.5, rely=0.5, anchor= CENTER)
        else:
            webbrowser.open(tabUrl + rando, new=new)

#main -------------------------------------------------------------------

x = 0
lista = []

#generación de ventana
window = Tk()

window.title("Decidir que mierda hacer con Mora")
window.geometry("600x500")
window.configure(background="light blue")

#descripciones
label1 = Label(window, text="Introduzca la cantidad de ítems",font="Helvetica 16", bd="3", background="light grey")
label1.place(relx = 0.5, rely= 0.35, anchor=CENTER)

#primer entry del número
texto1 = Entry(window, font = "Helvetica 17", width = 26)
texto1.bind("<Return>", cantidad_items)
texto1.place(relx = 0.5, rely=0.45, anchor=CENTER)

#firma
firma = Label(window, text="HermesBV",font = "Times 10", background= "light blue")
firma.place(relx = 1, rely= 1, anchor=SE)

#botón ejecución del input
boton1 = Button(window, text = "Ingresar", command = cantidad_items)
boton1.place(relx = 0.5, rely = 0.55, anchor= CENTER)

window.mainloop()

