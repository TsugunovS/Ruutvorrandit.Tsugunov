from tkinter import * 
def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

aken=Tk()
aken.geometry("650x260")
aken.title("Ruutvõrrandid")
aken.iconbitmap("xterm.ico")

pealkiri=Label(aken, #1
               text="Решение квадратного уравнения",
               bg="lightblue",
               fg="#168c35",
               font="Times_new_roma 20",
               height=2,
               width=28)
pealkiri.pack(pady=20)

nupp2=Button(aken, #1
               text="Решение",
               bg="Yellow",
               fg="black",
               font="Times_new_roma 14",
               activebackground="lightblue",
               height=2,
               width=40)
pealkiri.pack(pady=20)

tekst_kast=Entry(aken, #2
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)

pealkiri2=Label(aken, #3
               text="x**2",
               fg="#168c35",
               font="Times_new_roma 20",
               height=5,
               width=4,
               justify=LEFT)

tekst_kast2=Entry(aken, #4
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)

pealkiri3=Label(aken, #5
               text="x+",
               fg="#168c35",
               font="Times_new_roma 20",
               height=5,
               width=2,
               justify=LEFT)

tekst_kast3=Entry(aken, #6
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)

pealkiri4=Label(aken, #7
               text="=0",
               fg="#168c35",
               font="Times_new_roma 20",
               activebackground="#a80a1a",
               height=5,
               width=2,
               justify=LEFT)

nupp=Button(aken, #8
            text="Решить",
            bg="Green",
            fg="#020812",
            font="Algerian 20",
            activebackground="lightblue",
            height=2,
            width=7,
            justify=LEFT)




nupp2.pack(side=BOTTOM)
pealkiri.pack() #1
tekst_kast.pack(side=LEFT) #2
pealkiri2.pack(side=LEFT) #3
tekst_kast2.pack(side=LEFT) #4
pealkiri3.pack(side=LEFT) #5
tekst_kast3.pack(side=LEFT) #6
pealkiri4.pack(side=LEFT) #7
nupp.pack(side=LEFT) #8
side=BOTTOM
aken.mainloop()
