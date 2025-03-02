#Kullanicidan alinan herhangi 3 bilgi ile Dict olustur
"""q1 = input("Isminiz: ")
q2 = int(input("Yasiniz: "))
q3 = input("Dogum yeriniz: ")

dict1 = {"isim" : q1, "yas" : q2, "dogum yeri" : q3}
print(dict1)"""

#Kullanicidan alinan 3 sayiyi kucukten buyuge sirala
"""sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))
sayi3 = int(input("sayi3: "))
list1 = [sayi1, sayi2, sayi3]
sayi1 = max(list1)
sayi2 = min(list1)
sayi3 = list1.remove(max(list1))
sayi3 = list1.remove(min(list1))
print(f"{sayi1} > {sayi3} > {sayi2}")"""

#Kullanicidan aldiginiz bilgilerle ona bir karsilama metni olusturun
"""q1 = input("Isminiz: ")
print(f"Hosgeldin {q1} :)")"""

#Duplicate iceren bir liste alalim ve duplicatelerin silinmis halini yazdiralim
list2 = [1, 2, 2, 3, 3, 3]
list2 = list(set(list2))
print(list2)