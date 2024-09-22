from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import prodotti
import frameOperator as frameOP


font_One = 'Times New Roman'
color_window_left_frame = '#32373B'
color_window_right_frame = '#4A5859'
color_button = '#F4B860'
color_button_active = '#C42335'
color_text = 'white'
color_top_background = '#C11C1E'
color_lightgray = '#CED4DA'
color_gray = '#ADB5BD'
color_verylightgray = "#E9ECEF"

tipi = {
        'Tubolare' : 'tb',
        'Piatto' : 'pt',
        'TuboTondo' : 'tt',
        'Tondo' : 'td',
        'Quadro' : 'qd',
    }

def show_error_message():
    messagebox.showerror(title="Errore",message="Errore nell'inserimento dei valori")
def show_info_message():
    messagebox.showinfo(title="Info", message="Dati mancanti\nControlla di aver inserito le misure")
def crea_prodotto(prodotto):
    if prodotto[0] == "tb":
        if prodotto[1].get() == "" or prodotto[2].get() == "" or prodotto[3].get() == "":
            return "error"
        else:
            return prodotti.Tubolare(prodotto[1].get(),prodotto[2].get(),prodotto[3].get())
    if prodotto[0] == "pt":
        if prodotto[1].get() == "" or prodotto[2].get() == "":
            return "error"
        else:
            return prodotti.Piatto(prodotto[1].get(),prodotto[2].get())
    if prodotto[0] == "tt":
        if prodotto[1].get() == "" or prodotto[2].get() == "":
            return "error"
        else:
            return prodotti.TuboTondo(prodotto[1].get(),prodotto[2].get())
    if prodotto[0] == "td":
        if prodotto[1].get() == "":
            return "error"
        else:
            return prodotti.Tondo(prodotto[1].get())
    if prodotto[0] == "qd":
        if prodotto[1].get() == "" or prodotto[2].get() == "":
            return "error"
        else:
            return prodotti.Quadro(prodotto[1].get(),prodotto[2].get())
    else:
        print("tipo prodotto passato non riconosciuto")

def crea_prodotto_from_selection(prodotto):
    if prodotto[0] == "tb":
        return prodotti.Tubolare(prodotto[1],prodotto[2],prodotto[3])
    if prodotto[0] == "pt":
        return prodotti.Piatto(prodotto[1],prodotto[2])
    if prodotto[0] == "tt":
        return prodotti.TuboTondo(prodotto[1],prodotto[2])
    if prodotto[0] == "td":
        return prodotti.Tondo(prodotto[1])
    if prodotto[0] == "qd":
        return prodotti.Quadro(prodotto[1],prodotto[2])
    else:
        print("tipo prodotto passato non riconosciuto")

def calcola(prodotto,frameCall):
    try:
        if type(prodotto[1]) == StringVar:
            prod = crea_prodotto(prodotto)
            prodotto.clear()
            if prod == "error": 
                show_error_message()
                frameOP.chiudi_frame(frameCall)
                return
        elif type(prodotto[1]) == str:
            prod = crea_prodotto_from_selection(prodotto)
            prodotto.clear()
        else:
            print("no check")
    except:
        prodotto.clear()
        show_info_message()
        return
    finally:
        frameOP.chiudi_frame(frameCall)

    
    calcolaWindow = Tk()
    calcolaWindow.geometry('570x220+570+260')
    calcolaWindow.resizable(False,False)
    calcolaWindow.columnconfigure(3,weight=1)
    calcolaWindow.rowconfigure(2,weight=1)
    calcolaWindow.title(prod.stampa_prodotto()) # SETTAGGIO TITOLO FINESTRA CON CODICE PRODOTTO

    def converti():
        entryFocus = calcolaWindow.focus_get()
        #metriEntry.index('end') == 0
        #kiliEntry.index('end') == 0
        if entryFocus == kiliEntry:
            metriRes = '{:.2f}'.format(prod.kgToMt(prod.get_pesoT(),float(kiliEntry.get())))
            metriEntry.delete(0,END)
            metriEntry.insert(0,metriRes)
        elif entryFocus == metriEntry:
            kiliRes = '{:.2f}'.format(prod.mtToKg(prod.get_pesoT(),float(metriEntry.get())))
            kiliEntry.delete(0,END)
            kiliEntry.insert(0,kiliRes)
        else:
            print('errore di calcolo')
            #Msgbox per errore inserimento
            pass

    #Creazione GUI
    topLabel_description = Label(calcolaWindow,text=prod.stampa_prodotto(),font=(font_One,24))
    topLabel_description.grid(column=0,row=0,columnspan=3)

    metriLabel = Label(calcolaWindow,text='METRI',font=(font_One,18),padx=10,pady=10)
    metriLabel.grid(column=0,row=1,padx=30,pady=10)
    metriEntry = Entry(calcolaWindow,font=(font_One,18),width=15,bd=7)
    metriEntry.grid(column=0,row=2,padx=10,pady=2)

    equalLabel = Label(calcolaWindow,text='=',font=(font_One,28),padx=10,pady=10)
    equalLabel.grid(column=1,row=1,rowspan=2,padx=30,pady=10)

    kiliLabel = Label(calcolaWindow,text='KILOGRAMMI',font=(font_One,18),padx=10,pady=10)
    kiliLabel.grid(column=2,row=1,padx=30,pady=10)
    kiliEntry = Entry(calcolaWindow,font=(font_One,18),width=15,bd=7)
    kiliEntry.grid(column=2,row=2,padx=10,pady=2)

    calcolaPesoButton = Button (calcolaWindow,text='Calcola',command=lambda:converti())
    calcolaPesoButton.grid(column=0,row=4,columnspan=3,pady=15)

def mostra():
    mostraWindow = Tk()
    mostraWindow.geometry('810x520+245+100')
    mostraWindow.title('Elenco prodotti')
    mostraWindow.resizable(False,False)

    
    colonne = ['tipo','misure','peso']
    tabella_prodotti = ttk.Treeview(mostraWindow,columns=colonne, show='headings',style='Treeview')
    tabella_prodotti.tag_configure('cell1',background=color_lightgray,foreground='black',font=(font_One,16))
    tabella_prodotti.tag_configure('cell2',background=color_gray,foreground='black',font=(font_One,16))
    tabella_prodotti.heading('tipo', text= 'Tipo',anchor='w')
    tabella_prodotti.heading('misure', text= 'Misure')
    tabella_prodotti.heading('peso', text= 'Peso Teorico')
    tabella_prodotti.column('tipo',width=260)
    tabella_prodotti.column('misure',width=260,anchor='center')
    tabella_prodotti.column('peso',width=260)


    righe = prodotti.crea_lista_prodotti_tabella()
    i=1
    print(righe[1])
    for riga in righe:
        riga = riga[1:]
        if i%2 == 0:
            tabella_prodotti.insert('',END,values=riga,tags='cell1')
        else:
            tabella_prodotti.insert('',END,values=riga,tags='cell2')
        i+=1

    tabella_prodotti.pack(fill=BOTH,side=LEFT,padx=5,pady=5)

    scrollBar = ttk.Scrollbar(mostraWindow, orient='vertical',command=tabella_prodotti.yview)
    scrollBar.pack(fill=Y,side='right')

    tabella_prodotti['yscrollcommand'] =scrollBar.set

def create_main_window():
    mainWindow = Tk()
    mainWindow.title('Convertitore pesi prontuario')
    mainWindow.iconbitmap("utility\LOGO DSALD.ico")
    mainWindow.geometry('800x520+250+100')
    mainWindow.resizable(False,False)

    tipo = StringVar()
    prodotto = []

    def selected():
        selected_index = listbox.curselection()  # Get the selected item's index
        if selected_index:
            selected_item = listbox.get(selected_index[0])  # Get the selected item
            prodotto.clear()
            dati = selected_item.split()
            tipo = tipi[dati[0].strip()]
            misure = dati[1].split('x')
            prodotto.append(tipo) 
            for misura in misure :
                prodotto.append(misura)

    def scegli_input():
        frameOP.chiudi_frame(mainWindow_inputFrame[0])
        mainWindow_inputFrame.pop()
        mainWindow_inputFrame.append(frameOP.crea_InputFrame(mainWindow_leftFrame))
        inputTipo = tipi[tipo.get()]
        prodotto.clear()
        id = inputTipo 
        frameOP.aggiorna_listBox(listbox,id)
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
        elif inputTipo == 'td':
            diametro = frameOP.crea_diametroFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,diametro])
        elif inputTipo == 'qd':
            larghezza = frameOP.crea_larghezzaFrame(mainWindow_inputFrame[0])
            altezza = frameOP.crea_altezzaFrame(mainWindow_inputFrame[0])
            prodotto.extend([inputTipo,larghezza,altezza])
        else:
            print("Errore comboBox")

    # Banner titolo largo
    mainWindow_topFrame = Frame(mainWindow,background = color_top_background)
    mainWindow_topFrame.pack(side='top',fill= 'x')
    mainWindow_labBig = Label(mainWindow_topFrame, text="Convertitore pesi prontuario",background = color_top_background,font=(font_One,36),pady=10)
    mainWindow_labBig.pack(side=LEFT)
    
    #Frame di sinistra contenente tipoFrame e inputFrame
    mainWindow_leftFrame = Frame(mainWindow,background=color_window_left_frame,padx=50)
    mainWindow_leftFrame.pack(side='left',fill=BOTH)

    # Frame per input
    mainWindow_inputFrame = [frameOP.crea_InputFrame(mainWindow_leftFrame)]

    #TIPO Frame con combobox per selezione tipo e GUI
    mainWindow_tipoFrame = Frame(mainWindow_leftFrame,background=color_window_left_frame,padx=50,pady=15)
    mainWindow_tipoFrame.pack(fill=BOTH)

    tipoLabel = Label(mainWindow_tipoFrame,text = 'Inserisci tipo:',background=color_window_left_frame,foreground='white',font=(font_One,16))
    tipoLabel.pack()
    tipoBox = ttk.Combobox(mainWindow_tipoFrame,textvariable = tipo)
    tipoBox.configure(font=(font_One,14))
    tipoBox['values'] = list(tipi.keys())
    tipoBox['state'] = 'readonly'
    tipoBox.pack()

    tipoBox.bind("<<ComboboxSelected>>",lambda x:scegli_input())

     # Frame per contenere i bottoni
    mainWindow_buttonFrame = Frame(mainWindow,padx=3,background=color_verylightgray)
    mainWindow_buttonFrame.pack(side='right',fill = BOTH,expand=True)
    mainWindow_buttonFrame.columnconfigure(2)
    mainWindow_buttonFrame.rowconfigure(4)

    # Bottone MOSTRA
    button2 = Button(mainWindow_buttonFrame, text="MOSTRA",
                     command = lambda:mostra(),
                     font =(font_One,16),width=15, height=1,
                     background=color_button, activebackground =color_button_active)
    button2.grid(column=0,row=0,padx=2,pady=5)
    
    # Bottone CALCOLA
    button3 = Button(mainWindow_buttonFrame, text="CALCOLA",
                     command=lambda:calcola(prodotto,mainWindow_inputFrame[0]),
                     font =(font_One,16),width=15, height=1,
                     background=color_button, activebackground =color_button_active)
    button3.grid(column=1,row=0,padx=3,pady=5)

    # ListBox che mostra tutti i prodotti nella home
    listbox = Listbox(mainWindow_buttonFrame,height=16,width=35,selectmode='single', bd=1,
                     background= color_lightgray,selectbackground=color_button,selectforeground='black',font=('Helvetiva',14))
    

    listbox.grid(column=0,row=1,columnspan=2,pady=5)
    listbox.bind('<<ListboxSelect>>',lambda x:selected())

    frameOP.aggiorna_listBox(listbox,id)

    mainWindow.mainloop()


# Esecuzione della funzione per la creazione della finestra principale
create_main_window()
