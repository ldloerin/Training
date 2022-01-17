class Ausnahme:
    def rechne(self):
        while True:    
            try:
                z1 = float(input("Bitte die erste Zahl eingeben:\n"))    
                z2 = float(input("Bitte die zweite Zahl eingeben:\n"))    
                erg = z1 / z2
                print(erg)

            except ValueError:
                print("Bitte nur Zahlen eingeben")
            except ZeroDivisionError:
                print("Die zweite Eingabe darf nicht 0 sein")
            if(input("Ende mit q - weiter mit jeder anderen Taste: ")=="q"):             
                break
                
        print("Ende der Berechnungen")
        
