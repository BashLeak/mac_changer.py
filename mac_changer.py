#for linux
import os
import subprocess

ata = ""
dene = os.listdir('/sys/class/net/')

for i in dene:
    ata = ata+str(i)+" "

arayuz = input("mac adresini değiştirmek istediğiniz "+ata + "arayüzlerinden birini giriniz: ")

while True:

    if arayuz in dene :

        subprocess.call(["ifconfig",arayuz,"down"])

        subprocess.call(["ifconfig",arayuz,"hw","ether","00:34:87:44:12:92"])

        subprocess.call(["ifconfig",arayuz,"up"])

        print("işlem başarıyla tamamlandı")
        break
    else:
        print("yanlış giriş yaptınız")
        arayuz = input(ata + "arayüzlerinden birini giriniz: ")
