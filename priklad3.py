class Osoba:
    def __init__(self, jmeno, prijmeni, rc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rc = rc
    
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Ucet:
    def __init__(self, osoba):
        self.__osoba = osoba
        self.__zustatek = 0
    
    @property
    def osoba(self):
        return self.__osoba

    @property
    def zustatek(self):
        return self.__zustatek
    
    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise Exception("zaporna hodnota")
        self.__zustatek = hodnota

    def __str__(self):
        return f"Ucet vlastni {self.osoba} a zustatek je {self.zustatek}"

if __name__ == "__main__":
    ucet = Ucet(Osoba().set_jmeno("Tomas").set_prijmeni("Novak").set_rc("123456/7890"))
    ucet.zustatek = 100
    print(ucet)
    osoba2 = Osoba("Martin", "Dvorak", "987654/3210")
    ucet.osoba = osoba2
    print(ucet)
    