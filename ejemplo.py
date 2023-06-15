from tkinter import *

#Variables x, y
X = 460
Y = 460

#Crear una ventana 
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")


#frame

graf = Frame(ventana_principal)
graf.config(width=480, height=480, bg="red")
graf.place(x=10,y=10)

# Canvas

c = Canvas(graf,width=X, height=Y)
c.config(bg="black")
c.place(x=10,y=10)


#Rectangulo del tren
rect_1 = c.create_rectangle(X/2-100,Y/2+5,X/2+200,Y/2+180, fill="light grey")
rect_2 = c.create_rectangle(X/2+25,Y/2-130,X/2+180,Y/2+5, fill="ivory4")
rect_3 = c.create_rectangle(X/2+50,Y/2-105,X/2+155,Y/2-20, fill="gainsboro")
rect_4 = c.create_rectangle(X/2+5,Y/2-180,X/2+200,Y/2-130, fill="gray26")
rect_5 = c.create_rectangle(X/2+26,Y/2-215,X/2+179,Y/2-180, fill="gray26")
rect_6 = c.create_rectangle(X/2-80,Y/2-55,X/2-40,Y/2+5, fill="ivory4")
rect_7 = c.create_rectangle(X/2-100,Y/2-95,X/2-20,Y/2-55, fill="ivory4")

rect_8 = c.create_rectangle(X/2-125,Y/2+150,X/2-100,Y/2+20, fill="ivory4")
circ_1 = c.create_oval(X/2-205,Y/2+25,X/2-150,Y/2+150, fill="gray26")
rect_9 = c.create_rectangle(X/2-125,Y/2+5,X/2-170,Y/2+170, fill="ivory4")

# Circulos del tren
circ_2 = c.create_oval(X/2+120,Y/2+105,X/2+230,Y/2+220, fill="gray26")
circ_3 = c.create_oval(X/2-0,Y/2+105,X/2+110,Y/2+220, fill="gray26")
circ_4 = c.create_oval(X/2-120,Y/2+105,X/2-10,Y/2+220, fill="gray26")

# Otros rectangulos
rect_7 = c.create_rectangle(X/2-50,Y/2+145,X/2+40,Y/2+185, fill="gray17")
rect_8 = c.create_rectangle(X/2+70,Y/2+145,X/2+170,Y/2+185, fill="gray17")

# Cara
cara_1 = c.create_oval(X/2+55,Y/2-115,X/2+149,Y/2-20, fill="yellow")

# Nombre (text)
text_1 = c.create_text(X/2+50,Y/2+80, anchor="center", text="Orlando Villarreal Aparicio", font=("Arial", 18, "bold"), fill="blue", activefill="yellow")



ventana_principal.mainloop()