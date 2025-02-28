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

#6-tuple
f = {1,2,3}

#7-range
g = range(9)

#8-dictionary
h = {"name":"Esmanur", "surname":"Tetik"}

#9-set
i = ()

#Logical Data Type 10-bool
j = True or False
print(10>9)

#Ondalik yuvarlama
k = int(3.3)
print(k)