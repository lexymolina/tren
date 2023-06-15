from tkinter import*
import random

#--------------------
#variables globales
#--------------------
BASE = 360
ALTURA = 360

#--------------------
#ventana principal
#--------------------
ventana_principal = Tk()
ventana_principal.title("graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("400x400")
ventana_principal.config(bg= "white")

#----------------------
#frame de graficacion
#----------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=380, height=380)
frame_graficacion.place(x=10, y=10)

#creacion canvas 
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# tren
rect_1 = c.create_rectangle(BASE-250,ALTURA-100,BASE-80,ALTURA-200, fill="purple1")
rect_2 = c.create_rectangle(BASE-170,ALTURA-200,BASE-100,ALTURA-270, fill="mediumpurple1")
rect_3 = c.create_rectangle(BASE-160,ALTURA-210,BASE-110,ALTURA-260, fill= "white")
rect_4 = c.create_rectangle(BASE-180,ALTURA-270,BASE-90,ALTURA-290, fill="dodgerblue2")
rect_5 = c.create_rectangle(BASE-170,ALTURA-290,BASE-100,ALTURA-300, fill="dodgerblue1")
rect_6 = c.create_rectangle(BASE-200,ALTURA-200,BASE-220,ALTURA-250, fill="mediumpurple1")
rect_7 = c.create_rectangle(BASE-190,ALTURA-250,BASE-230,ALTURA-260, fill="dodgerblue1")
circ_1 = c.create_oval(BASE-250,ALTURA-190,BASE-300,ALTURA-112, fill="deepskyblue4")
rect_8 = c.create_rectangle(BASE-260,ALTURA-110,BASE-250,ALTURA-190, fill="mediumpurple")
rect_9 = c.create_rectangle(BASE-280,ALTURA-200,BASE-260,ALTURA-100, fill="mediumpurple1")
circ_2 = c.create_oval(BASE-120,ALTURA-140,BASE-70,ALTURA-80, fill="steelblue")
circ_3 = c.create_oval(BASE-183,ALTURA-140,BASE-133,ALTURA-80, fill="steelblue")
circ_4 = c.create_oval(BASE-250,ALTURA-140,BASE-200,ALTURA-80, fill="steelblue")
rect_10 = c.create_rectangle(BASE-220,ALTURA-115,BASE-170,ALTURA-100, fill="deep sky blue")
rect_11 = c.create_rectangle(BASE-150,ALTURA-115,BASE-100,ALTURA-100, fill="deep sky blue")

# Nombre (text)
text_1 = c.create_text(BASE-160,ALTURA-170, anchor="center", text="LEXY", font=("Arial", 10, "bold"), fill="blue")
text_1 = c.create_text(BASE-160,ALTURA-150, anchor="center", text="MOLINA", font=("Arial", 10, "bold"), fill="blue")

#agregar una imagen al canvas
img_cara = PhotoImage(file="cara1.png")
cara1 = c.create_image(BASE/1.6, ALTURA/2.8, image=img_cara)

#desplegar ventana
ventana_principal.mainloop()
