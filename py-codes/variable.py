# variable

h=13 # int tam sayi
o=42.13 # float ondalikli sayi
text="trs" # string metinsel ifade

text="python" # tip degistirmesi mumkun

print(h)
print(o)
print(text)

# variable casting: bir veri turunu baska bir veri tipine donusturmeye yarar
x=str(13) # metinsel olarak 13'u donusturdu
y=int(13.42) # tam sayi olarak donusturdu
z=float(13) # ondalikli sayi olarak donusturdu

print(x)
print(y)
print(z)

v="python 3.14.4"

# 'type' verilen degiskenin hangi veri turunde oldugunu soyleyen bir fonksiyon
print(type(z))
print(type(v))

# variable case sensitive/harfe duyarli degiskenler

# her ikisi ayni degil cunku biri buyu biri kucuk harf ile basladi
name="halil"
Name='atlas' # tek ' tirnakla yazdirma veya degisken atama islemi yapilabilir

# ---

adSoyad="halil hattab"

AdSoyad="halil hattab"

ad_soyad="halil hattab" # favorim

# tek bir satirla bir cok degisken olusturma ve degerleri atama:

x,y,z="halil", 1342, 19 # virgul ile ayirarak atama yapildi
i=j=k="selam dunya" # hepsine ayni degeri atadi

first_name=ad_soyad # degiskeni baska bir degiskene atama

print(x, y, z) # ayni anda yazdirma
