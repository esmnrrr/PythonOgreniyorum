#Python dinamik olarak yazilan bir programlama dili. Yani bir degiskeni herhangi bir ture esitleyebilirz.

#x = 1 dinamik                  int x = 1 static in java
#y = "Esmanur" dinamik          str y = "Esmanur" static in java 

print("Hello stupid World!")

#VERI TIPLERI
#1-integer : tam sayi degerleri
a = 1

#2-string : "" icine ya da '' icine yazilan herhangi bir sey 
b = "Selam cnmm"
print(b[0:5])
print(b.upper())
print(b.replace("cnmm", "canim"))
print(b.split()) #icine yazilana gore metni ayirir

x = 22
y = "Benim yasim maalesef ki {}"
z = ";/"
print(y.format(x), z)

#3-float : virgullu sayilar
c = 3,33

#4-complex : sayi ve harfin birlikte yazildigi tip
d = 4j

#5-list
e = [1,2,3]
e[0]
e.clear()
e.append(33)
e.insert(0, 333)
print(e)

#6-tuple : icerisinde manipulasyon yapilamayan sdc index numaralarini bulabilecegimiz listelerdir
f = ("elma", "armut", "muz")
index1 = tuple.index("muz")
print(index1)

#7-range
g = range(9)

#8-dictionary
h = {"name":"Esmanur", "surname":"Tetik"}

#9-set
i = {1, 2, 3}
j = {3, 4, 5}
result = i | j #birlesim kumesi (and op) ortak elamanlar tekrar yazilmaz kumelerde oldugu gibi
result = i & j #kesisim kumesi 

#Logical Data Type 10-bool
k = True or False
print(10>9)

#Ondalik yuvarlama
l = int(3.3)
print(k)
