
f = open("C:/Users/lucad/Desktop/file python/ProntuarioConverter/dataFile/tubolariProntuario.txt","r")
righe = f.readlines()
f.close()
i=0
for riga in righe:
        #newRiga="tb-"
        #riga.strip()
        #dati = riga.split("x")
        #newRiga += (dati[0].strip() +"x" + dati[1].strip() + "x")
        #dati[2] = dati[2].strip()
        #dati2 = dati[2].split()
        #newRiga += (dati2[0].strip() + " | " + dati2[1].strip() + "\n")
        #righe[i] = newRiga
        #i+=1
        newRiga = righe[i].replace(",", ".")
        righe[i] = newRiga
        i+=1


f = open("C:/Users/lucad/Desktop/file python/ProntuarioConverter/dataFile/tubolariProntuario.txt","w")
f.writelines(righe)
f.close()