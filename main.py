from tkinter import *
from tkinter import ttk
import prodotti

elencoPesiProdotti = 'pesi_teorici_ferro.txt'
fontOne = 'Helvetica'
root = Tk()
root.title('Convertitore pesi prontuario')
root.geometry('350x300')

root_frmTop = Frame(root,bg='#931F1D',width=300,height=50)
root_frmTop.pack(fill=BOTH,side=TOP)
root_frmCommand = Frame(root,bg='#D1CCDC',width=300,height=250)
root_frmCommand.pack(fill=BOTH,expand=True)
root_frmCommand.columnconfigure(2,weight=1)
root_frmCommand.rowconfigure(2,weight=1)

root_labBig =Label(root_frmTop,text = 'Convertitore Rapido',font=(fontOne,28),border=3)
root_labBig.grid(column=0,row=0,columnspan=2,ipadx=5,ipady=5,sticky='ew')

root_btnCalcola =Button(root_frmCommand,text='Calcola',padx=5,pady=5,font=(fontOne,15))
root_btnAggiungi =Button(root_frmCommand,text='Aggiungi',padx=5,pady=5,font=(fontOne,15))
root_btnModifica =Button(root_frmCommand,text='Modifica',padx=5,pady=5,font=(fontOne,15))
root_btnCalcola.grid(column=0,row=1,ipadx=5,ipady=5)
root_btnAggiungi.grid(column=1,row=1,ipadx=5,ipady=5)
root_btnModifica.grid(column=0,row=2,columnspan=2,ipadx=5,ipady=5)


root.mainloop()