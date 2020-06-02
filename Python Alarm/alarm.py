#coding=utf8

# SEVBAN (:

import os

from datetime import datetime

saat = int(input("Alarmın Saati : "))
dakika = int(input("Alarmın Dakikası : "))


while (1 == 1):
    if (saat == datetime.now().hour and
        dakika == datetime.now().minute):
        print("\a") # Burada Windows Bildirim Sesi çıkar. Ama Siz os modülü ile istediğiniz 
                    # şarkıyı çalabilirsiniz 
        break
    else:
        pass


print("Alarm Çaldı!")

input()
