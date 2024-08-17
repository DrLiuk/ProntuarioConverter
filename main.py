from tkinter import *
from tkinter import ttk
import prodotti

elencoPesiProdotti = 'pesi_teorici_ferro.txt'
font_One = 'Arial'


def calcola(tipo,larghezza,altezza,spessore):
    calcolaWindow = Tk()
    calcolaWindow.title("Calcola...")
    calcolaWindow.geometry('570x180+570+260')
    calcolaWindow.resizable(False,False)
    calcolaWindow.columnconfigure(3,weight=1)
    calcolaWindow.rowconfigure(2,weight=1)

    def converti():
        entryFocus = calcolaWindow.focus_get()
        #metriEntry.index('end') == 0
        #kiliEntry.index('end') == 0
        if entryFocus == kiliEntry:
            metriRes = '{:.2f}'.format(prodotti.kgToMt(float(kiliEntry.get()),peso))
            metriEntry.delete(0,END)
            metriEntry.insert(0,metriRes)
        elif entryFocus == metriEntry:
            kiliRes = '{:.2f}'.format(prodotti.mtToKg(float(metriEntry.get()),peso))
            kiliEntry.delete(0,END)
            kiliEntry.insert(0,kiliRes)
        else:
            print('errore di calcolo')
            #Msgbox per errore inserimento
            pass

    peso = prodotti.pesoTeoricoDaMisure(tipo,larghezza,altezza,spessore)

    metriLabel = Label(calcolaWindow,text='METRI',font=(font_One,18),padx=10,pady=10)
    metriLabel.grid(column=0,row=0,padx=30,pady=10)
    metriEntry = Entry(calcolaWindow,font=(font_One,18),width=15,bd=7)
    metriEntry.grid(column=0,row=1,padx=10,pady=2)
    metriEntry.focus()

    equalLabel = Label(calcolaWindow,text='=',font=(font_One,28),padx=10,pady=10)
    equalLabel.grid(column=1,row=0,rowspan=2,padx=30,pady=10)

    kiliLabel = Label(calcolaWindow,text='KILOGRAMMI',font=(font_One,18),padx=10,pady=10)
    kiliLabel.grid(column=2,row=0,padx=30,pady=10)
    kiliEntry = Entry(calcolaWindow,font=(font_One,18),width=15,bd=7)
    kiliEntry.grid(column=2,row=1,padx=10,pady=2)

    calcolaPesoButton = Button (calcolaWindow,text='Calcola',command=lambda:converti())
    calcolaPesoButton.grid(column=0,row=3,columnspan=3,pady=15)

def create_main_window():
    mainWindow = Tk()
    mainWindow.title('Convertitore pesi prontuario')
    mainWindow.geometry('700x520+500+100')
    mainWindow.resizable(False,False)

    # Titolo largo in cima
    mainWindow_topFrame = Frame(mainWindow,background = '#931F1D')
    mainWindow_topFrame.pack(side='top',fill= 'x')
    mainWindow_labBig = Label(mainWindow_topFrame, text="Convertitore pesi e lunghezze",background = '#931F1D',font=(font_One,36),pady=10)
    mainWindow_labBig.pack(side=LEFT)

    # Frame per input
    def crea_InputFrame():
        mainWindow_inputFrame = Frame(mainWindow,background='#1E1E24',padx=50)
        mainWindow_inputFrame.pack(side='left',fill=BOTH,expand=True)
        return mainWindow_inputFrame
    mainWindow_inputFrame = crea_InputFrame()
    def distruggiFrame(frame):
        frame.destroy()
    
    # Frame per contenere i primi due bottoni affiancati
    mainWindow_buttonFrame = Frame(mainWindow)
    mainWindow_buttonFrame.pack(side='right',fill = BOTH,expand=True)
    
    #Input utente
    mainWindow_tipoFrame = Frame(mainWindow_inputFrame,background='#1E1E24')
    mainWindow_tipoFrame.pack(padx=15,pady=20)
    tipo = StringVar()
    tipoLabel = Label(mainWindow_tipoFrame,text = 'Inserisci tipo:',background='#1E1E24',foreground='white',font=(font_One,16))
    tipoLabel.pack()
    tipoBox = ttk.Combobox(mainWindow_tipoFrame,textvariable= tipo,font=(font_One,14))
    tipoBox['values'] = ['tubo','piatto','quadro','tondo']
    tipoBox['state'] = 'readonly'
    tipoBox.pack()
    #tipoEntry = Entry(mainWindow_tipoFrame,textvariable=tipo,background='#1E1E24',foreground='white',font=(font_One,14))
    #tipoEntry.pack()
   
  
    mainWindow_larghezzaFrame = Frame(mainWindow_inputFrame,background='#1E1E24')
    mainWindow_larghezzaFrame.pack(padx=15,pady=20)
    larghezza = StringVar()
    larghezzaLabel = Label(mainWindow_larghezzaFrame,text = 'Inserisci larghezza:',background='#1E1E24',foreground='white',font=(font_One,16))
    larghezzaLabel.grid(column=0,row=2)
    larghezzaEntry = Entry(mainWindow_larghezzaFrame,textvariable=larghezza,font=(font_One,14))
    larghezzaEntry.grid(column=0,row=3,padx=10,pady=5)

    
    mainWindow_altezzaFrame = Frame(mainWindow_inputFrame,background='#1E1E24')
    mainWindow_altezzaFrame.pack(padx=15,pady=20)
    altezza = StringVar()
    altezzaLabel = Label(mainWindow_altezzaFrame,text = 'Inserisci altezza:',background='#1E1E24',foreground='white',font=(font_One,16))
    altezzaLabel.grid(column=0,row=4)
    altezzaEntry = Entry(mainWindow_altezzaFrame,textvariable=altezza,font=(font_One,14))
    altezzaEntry.grid(column=0,row=5,padx=10,pady=5)
    

    mainWindow_spessoreFrame = Frame(mainWindow_inputFrame,background='#1E1E24')
    mainWindow_spessoreFrame.pack(padx=15,pady=20)
    spessore = StringVar()
    spessoreLabel = Label(mainWindow_spessoreFrame,text = 'Inserisci spessore:',background='#1E1E24',foreground='white',font=(font_One,16))
    spessoreLabel.grid(column=0,row=6)
    spessoreEntry = Entry(mainWindow_spessoreFrame,textvariable=spessore,font=(font_One,14))
    spessoreEntry.grid(column=0,row=7,padx=10,pady=5)


    # Primo bottone
    button1 = Button(mainWindow_buttonFrame, text="AGGIUNGI",font =(font_One,18),width=15, height=2)
    button1.pack(padx=10,pady=35)
    
    # Secondo bottone
    button2 = Button(mainWindow_buttonFrame, text="MODIFICA",font =(font_One,18),width=15, height=2)
    button2.pack(padx=10,pady=35)
    
    # Terzo bottone largo quanto i due precedenti insieme
    button3 = Button(mainWindow_buttonFrame, text="CALCOLA", command=lambda:calcola(tipo.get(),larghezza.get(),altezza.get(),spessore.get()),font =(font_One,18),width=15, height=2)
    button3.pack(padx=10,pady=35)

    mainWindow.mainloop()

# Esecuzione della funzione per la creazione della finestra principale
create_main_window()
