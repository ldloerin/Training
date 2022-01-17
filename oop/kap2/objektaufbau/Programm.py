from Kunde import *
from Konto import *
kunde1 = Kunde("Hans","Dampf",42,"Mann","Milchstrasse 123, 666 Irgendwo", Konto(1000,"Girokonto"))
print(kunde1.vorname)
print(kunde1.konto)
print(kunde1.konto.kontostand)
kunde1.konto.einzahlen(123)
print(kunde1.konto.kontostand)
