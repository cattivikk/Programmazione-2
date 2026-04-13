#classe
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        # incapsulamento
        self._eta = eta 

    def get_eta(self):
        return f"l'eta è di {self.nome} è di {self._eta} anni"

    def set_eta(self, valore):
        self._eta = valore

    #astrazione
    def saluta(self):
        print(f"ciao sono {self.nome}")

#ereditarietà
class Dipendente(Persona):
    def __init__(self, nome, cognome, eta, ufficio):
        super().__init__(nome, cognome, eta)
        self.ufficio = ufficio

    #polimorfismo
    def saluta(self):
        return f"{self.nome} sta lavorando nell'ufficio {self.ufficio}."

class Studente(Persona):
    def __init__(self, nome, cognome, eta, corso):
        super().__init__(nome, cognome, eta)
        self.corso = corso

    def saluta(self):
        print(f"ciao sono {self.nome} e studio {self.corso}")

#oggetti
dario = Dipendente("dario", "spadola", 31, "IT")
luca = Studente("luca", "rossi", 20, "biologia")
nonna = Persona("teresa", "galizia", 84)

print(dario.get_eta())
nonna.set_eta(57)
print(nonna.get_eta())
print(luca.saluta())
