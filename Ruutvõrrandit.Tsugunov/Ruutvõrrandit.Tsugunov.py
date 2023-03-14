from tkinter import * 
def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

aken=Tk()
aken.geometry("650x260")
aken.title("Ruutvõrrandid")

pealkiri=Label(aken,
               text="Ruutvõrrandid",
               bg="lightblue",
               fg="#32a852",
               font="Times_new_roma 20",
               height=2,
               width=28)
pealkiri.pack(pady=20)

tekst_kast=Entry(aken,
                 fg="#24ab67",
                 bg="Lightblue",
                 font="Algerian 20",
                 width=3,
                 justify=LEFT)

nupp=Button(aken,
            text="Решить",
            bg="lightblue",
            fg="#020812",
            font="Times_new_roma 20",
            activebackground="lightblue",
            height=2,
            width=24,
            anchor=E)

tekst_kast=Entry(aken,
                 fg="lightblue",
                 bg="grey",
                 font="Algerian 20",
                 width=20,
                 justify=CENTER)
tekst_kast.bind("<Return>", text_to_lbl)

tekst_kast.pack()
tekst_kast.pack(side=LEFT)
pealkiri.pack()
nupp.pack()
aken.mainloop()
