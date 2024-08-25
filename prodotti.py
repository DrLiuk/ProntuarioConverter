
#Inizializzazione variabile per FILE.txt elenco pesi teorici elementi
fileName = "dataFile/pesi_teorici_ferro.txt"

tipi = {
   'tb' : 'Tubolare',
   'pt' : 'Piatto',
   'tt' : 'Tubo tondo',
   'td' : 'Tondo',
   'qd' : 'Quadro'
    }

class Prodotto:
   def __init__(self, cod):
      self.codice = cod

   def stampa_prodotto(self):
      return (f"{self.codice}    {self.get_pesoT()} Kg/m")
   
   def get_pesoT(self):
      f = open(fileName,"r")
      righe = f.readlines()
      f.close()
      for riga in righe:
         riga = riga.strip()
         dati = riga.split('|')
         if dati[0].strip() == self.codice:
            pesoT = dati[1].strip()
            return float(pesoT)

   def aggiungi_prodotto(self,pesoT):
      f = open(fName,'a')
      f.write(f'{self.codice} | {pesoT}\n')
      f.close()
   
   def modifica_prodotto(self,newPeso):
      trovato = False
      try:
         f = open(fName,"r")
         righe = f.readlines()
         f.close()
         i = 0
         for riga in righe:
            riga = riga.strip()
            dati = riga.split('|')
            cod = dati[0]
            cod = cod.strip()
            if cod == self.codice:
                  righe[i] = (f'{self.codice} | {newPeso}\n')
                  trovato = True
                  break
            i+=1
         f = open(fName,"w")
         f.writelines(righe)
         f.close()
         return trovato
      except:
         print("Prodotto non presente")

   def mtToKg(self,pesoT,metri):
      return pesoT*metri

   def kgToMt(self,pesoT,kili):
      return kili/pesoT
  
def crea_lista_prodotti():
   f = open(fileName,'r')
   righe = f.readlines()
   f.close()

   prodotti_list = []
   for riga in righe:
      dati = riga.split('|')
      cod = dati[0].strip()
      p = Prodotto(cod)
      prodotti_list.append(p)

   return prodotti_list


class Tubolare(Prodotto):
   def __init__(self,larghezza,altezza,spessore):
      self.tipo = "tb"
      self.larghezza = larghezza
      self.altezza = altezza
      self.spessore = spessore
      codice = (f"{self.tipo}-{self.larghezza}x{self.altezza}x{self.spessore}")
      super().__init__(codice)
   
   def stampa_tubolare(self):
      print(f"Tubolare {self.larghezza}x{self.altezza}x{self.spessore}\tPeso Teorico:{self.pesoT}")
      
class Piatto(Prodotto):
   def __init__(self,larghezza,spessore):
      self.tipo = "pt"
      self.larghezza = larghezza
      self.spessore = spessore
      codice = (f"{self.tipo}-{self.larghezza}x{self.spessore}")
      super().__init__(codice)
   
   def stampa_piatto(self):
      print(f"Piatto {self.larghezza}x{self.spessore}\tPeso Teorico:{self.pesoT}")

class TuboTondo(Prodotto):
   def __init__(self,diametro,spessore):
      self.tipo = "tt"
      self.diametro = diametro
      self.spessore = spessore
      codice = (f"{self.tipo}-{self.diametro}x{self.spessore}")
      super().__init__(codice)

class Tondo(Prodotto):
   def __init__(self,diametro):
      self.tipo = "td"
      self.diametro = diametro
      codice = (f"{self.tipo}-{self.diametro}")
      super().__init__(codice)

class Quadro(Prodotto):
   def __init__(self,larghezza,altezza):
      self.tipo = "qd"
      self.larghezza = larghezza
      self.altezza = altezza
      codice = (f"{self.tipo}-{self.larghezza}x{self.altezza}")
      super().__init__(codice)

