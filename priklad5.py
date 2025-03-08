class Osoba:
    def __init__(self):
        self.jmeno = None
        self.prijmeni = None
        self.rc = None
    
    def __str__(self):
        return f"Osoba(jmeno={self.jmeno}, prijmeni={self.prijmeni}, rc={self.rc})"
    
    def set_jmeno(self, jmeno):
        self.jmeno = jmeno
        return self
    
    def set_prijmeni(self, prijmeni):
        self.prijmeni = prijmeni
        return self
    
    def set_rc(self, rc):
        self.rc = rc
        return self

if __name__ == "__main__":
    print(Osoba().set_jmeno("Tomas").set_prijmeni("Novak").set_rc("123456/7890"))


