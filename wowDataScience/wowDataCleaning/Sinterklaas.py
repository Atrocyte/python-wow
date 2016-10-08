class Sinterklaas:
    def zingEenLied(self):
        print("Bork bork bork")

Sinterklaas().zingEenLied()

class Pieterbaas:
    kleur = ""
    def zingEenLied(self):
        print("Knaft Knaft Knaft")

    def bekenKleur(self):
        print(self.kleur + " " +self.kleur + " " +self.kleur)

Pieterbaas().zingEenLied()
piet = Pieterbaas()
piet.kleur = "geel"
piet.bekenKleur()
piet.kleur = "groen"
piet.bekenKleur()
