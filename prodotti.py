
class Prodotto:
    def __init__(self, cod, pesoTeorico):
       self.codice = cod
       self.pesoTeorico = pesoTeorico

    def print(self):
       print(self.codice)
       print(str(self.pesoTeorico) + " Kg/m")
    
    def to_kg(self,mt = 1):
       return (self.pesoTeorico * mt)
    
    def to_mt(self, kg = 1):
       return (kg/self.pesoTeorico)


# CLASSE TUBOLARE
class Tubolare(Prodotto):
   def __init__(self, dim1, dim2, sp, pesoTeorico):
      cod = ("tb" + {dim1}+ "x" + {dim2} + "x" + {sp})
      super().__init__(cod, pesoTeorico)
      self.dim1 = dim1
      self.dim2 = dim2
      self.sp = sp
   
   def print(self):
      print("TUBOLARE")
      print({self.dim1} + "x" + {self.dim2} + "x" + {self.sp})
      print("Peso Teorico: " + {self.pesoTeorico})
    
#CLASSE PIATTO LAMINATO
class PiattoLam(Prodotto):
   def __init__(self, dim1, sp, pesoTeorico):
      cod = ("ptLam" + {dim1}+ "x" + {sp})
      super().__init__(cod, pesoTeorico)
      self.dim1 = dim1
      self.sp = sp
   
   def print(self):
      print("PIATTO LAMINATO")
      print({self.dim1} + "x" + {self.sp})
      print("Peso Teorico: " + {self.pesoTeorico})
