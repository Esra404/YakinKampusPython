from tkinter import *
master=Tk()
canvas=Canvas(master,heigh=450,width=750)
canvas.pack()

frame_ust=Frame(master,bg='#add8e6')
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)



frame_alt_sol=Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)


frame_sag=Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)
hatirlatma_tipi_etiket=Label(frame_ust,bg='#add8e6',text="hatırlatma tipi :",font="verdana  12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,side=LEFT)
hatirlatma_tipi_opsiyon=StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")
hatirlatma_tipi_acilir_menu=OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "dogum günü",
    "alisveris",
    "odeme"
)
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT)

print(master.mainloop())