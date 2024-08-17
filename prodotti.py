
#Inizializzazione variabile per FILE.txt elenco pesi teorici elementi
fName = 'pesi_teorici_ferro.txt'

class Prodotto:
    def __init__(self, cod):
       self.codice = cod

    def print(self,peso):
       print(f"{self.codice} - {peso} Kg/m")

def calcolaPesoTeorico(cod):
   f = open(fName,"r")
   righe = f.readlines()
   f.close()
   print(f'Prima riga {righe[0]}')
   cod = cod.strip()
   dati = cod.split('-')
   codTipo = dati[0]
   codMis = dati[1]

   for riga in righe:
      riga = riga.strip()
      dati = riga.split('-')
      if dati[0] == codTipo and dati[1] == codMis:
         dati = riga.split('|')
         return dati[1]
   #creare msg Box
   return ''  

def pesoTeoricoDaMisure(tipo,larghezza,altezza,spessore):
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
   return 0  

def mtToKg(metri,peso):
   return peso*metri

def kgToMt(kili,peso):
   return kili/peso