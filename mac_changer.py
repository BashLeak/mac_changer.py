#for linux
import os
import subprocess
import random

ata = ""
dene = os.listdir('/sys/class/net/')
dizi = []
tata = ""
dizia = [":"]

for i in range(10):
    i += 1
    dizi.append(random.randint(0,9))

    if (i%2 == 0):
      dizi.extend(dizia)

dizi.insert(0,0)
dizi.insert(1,0)
dizi.insert(2,":")
dizi.pop()

for i in dizi:

    tata = tata+str(i)

for i in dene:
    ata = ata+str(i)+" "

arayuz = input("mac adresini değiştirmek istediğiniz "+ata + " arayüzlerinden birini giriniz: ")

print("mac adresi "+tata+" dır")

while True:

    if arayuz in dene :

        subprocess.call(["ifconfig",arayuz,"down"])

        subprocess.call(["ifconfig",arayuz,"hw","ether",tata])

        subprocess.call(["ifconfig",arayuz,"up"])

        print("işlem başarıyla tamamlandı")
        break
    else:
        print("yanlış giriş yaptınız")
        arayuz = input(ata + "arayüzlerinden birini giriniz: ")
