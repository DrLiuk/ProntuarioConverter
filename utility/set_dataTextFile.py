
f = open("C:/Users/lucad/Desktop/file python/ProntuarioConverter/dataFile/pesi_teorici_ferro.txt","r")
righe = f.readlines()
f.close()
i=0
for riga in righe:
        newRiga = riga.replace("tp", "td")
        newRiga = newRiga.replace(",", ".")
        righe[i] = newRiga
        i+=1


f = open("C:/Users/lucad/Desktop/file python/ProntuarioConverter/dataFile/pesi_teorici_ferro.txt","w")
f.writelines(righe)
f.close()