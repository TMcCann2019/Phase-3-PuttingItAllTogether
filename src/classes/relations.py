# sandbox environment for testing purposes

from Makeup import Makeup
from People import People
from Purchase import Purchase

#Makeup objects
lipstick1 = Makeup("Pat McGrath", "lipstick")
lipstick2 = Makeup("Elf", "lipstick")
eyeshadow1 = Makeup("Clinique", "eyeshadow")
mascara1 = Makeup("ELF", "mascara")

#People objects
person1 = People("Morgan Freeman", 87)
person2 = People("Bruce Willis", 75)
person3 = People("Barry Allen", 32)

#Purchase objects
purchase1 = Purchase(lipstick1, person1, "2020-01-01")
purchase2 = Purchase(lipstick2, person2, "2020-01-02")
purchase3 = Purchase(mascara1, person3, "2020-01-02")
purchase4 = Purchase(eyeshadow1, person1, "2020-01-04")
purchase5 = Purchase(lipstick1, person2, "2020-01-01")
purchase6 = Purchase(lipstick2, person3, "2020-01-01")
purchase7 = Purchase(lipstick1, person3, "2020-01-01")

#Prints
print(lipstick1)
print(purchase1.makeup_item.brand)
print(lipstick1._owners)

#sandbox
print(Makeup.get_unique_types())
print(Purchase.get_most_popular_brand())