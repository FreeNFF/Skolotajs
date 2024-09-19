class Skolotaji:
    def __init__(self, tips1, tips2, uzvards1, uzvards2):
        self.uzvards1 = uzvards1
        self.uzvards2 = uzvards2
        self.tips1 = tips1
        self.tips2 = tips2

    def izdruka(self):
        pass



class SakumskolasSkolotajs(Skolotaji):
    def __init__(self,  uzvards1, skaits1, klase1):
        self.uzvards1 = uzvards1
        self.klase1 = klase1
        self.skaits1 = skaits1



    def sakumsskola(self):
        return("Sākumskolas (tips – 1) skolotājs {} māca {} stundas {} klasē.").format(self.uzvards1, self.skaits1, self.klase1)

class VidusskolasSkolotajs(Skolotaji):
    def __init__(self, uzvards1, prieksmets1, prieksmets2, skaits2):
        self.uzvards1 = uzvards1
        self.prieksmets1 = prieksmets1
        self.prieksmets2 = prieksmets2
        self.skaits2 = skaits2



    def vidusskola(self):
        return("Vidusskolas (tips – 3) skolotājs {} māca šādus priekšmetus: {} un {}, kopā {} stundas.").format(self.uzvards1, self.prieksmets1, self.prieksmets2, self.skaits2)


tips1 = int(input("Ja 1. skolotājs māca sākumskolā, ievadiet (1), ja skolotājs māca vidusskolā ievadiet (3): "))

if tips1 == 3:
    uzvards1 = input("Ievadiet 1. skolotāja uzvārdu: ")
    prieksmets1 =input("Ievadiet pirmo pasniegto priekšmetu: ")
    stunda4 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    prieksmets2 =input("Ievadiet otro pasniegto priekšmetu: ")
    stunda3 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    skaits2 = stunda3 + stunda4
    objekts1 = VidusskolasSkolotajs(uzvards1, prieksmets1, prieksmets2, skaits2)
    print(objekts1.vidusskola())
elif tips1 == 1:
    uzvards1 = input("Ievadiet 1. skolotāja uzvārdu: ")
    klase1 = input("Ievadiet skolotāja klasi: ")
    skaits1 = input("Ievadiet skolotāja stundu skaitu: ")
    objekts2 = SakumskolasSkolotajs(uzvards1, skaits1, klase1)
    print(objekts2.sakumsskola())
else:
    print("Nav pareizi ievadīti dati.")



tips2 = int(input("Ja 2. skolotājs māca sākumskolā, ievadiet (1), ja skolotājs māca vidusskolā ievadiet (3): "))

if tips2 == 3:
    uzvards1 = input("Ievadiet 2. skolotāja uzvārdu: ")
    prieksmets1 =input("Ievadiet pirmo pasniegto priekšmetu: ")
    stunda4 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    prieksmets2 =input("Ievadiet otro pasniegto priekšmetu: ")
    stunda3 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    skaits2 = stunda3 + stunda4
    objekts3 = VidusskolasSkolotajs(uzvards1, prieksmets1, prieksmets2, skaits2)
    print(objekts3.vidusskola())
    
elif tips2 == 1:
    uzvards1 = input("Ievadiet 2. skolotāja uzvārdu: ")
    klase1 = input("Ievadiet skolotāja klasi: ")
    skaits1 = int(input("Ievadiet skolotāja stundu skaitu: "))
    objekts4 = SakumskolasSkolotajs(uzvards1, skaits1, klase1)
    print(objekts4.sakumsskola())


else:
    print("Nav pareizi ievadīti dati.")

    


