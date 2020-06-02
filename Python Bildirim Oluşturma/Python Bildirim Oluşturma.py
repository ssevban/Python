# CREATED BY SEVBAN

# coding=utf8

modul_yuklemek_icin = "pip install win10toast"

 
from  win10toast import ToastNotifier
bildirim = ToastNotifier()
 
bildirim.show_toast("Başarabilirsin!","Asla Pes Etme!",duration=10)