import json

class Osoba:
    def __init__(self, jmeno, prijmeni, rc, email=None):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rc = rc
        self.email = email

    def __str__(self):
        return f"Osoba(jmeno={self.jmeno}, prijmeni={self.prijmeni}, rc={self.rc})"
    
    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_json(cls, data):
        jmeno = data["jmeno"]
        prijmeni = data["prijmeni"]
        rodne_cislo = data["rodne cislo"]
        email = data["email"]
        return cls(jmeno, prijmeni, rodne_cislo, email)


if __name__ == "__main__":
    fp = open("konfigurace.json", "r")
    data = fp.read()
    jdata = json.loads(data)

    osoby = []

    for j in jdata:
        osoby.append(Osoba.from_json(j))

    print(osoby)