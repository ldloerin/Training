from Tier import *
class ProgrammKlasse:
    def main():
        print("Anzahl der Tiere: ", Tier.AnzahlTiere())
        susi = Tier()
        print("Anzahl der Tiere: ", Tier.AnzahlTiere())
        strolch = Tier()
        print("Anzahl der Tiere: ", Tier.AnzahlTiere())
        herb = Tier()
        print("Anzahl der Tiere am Ende (Abfrage für die Klasse): ", Tier.AnzahlTiere())
        print("Anzahl der Tiere am Ende (Abfrage für eine Instanz):", susi.AnzahlTiere())


    def __init__(self):
        ProgrammKlasse.main()
ProgrammKlasse()
