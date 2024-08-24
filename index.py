from tkinter import *
from tkinter import ttk
import prodotti
import frameOperator as frameOP

font_One = 'Times New Roman'

def crea_prodotto(prodotto):
    if prodotto[0] == "tb":
        return prodotti.Tubolare(prodotto[1].get(),prodotto[2].get(),prodotto[3].get())
    if prodotto[0] == "pt":
        return prodotti.Piatto(prodotto[1].get(),prodotto[2].get())
    if prodotto[0] == "tt":
        return prodotti.TuboTondo(prodotto[1].get(),prodotto[2].get())
    if prodotto[0] == "tp":
        return prodotti.TondoPieno(prodotto[1].get())
    if prodotto[0] == "rp":
        return prodotti.RettangoloPieno(prodotto[1].get(),prodotto[2].get())
    else:
        print("tipo prodotto passato non riconosciuto")

def calcola(prodotto,frameCall):
    calcolaWindow = Tk()
    calcolaWindow.geometry('570x180+570+260')
    calcolaWindow.resizable(False,False)
    calcolaWindow.columnconfigure(3,weight=1)
    calcolaWindow.rowconfigure(2,weight=1)

    frameOP.chiudi_frame(frameCall)
    prod = crea_prodotto(prodotto)

    calcolaWindow.title(prod.codice) # SETTAGGIO TITOLO FINESTRA CON CODICE PRODOTTO

    def converti():
        entryFocus = calcolaWindow.focus_get()
        #metriEntry.index('end') == 0
        #kiliEntry.index('end') == 0
        if entryFocus == kiliEntry:
            metriRes = '{:.2f}'.format(prod.kgToMt(float(prod.get_pesoT()),float(kiliEntry.get())))
            metriEntry.delete(0,END)
            metriEntry.insert(0,metriRes)
        elif entryFocus == metriEntry:
            kiliRes = '{:.2f}'.format(prod.mtToKg(float(prod.get_pesoT()),float(metriEntry.get())))
            kiliEntry.delete(0,END)
            kiliEntry.insert(0,kiliRes)
        else:
            print('errore di calcolo')
            #Msgbox per errore inserimento
            pass

    #Creazione GUI
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

""" def aggiungi(prodotto,frameCall):
    aggiungiWindow = Tk()
    aggiungiWindow.title('Aggiungi...')
    aggiungiWindow.geometry('570x180+570+260')
    aggiungiWindow.resizable(False,False)

    prod = prodotto[0]
    def aggiungi_elemento():
        #Se prodotto già esiste modifica peso Teorico con nuovo valore inserito
        if not prod.modifica_prodotto(prod.codice,pesoTeoricoEntry.get()):
        #Se prodotto non esiste lo crea
            prod.aggiungi_prodotto(prod.codice,pesoTeoricoEntry.get())
        aggiungiWindow.destroy()
        frameOP.chiudi_frame(frameCall)

    pesoTeoricoLabel = Label(aggiungiWindow,text='Peso Teorico (Kg/m)',font=(font_One,18),padx=10,pady=10)
    pesoTeoricoLabel.pack(pady=10)
    pesoTeoricoEntry = Entry(aggiungiWindow,font=(font_One,18),width=15,bd=7)
    pesoTeoricoEntry.pack(pady=5)
    pesoTeoricoEntry.focus()

    aggiungiProdottoButton = Button (aggiungiWindow,text='Aggiungi',command=lambda:aggiungi_elemento())
    aggiungiProdottoButton.pack(side='right',expand=True)
 """
def mostra():
    mostraWindow = Tk()
    mostraWindow.geometry('570x400+570+260')
    mostraWindow.title('Elenco prodotti')
    mostraWindow.resizable(False,False)
 
    prods = prodotti.crea_lista_prodotti()

    listbox = Listbox(mostraWindow,height=20,width=40,selectmode='single',font=('Helvetiva',14))
    listbox.pack(fill=BOTH,expand=True,side='left')

    i=0
    for prod in prods:
        listbox.insert(i,prod.stampa_prodotto())
        i+=1
        listbox.insert(i,'')
        i+=1

    scrollBar = ttk.Scrollbar(mostraWindow, orient='vertical',command=listbox.yview)
    scrollBar.pack(fill=Y,side='right')

    listbox['yscrollcommand'] =scrollBar.set

def create_main_window():
    mainWindow = Tk()
    mainWindow.title('Convertitore pesi prontuario')
    mainWindow.geometry('800x520+250+100')
    mainWindow.resizable(False,False)

    # Banner titolo largo in alto
    mainWindow_topFrame = Frame(mainWindow,background = '#931F1D')
    mainWindow_topFrame.pack(side='top',fill= 'x')
    mainWindow_labBig = Label(mainWindow_topFrame, text="Convertitore pesi prontuario",background = '#931F1D',font=(font_One,36),pady=10)
    mainWindow_labBig.pack(side=LEFT)
    
    #Frame di sinistra contenente tipoFrame e inputFrame
    mainWindow_leftFrame = Frame(mainWindow,background='#1E1E24',padx=50)
    mainWindow_leftFrame.pack(side='left',fill=BOTH,expand=True)

    #TIPO Frame con combobox per selezione tipo e GUI
    mainWindow_tipoFrame = Frame(mainWindow_leftFrame,background='#1E1E24',padx=50,pady=15)
    mainWindow_tipoFrame.pack(fill=BOTH,expand=False)

    tipo = StringVar()
    tipi = {
        'Tubolare' : 'tb',
        'Piatto' : 'pt',
        'Tubo tondo' : 'tt',
        'Tondo pieno' : 'tp',
        'Rettangolo pieno' : 'rp',
    }

    tipoLabel = Label(mainWindow_tipoFrame,text = 'Inserisci tipo:',background='#1E1E24',foreground='white',font=(font_One,16))
    tipoLabel.pack()
    tipoBox = ttk.Combobox(mainWindow_tipoFrame,textvariable = tipo)
    tipoBox.configure(font=(font_One,14))
    tipoBox['values'] = list(tipi.keys())
    tipoBox['state'] = 'readonly'
    tipoBox.pack()

    # Frame per input
    mainWindow_inputFrame = [frameOP.crea_InputFrame(mainWindow_leftFrame)]
    prodotto = []
    
    def scegli_input():
        frameOP.chiudi_frame(mainWindow_inputFrame[0])
        mainWindow_inputFrame.pop()
        mainWindow_inputFrame.append(frameOP.crea_InputFrame(mainWindow_leftFrame))
        prodotto.clear()
        inputTipo = tipi[tipo.get()]
        if inputTipo == 'tb':
            larghezza = frameOP.crea_larghezzaFrame(mainWindow_inputFrame[0])
            altezza = frameOP.crea_altezzaFrame(mainWindow_inputFrame[0])
            spessore = frameOP.crea_spessoreFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,larghezza,altezza,spessore])
        elif inputTipo == 'pt':
            larghezza = frameOP.crea_larghezzaFrame(mainWindow_inputFrame[0])
            spessore = frameOP.crea_spessoreFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,larghezza,spessore])
        elif inputTipo == 'tt':
            diametro = frameOP.crea_diametroFrame(mainWindow_inputFrame[0])
            spessore = frameOP.crea_spessoreFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,diametro,spessore])
        elif inputTipo == 'tp':
            diametro = frameOP.crea_diametroFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,diametro])
        elif inputTipo == 'rp':
            larghezza = frameOP.crea_larghezzaFrame(mainWindow_inputFrame[0])
            altezza = frameOP.crea_altezzaFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,larghezza,altezza])
        else:
            print("Errore comboBox")
    
    tipoBox.bind("<<ComboboxSelected>>",lambda x:scegli_input())

    # Frame per contenere i bottoni
    mainWindow_buttonFrame = Frame(mainWindow)
    mainWindow_buttonFrame.pack(side='right',fill = BOTH,expand=True)
    
    # Bottone AGGIUNGI/MODIFICA
    button1 = Button(mainWindow_buttonFrame, text="AGGIUNGI",
                     command = lambda:aggiungi(prodotto,mainWindow_inputFrame[0]), font =(font_One,18),width=15, height=2)
    button1.pack(padx=10,pady=35)
    
    # Bottone MOSTRA
    button2 = Button(mainWindow_buttonFrame, text="MOSTRA",
                     command = lambda:mostra(), font =(font_One,18),width=15, height=2)
    button2.pack(padx=10,pady=35)
    
    # Bottone CALCOLA
    button3 = Button(mainWindow_buttonFrame, text="CALCOLA",
                     command=lambda:calcola(prodotto,mainWindow_inputFrame[0]),font =(font_One,18),width=15, height=2)
    button3.pack(padx=10,pady=35)
    mainWindow.mainloop()


# Esecuzione della funzione per la creazione della finestra principale
create_main_window()
