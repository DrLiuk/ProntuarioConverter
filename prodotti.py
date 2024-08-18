
#Inizializzazione variabile per FILE.txt elenco pesi teorici elementi
fName = 'pesi_teorici_ferro.txt'

tipi = {
   'tb' : 'Tubolare',
   'pt' : 'Piatto',
   'tt' : 'Tubo tondo',
   'td' : 'Tondo pieno',
   'qd' : 'Quadro pieno',
    }


class Prodotto:
    def __init__(self, cod):
       self.codice = cod

    def print(self,peso):
       print(f"{self.codice} - {peso} Kg/m")

def getPesoTeorico_daCodice(cod):
   f = open(fName,"r")
   righe = f.readlines()
   f.close()
   cod = cod.strip()
   dati = cod.split('-')
   codTipo = dati[0]
   codMis = dati[1]

   for riga in righe:
      riga = riga.strip()
      dati = riga.split('-')
      if dati[0] == codTipo:
         cod = dati[1].split('|')
         cod[0] = cod[0].strip()
         cod[1] = cod[1].strip()
         if cod[0] == codMis:
            return float(cod[1])
   #creare msg Box
   return 0.0  

def getPesoTeorico_daMisure(tipo,larghezza,altezza,spessore):
   f = open(fName,'r')
   righe = f.readlines()
   f.close()

   codMis1 = (f'{larghezza}x{altezza}x{spessore}')
   codMis2 = (f'{altezza}x{larghezza}x{spessore}')
 
   for riga in righe:
      riga = riga.strip()
      dati = riga.split('-')
      if dati[0] == tipo:
         cod = dati[1].split('|')
         cod[0] = cod[0].strip()
         cod[1] = cod[1].strip()
         if cod[0] == codMis1 or cod[0] == codMis2:
            return float(cod[1])
   #creare msg Box
   return 0.0  

def aggiungi_prodotto_daMisure(tipo,larghezza,altezza,spessore,peso):
   f = open(fName,'a')
   f.write(f'{tipo}-{larghezza}x{altezza}x{spessore} | {peso}\n')
   f.close()
   
def aggiungi_prodotto_daCodice(codice,peso):
   f = open(fName,'a')
   f.write(f'{codice} | {peso}\n')
   f.close()

def modifica_prodotto_daCodice(codice,peso):
   trovato = False
   f = open(fName,"r")
   righe = f.readlines()
   f.close()
   i = 0
   for riga in righe:
      riga = riga.strip()
      dati = riga.split('|')
      cod = dati[0]
      cod = cod.strip()
      if cod == codice:
         righe[i] = (f'{codice} | {peso}\n')
         trovato = True
         break
      i+=1
   f = open(fName,"w")
   f.writelines(righe)
   f.close()
   return trovato
   
def crea_lista_prodotti():
   f = open(fName,'r')
   righe = f.readlines()
   f.close()

   i=0
   for riga in righe:
      dati = riga.split('-')
      tipoCompleto = tipi[dati[0]]
      dati = dati[1].split('|')
      righe[i] = (f'{tipoCompleto} - {dati[0]}  Peso: {dati[1]} Kg/m')
      i+=1

   return righe

def mtToKg(metri,peso):
   return peso*metri

def kgToMt(kili,peso):
   return kili/peso