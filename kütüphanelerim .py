# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:09:43 2023

@author: emrep
"""
#%% numpy basics
# sum(),int(),float() gibi fonksiyonlar python'ın kendi söz diziminde varken bu fonksiyonların yetersiz kaldığı 
# yerlerde kullanılmak üzere komplex matematiksel işlemleri yapabilen fonksiyonlar bulunduran numpy kütüphanesi
# tanımlanmıştır.

# import ederken sadece import numpy demek yeterliyken programımızda daha kısa harf öbekleriyle ifade edeceksek
# import numpy dedikten sonra as diyip nasıl ifade edeceksek o şekilde bir kısaltma yapmamız gerekmektedir.
import numpy as np
dizi1=np.array([99,88,77,66,55,33,11,121]) # 1*8 vektör
# array oluşturmak için numpy kütüphanesindeki array() fonksiyonunu kullandık ve 1 satır,7 sütundan oluşan bir dizi
# yarattık.
dizi2=np.array([[1,3,5,7,9],[2,4,6,8,10]]) # Bu şekilde çok boyutlu diziler de oluşturabiliriz.
print(dizi1)
print(dizi2)
print(dizi1.shape)
print(dizi2.shape)
b=dizi1.reshape(4,2)
# reshape metodunun içindeki sayılar çarpımı dizinin eleman sayısına eşit olmalı.
# print(reshape(dizi2.reshape(3,4)))
print(b)
print(b.shape)
d3=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]],[[13,14],[15,16]]])
print(d3)
print("dimension(boyut)=",d3.ndim)
print("data type1=",dizi1.dtype.name+"\ndata type2=",dizi2.dtype.name+"\ndata type3=",d3.dtype.name)
print(d3.size)
print(type(d3))
e=np.zeros((3,7,2))
print(e)
e1=e.reshape(6,7)
print(e1)
print("Önceki boyut(en,boy,yükseklik gibi yani)=",e.ndim)
print("Sonraki boyut=",e1.ndim)
e1[2][3]=5 # Bunun yerine e1[2,3] de diyebiliriz.
e1[5,6]+=17
print(e1)
f=np.ones((4,1,5))
print(f)
f[2,0,3]*=5
print(f)
g=np.empty((5,3,2))
print(g) # 6.23042070e-307=6.23042070*pow(10,-307) gibi sayılar fazlasıyla küçük olduklarından python tarafından
# empty hükmünde kabul edilir.
h=np.arange(0,40,8) # numpy.arange fonksiyonu içine alığı ilk elemandan 2. elemana kadar olan sayıları 3. eleman
# kadar aralıklarla yazar.
print(h)
ı=np.arange(5,10,0.7)
print(ı)
i=np.linspace(0.3,7.7,13)
print(i)
# numpy.linspace fonksiyonu içindeki ilk elemandan 2. elemana kadar(2. eleman dahil olmak üzere) olan sayıları 
# doğrusal olarak aartacak şekilde yazar.
j=np.linspace(0.5,1.9,17)
print(j)
#%% numpy basic operations
import numpy as np
p=np.array([[2,3],[5,4],[6,7]])
k=np.array([[9,8],[11,12],[14,13]])
b=np.array([[7],[8]])
c=np.array([[9,8],[12,13]])
print("",b+c,"\n",b-c,"\n",b**7)
print(p+k)
print(p-k)
print(k**2)
print(np.sin(p))
print(b<8)
print(c>8)
# element wise product
print(p*k)
# matris product(matris çarpımı)
print(k.dot(c))
print(p.dot(b))
print(k.T)
print(p.dot(k.T))
print(np.exp(p))
a=np.random.random((6,5))
print(a)
print(a.sum())
print("",a.max(),"\n",a.min())
print(a.sum(axis=0))
# a.sum(axis=0) derken a matrisinin aynı sütunundaki tüm elemanları topla ve bunları 1 satırda ayrı sütunlara
# yaz demiş oluruz.
print(a.sum(axis=1))
# a.sum(axis=1) derken de matrisin aynı satırındaki elemanları topla ve bunları 1 satırda ayrı sütunlara yaz
# demiş oluruz.
print(np.sqrt(a))
# Yukarıda yazdığım fonksiyon a matrisindeki tüm elemanların karekökünü alıp yeni oluşan matrisi yazdırır.
print(np.square(a)) # a**2
# Bu fonksiyonda a matrisinin tüm elemanlarının karesini alıp yeni matrisi yazdırır.
# Python'da matris toplamı yapılacağında(sadece aynı boyuttaki matrisler toplanabilir.) a+b yerine np.add(a,b) de
# denebilir. 
print(np.add(p,k)) # Yani p+k demekle bunun arasında bir fark yoktur.
#%%
# indexing and slicing
# Spyder'ı kapatıp açınca daha önceden import edilen kütüphaneleri kullanacağımız yeni kodlar için tekrar import
# etmemiz gerekir.
import numpy as np
dizi1=np.array([1,5,8,3,9,0]) # vector: dimension=1
print(dizi1[0:6])
# Dizilerde dizi_adı[::"sayı"] dendiğinde sayının pozitif veya negatif olmasına göre baştan veya sondan başlanıp
# sayının mutlak değeri kadar aralıklarla dizinin elemanları arasında gezilir.
print(dizi1[::-2]) # Mesela bu fonksiyon dizi1'in sonuncu indisinden başlayarak dizi1'in elemanlarını 2'şer 2'şer 
# tarar ve [0 3 5] sonucunu konsola yazar.
print(dizi1[::-3]) # [0 8] sonucu döndürür.
print(dizi1[::3]) # Bu da aynı mantıkla ama bu sefer baştan başlayarak dizi1'in elemanlarını 3'er 3'er tarar.
dizi2=np.array([[1,3,7,9,11],[2,5,8,10,12]]) # matris: dimension=2
print(dizi2)
print(dizi2[0,2]) # Bu fonksiyon dizi2'deki index numarası 0 olan satırın index numarası 2 olan sütunundaki
# elemanı yazar.
print(dizi2[0][2]) # Yukarıdaki fonksiyon istenirse bu şekilde de yazılabilir, değişen bir şey olmaz.
print(dizi2[:,2:4]) # Eğer bir matrisin satırlarından istediğimiz bölümünün aynı matrisin sütunlarının istediğimiz 
# istediğimiz kısmıyla kesişimini bulmak istersek x ve y satırların başlangıç ve bitiş, z ve t de sütunların
# başlangıç ve bitiş indisi olmak üzere matris_adı[x:y,z:t] demeliyiz.
# Her ne kadar matris_adı[n][k]=matris_adı[n,k] olsa da aynı şey matris_adı[x:y,z:t]=matris_adı[x:y][z:t] için
# geçerli değildir. Yani matris_adı[x:y][z:t] fonksiyonu saçma sonuçlar türetebilir.
# print(dizi2[1:2][1:3]) # Mesela bunun gibi.
print(dizi2[1:2,1:3]) # Bu şekilde yapılırsa her zaman doğru sonuç verir.
print(dizi2[:,:])
#%%
# shape manipulation
import numpy as np
dizi1=np.array([[1,3,5],[2,4,6],[8,10,12],[9,11,13]])
print(dizi1)
# flatten
dizi2=dizi1.ravel()
print(dizi2) # ravel() fonksiyonu önceden tanımladığımız array(dizi)'i tek satırlı hale getirir.
d=dizi1.reshape(12,1) 
print(d) # reshape(x,y) fonksiyonu ise x*y=dizinin eleman sayısı olmak koşuluyla x satır sayısı, y de sütun
# sayısı olmak üzere diziyi yeniden şekillendirir ama dizinin başlangıçtaki adı başka satırda yeniden
# çağırıldığında yine başlangıçtaki hali döner.
e=d.T
print(e) # .T fonksiyonu da dizinin transpozunu(devriğini)(sütunlar satır, satırlar sütun olmuş hali) alır. 
print(e.shape) # .shape fonksiyonu dizinin satır ve sütun sayısını bularak (satır_sayısı,sütun_sayısı) şeklinde 
# sonuç döndürür.
f=np.array([[2,5],[8,11],[14,17],[20,23],[26,29],[32,35]])
print(f)
f.resize(2,6) # resize(yeni_şekil) metodu diziyi yeniden şekillendirir ve dizinin başlangıçtaki adı
# çağırıldığında dizinin yeni şekli döner. Yani daha az değişken ismine ihtiyaç duyulur.
print(f)
print(dizi1)
dizi3=np.array([[2,4,7,15],[5,11,23,37]])
print(dizi3)
dizi3.reshape(4,2) 
print(dizi3)
dizi3.resize(4,2)
print(dizi3)
# Görülebileceği üzere reshape() fonksiyonundan sonra aynı isimle diziyi yazdırınca dizinin eski hali yazılırken
# resize() fonksiyonundan sonra yazdırınca şekli değişmiş hali yazılır.

#%%
# stacking arrays
import numpy as np
dizi1=np.array([[3,7,11],[4,8,12]])
dizi2=np.array([[5,9,13],[6,10,14]])
# Dizileri birleştirmenin 2 yolu var. 
# İstersek böyle yani numpy.vstack() fonksiyonunu kullanarak vertical(dikey) olarak; 
# [[3,7,11]
#  [4,8,,12]
# [[5,9,13]
#  [6,10,14] 
dizi3=np.vstack((dizi1,dizi2))
print(dizi3)
# İstersek de aşağıdaki şekilde yani numpy.hstack() fonksiyoynunu kullanarak horizontal(yatay) olarak
# birleştirebiliriz.
# [[3,7,11,5,9,13]
#  [4,8,12,6,10,14]]
dizi4=np.hstack((dizi1,dizi2))
print(dizi4)
#%%
# convert and copy array
import numpy as np
dizi1=np.array([5,12,19])
dizi2=np.array([[7,13,18],[20,23,25]])
print(dizi1<dizi2)
liste1=[1,2,4]
print("listenin ilk hali=",liste1)
k=np.array(liste1) # Bu şekilde liste1 adındaki listeyi k adındaki diziye dönüştürdük.
print("listenin yeni hali(k)=",k)
d1=np.hstack((dizi1,k))
d2a=np.vstack((dizi1,k))
# d1=np.hstack((dizi2,k)) dizi2 nin 2, k nın 1 satırı olduğundan ötürü dizi2 ve k yatay olarak birleştirilemez.
d2b=np.vstack((dizi2,k)) 
print("dizi1 ile k nın yatay birleşimi:\n",d1,"\ndizii1 ile k nın dikey birleşimi:\n",d2a,"\ndizi2 ile k nın dikey"
      " birleşimi=\n",d2b)
liste2=list((dizi2)) # Bu şekilde dizi2 adındaki diziyi liste2 adındaki listeye dönüştürmüş olduk.
print(liste2)
a=np.array([['e','f'],['g','h']])
b=a
c=a
d=a
c[1,1]='v' # Sadece d dizisinin index numarası 1 olan satırıyla sütununun kesiştiği yerdeki elemanını değiştirerek
# diğer matrislerin hepsini de değiştirmiş olduk. Bunun sebebi numpy.array() fonksiyonuyla bellekte bir yer ayırıp
# bu fonksiyonun eşitlendiği a matrisi ve a matrisinin eşitlendiği b,c ve d matrislerini bu bölgede depolamamızdı.
# Yani aslında a,b,c ve d integer,character gibi birer değişken değil, bellekte ayrılan bölgeye verilmiş farklı
# adlardı.  
print("İlk dizi:")
print(b)
print(d)
print(a)
print(c)
# İstenirse matrisler aşağıda görüldüğü gibi birbirine kopyalanarak bellekte farklı yerler tutan diziler
# oluşturulabilir. Böylece yukarıdaki gibi tanımlanmış olan a,b,c ve d matrislerinden hangisi değiştirilirse
# değiştirilsin bu değişiklik sadece o matrisle sınırlı kalır.
i=np.array([['m','n'],['o','p'],['q','r']]) 
j=i.copy()
k=i.copy()
l=i.copy()
k[1][1]='t'
print("İkinci dizi:")
print(j)
print(l)
print(i)
print(k)



































































































