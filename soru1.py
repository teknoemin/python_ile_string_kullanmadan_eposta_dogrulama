import re

olanlar = "^[a-z0-9\._]+[@]\w+[.]\w{2,3}([.]\w{2})?$"
def eposta_adresi_nedir(eposta):
    if (re.search(olanlar, eposta)):
    	print("E-Posta formatı doğru!")
    else:
    	print("E-Posta formatı hatalı!")

eposta_adresi_nedir("ali.erbey@usak.edu.tr")