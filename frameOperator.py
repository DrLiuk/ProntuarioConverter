from tkinter import *
from tkinter import ttk

font_One = 'Arial'

def crea_InputFrame(frame):
    mainWindow_inputFrame = Frame(frame,background='#1E1E24',padx=50)
    mainWindow_inputFrame.pack(fill=BOTH,expand=False)
    return mainWindow_inputFrame

def crea_larghezzaFrame(frame):
    mainWindow_larghezzaFrame = Frame(frame,background='#1E1E24')
    mainWindow_larghezzaFrame.pack(padx=15,pady=20)
    larghezza = StringVar()
    larghezzaLabel = Label(mainWindow_larghezzaFrame,text = 'Inserisci larghezza:',background='#1E1E24',foreground='white',font=(font_One,16))
    larghezzaLabel.pack()
    larghezzaEntry = Entry(mainWindow_larghezzaFrame,textvariable=larghezza,font=(font_One,14))
    larghezzaEntry.pack()
    return larghezza

def crea_altezzaFrame(frame):
    mainWindow_altezzaFrame = Frame(frame,background='#1E1E24')
    mainWindow_altezzaFrame.pack(padx=15,pady=20)
    altezza = StringVar()
    altezzaLabel = Label(mainWindow_altezzaFrame,text = 'Inserisci altezza:',background='#1E1E24',foreground='white',font=(font_One,16))
    altezzaLabel.pack()
    altezzaEntry = Entry(mainWindow_altezzaFrame,textvariable=altezza,font=(font_One,14))
    altezzaEntry.pack()
    return altezza

def crea_spessoreFrame(frame):
    mainWindow_spessoreFrame = Frame(frame,background='#1E1E24')
    mainWindow_spessoreFrame.pack(padx=15,pady=20)
    spessore = StringVar()
    spessoreLabel = Label(mainWindow_spessoreFrame,text = 'Inserisci spessore:',background='#1E1E24',foreground='white',font=(font_One,16))
    spessoreLabel.pack()
    spessoreEntry = Entry(mainWindow_spessoreFrame,textvariable=spessore,font=(font_One,14))
    spessoreEntry.pack()
    return spessore

def chiudi_frame(frame):
    frame.destroy()
