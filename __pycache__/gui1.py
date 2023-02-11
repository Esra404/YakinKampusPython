from tkinter import *
from tkcalendar import DateEntry

#PART 1
master=Tk()
canvas=Canvas(master,heigh=450,width=750)
canvas.pack()

frame_ust=Frame(master,bg='#1d3059')
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)



frame_alt_sol=Frame(master,bg='#3bb4ac')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)


frame_alt_sag=Frame(master,bg='#add8e6')
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)

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
hatirlatma_tarih_secici=DateEntry(frame_ust,width=12,background='orange',foreground='black',borderwidth=1,locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10,pady=10,side=RIGHT)
hatirlatma_tipi_etiket=Label(frame_ust,bg='#add8e6',text="hatırlatma tarihi :",font="verdana  12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,side=RIGHT)
#PART İKİ

Label(frame_alt_sol,text="Hatirlatma yöntemi",bg='#add8e6',font="Verdana 10 bold").pack(padx=10,pady=10,anchor=NW)
var=IntVar()
R1=Radiobutton(frame_alt_sol,text="Sisteme kaydet",variable=var,value=0,bg='#add8e6',font="Verdana 10")
R1.pack(anchor=NW,pady=5,padx=15)

R2=Radiobutton(frame_alt_sol,text="E posta gönder",variable=var,value=1,bg='#add8e6',font="Verdana 10")
R2.pack(anchor=NW,pady=5,padx=15)

var1=IntVar()
C1=Checkbutton(frame_alt_sol,text="bir hafta önce",variable=var1,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C1.pack(anchor=NW,pady=2,padx=25)

var2=IntVar()
C2=Checkbutton(frame_alt_sol,text="bir gün önce",variable=var2,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C2.pack(anchor=NW,pady=2,padx=25)

var3=IntVar()
C3=Checkbutton(frame_alt_sol,text="aynı gün",variable=var3,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C3.pack(anchor=NW,pady=2,padx=25)


#PART 3
from tkinter import messagebox
def gonder():
    son_mesaj=""
    # if var.get():
    #     if var.get()==1:
    #         son_mesaj +="veriniz basarıyla sisteme kaydedilmişitr"
    #         tip=hatirlatma_tipi_opsiyon() if hatirlatma_tipi_opsiyon.get() =='' else "genel"
    #         tarih=hatirlatma_tarih_secici.get()
    #         mesaj=metin_alani.grt("1.0","END")








        # elif var.get() ==2:
        #     son_mesaj +="e posta yoluyla hatirlatma size ulaşacaktır."

        # messagebox.showinfo("başarılı işlem ",son_mesaj)
    return
Label(frame_alt_sag,text="HATİRLATMA MESAJI",bg='#add8e6',font="verdana 10 bold").pack(padx=10,pady=10,anchor=NW)
metin_alani=Text(frame_alt_sag,heigh=9,width=50)
metin_alani.tag_configure('styls',foreground='#bfbfbf',font=('verdana',7,'bold'))
metin_alani.pack()

karsilama_metni='mesajini buraya gir'
metin_alani.insert(END,karsilama_metni,'style')
gonder_butonu=Button(frame_alt_sag,text='gonder',command=gonder)
gonder_butonu.pack(anchor=S)


print(master.mainloop())



