from tkinter import *
from tkinter import ttk
import prodotti

font_One = 'Times New Roman'
color_window_left_frame = '#32373B'
color_window_right_frame = '#4A5859'
color_button = '#F4B860'
color_button_active = '#C83E4D'
color_text = 'white'
color_base = 'white'
color_top_background = '#C83E4D'

def crea_InputFrame(frame):
    mainWindow_inputFrame = Frame(frame,background=color_window_left_frame)
    mainWindow_inputFrame.pack(fill=BOTH)
    return mainWindow_inputFrame

def crea_larghezzaFrame(frame):
    mainWindow_larghezzaFrame = Frame(frame,background=color_window_left_frame)
    mainWindow_larghezzaFrame.pack(padx=15,pady=20)
    larghezza = StringVar()
    larghezzaLabel = Label(mainWindow_larghezzaFrame,text = 'Inserisci larghezza:',
                           background=color_window_left_frame,foreground=color_text,font=(font_One,16))
    larghezzaLabel.pack()
    larghezzaEntry = Entry(mainWindow_larghezzaFrame,textvariable=larghezza,font=(font_One,14))
    larghezzaEntry.pack()
    return larghezza

def crea_altezzaFrame(frame):
    mainWindow_altezzaFrame = Frame(frame,background=color_window_left_frame)
    mainWindow_altezzaFrame.pack(padx=15,pady=20)
    altezza = StringVar()
    altezzaLabel = Label(mainWindow_altezzaFrame,text = 'Inserisci altezza:',
                         background=color_window_left_frame,foreground=color_text,font=(font_One,16))
    altezzaLabel.pack()
    altezzaEntry = Entry(mainWindow_altezzaFrame,textvariable=altezza,font=(font_One,14))
    altezzaEntry.pack()
    return altezza

def crea_spessoreFrame(frame):
    mainWindow_spessoreFrame = Frame(frame,background=color_window_left_frame)
    mainWindow_spessoreFrame.pack(padx=15,pady=20)
    spessore = StringVar()
    spessoreLabel = Label(mainWindow_spessoreFrame,text = 'Inserisci spessore:',
                          background=color_window_left_frame,foreground=color_text,font=(font_One,16))
    spessoreLabel.pack()
    spessoreEntry = Entry(mainWindow_spessoreFrame,textvariable=spessore,font=(font_One,14))
    spessoreEntry.pack()
    return spessore

def crea_diametroFrame(frame):
    mainWindow_diametroFrame = Frame(frame,background=color_window_left_frame)
    mainWindow_diametroFrame.pack(padx=15,pady=20)
    diametro = StringVar()
    diametroLabel = Label(mainWindow_diametroFrame,text = 'Inserisci diametro:',
                          background=color_window_left_frame,foreground=color_text,font=(font_One,16))
    diametroLabel.pack()
    diametroEntry = Entry(mainWindow_diametroFrame,textvariable=diametro,font=(font_One,14))
    diametroEntry.pack()
    return diametro

def chiudi_frame(frame):
    frame.destroy()

def aggiorna_listBox(box,id):
        box.delete(0, END)
        prods = prodotti.crea_lista_prodotti_tabella()
        for prod in prods: 
            if id in prod[0]:
                box.insert(END,f'{prod[1]}   {prod[2]}   --   {prod[3]} Kg/m')

