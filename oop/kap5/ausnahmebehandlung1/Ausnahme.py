class Ausnahme:
    def rechne(self):
        print("Eingabe Zahl 1")
        try:
            z1 = int(input())
            print(z1)
        except ValueError:
            print("Bitte eine Zahl eingeben")
        print("Das kommt immer")
