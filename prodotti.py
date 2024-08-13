
class Prodotto:
    def __init__(self, cod, peso):
       self.codice = cod
       self.peso = peso

    def print(self):
       print(self.codice)
       print(str(self.peso) + " Kg/m")
    
    def to_kg(self,mt = 1):
       return (self.peso * mt)
    
    def to_mt(self, kg = 1):
       return (kg/self.peso)


# CLASSE TUBOLARE
class Tubolare(Prodotto):
   def __init__(self, dim1, dim2, sp, peso):
      cod = ("tb" + {dim1}+ "x" + {dim2} + "x" + {sp})
      super().__init__(cod, peso)
      self.dim1 = dim1
      self.dim2 = dim2
      self.sp = sp
   
   def print(self):
      print("TUBOLARE")
      print({self.dim1} + "x" + {self.dim2} + "x" + {self.sp})
      print("Peso: " + {self.peso})
    
#CLASSE PIATTO LAMINATO
class PiattoLam(Prodotto):
   def __init__(self, dim1, sp, peso):
      cod = ("ptLam" + {dim1}+ "x" + {sp})
      super().__init__(cod, peso)
      self.dim1 = dim1
      self.sp = sp
   
   def print(self):
      print("PIATTO LAMINATO")
      print({self.dim1} + "x" + {self.sp})
      print("Peso: " + {self.peso})
