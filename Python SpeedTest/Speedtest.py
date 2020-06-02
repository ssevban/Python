import speedtest
 
 
s = speedtest.Speedtest()
print(f"İndirme Hızı: {s.download()}")
print(f"Yükleme Hızı: {s.upload()}")

input()