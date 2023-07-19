# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:52:39 2023

@author: emrep
"""

# Pandas kütüphanesinin oluşturulma amacı ve numpy kütüphanesinden farkı;
# 1) Pandas dataframeleri kullanmak için hızlı ve etkilidir.
# *Dataframe derken tablolar halinde verileri depoladığımız satır ve sütunlar kastediliyor.
# 2) CSV ve text dosyalarını açıp inceleyip sonuçlarımızı bu dosya tiplerine rahat bir şekilde kaydedebiliriz.
# 3) Pandas kütüphanesi Dataframe'leri oluştururken gözden kaçan veya herhangi bir şekilde yazmadığımız değerler
# konusunda bize yardımcı olur.
# 4) Numpy kütüphanesinde gördüğümüz reshape() fonksiyonunu çok daha etkili bir şekilde kullanıp datayı(veriyi) daha
# etkili bir şekilde işleyebiliriz.
# 5) Numpy da gördüğümüz slicing ve indexing işlemlerini çok daha kolay bir şekilde yapabiliriz.
# 6) Time series data analizi işlemlerini çok daha kolay bir şekilde yapabiliriz.
# 8) Time series data derken de zamana bağlı olarak değişen veriyi kastederiz.
# 7) Ayrıca Pandas hız açısından optimize edilmiş hızlı bir kütüphanedir.
import pandas as pd
import numpy as np
dictionary={"Name":["Ali","Veli","Ahmet","Mehmet","Ayşe","Elif","Merve","Helin"],"Surname":["A","B","C","D","E","F",
                                                                                            "G","H"],"Age":[1,2,3,4,
                                                                                                            5,6,7,8]}
# Pandas olmasaydı
print(dictionary,"\n\n\n")
# Pandasla birlikte;
dataframe1=pd.DataFrame(dictionary)
print(dataframe1,"\n\n\n")
# Pandas kütüphanesinin sağladığı yararlara bakmak için lütfen kodu çalıştırınız.
# Pandas kütüphanesindeki pandas.DataFrame() fonksiyonu bize excel dosyası halinde veriyi döndürürken dizi_adı.head(n)
# fonksiyonu da bize verinin ilk n satırını(0-(n-1).index) döndürür. Eğer dizi_adı.head() fonksiyonunun içine hiçbir
# şey yazmazsak da bize varsayılan olarak ilk 5 satırı döndürür.
head=dataframe1.head(7)
head1=dataframe1.head()
print(head,"\n\n\n",head1,"\n\n\n")
# dizi_adı.tail(n) fonksiyonu ise bize verinin son n satırını döndürür. Eğer dizi_adı.tail() fonksiyonunun içine
# hiçbir şey yazmazsak varsayılan olarak son 5 satıırını döndürür.
tail=dataframe1.tail()
tail1=dataframe1.tail(3)
print(tail,"\n\n\n",tail1)
#%%
# Pandas Basic Methods
# dizi_adı.columns() metodu sütun isimlerini tek bir satır halinde döndürür.
# Object daata type'ı aslında string(dizge) datatype'ı ile eşdeğerdir.
dictionary={"Rakamlar":[0,1,2,3,4,5,6,7,8,9],"Harfler":['a','b','c','d','e','...','w','x','y','z'],"Şifre":["a0","b9",
                                                                                                            "c5","d3",
                                                                                                            "e8","f4",
                                                                                                            "w2","x1",
                                                                                                            "y7","z6"]}                                                                                                            
dataframe=pd.DataFrame(dictionary)
dataframe1=dataframe.columns
print(dataframe1)
dataframe2=dataframe.info()
print(dataframe2)
# Pandas kütüphanesindeki dataframe_adı.dtypes metodu sonuna parantez açıp kapatma işareti almaz.
dataframe3=dataframe.dtypes
print(dataframe3)
# Pandas kütüphanesindeki dataframe_adı.describe() metodu da sadece numeric(sayısal) columnları(featureları) alarak
# bu featurelardaki eleman sayısı,ortalama,standart sapma,minimum değer,birinci çeyreklik,medyan,3. çeyreklik ve
# maksimum değeri döndürür.
print(dataframe.describe())
#%%
# Indexing and slicing data frames
dictionary={"Rakamlar":[9,8,7,6,5,4,3,2,1,0],"Harfler":['a','b','c','d','e','...','w','x','y','z'],"Şifre":["a0","b9",
                                                                                                            "c5","d3",
                                                                                                            "e8","f4",
                                                                                                            "w2","x1",
                                                                                                            "y7","z6"]}                                                                                                            
dataframe=pd.DataFrame(dictionary)
# İstersek dataframeimizdeki sadece 1 sütunun yazılmasını da print(dataframe_adı[sütun_adı]) koduyla sağlayabiliriz.
# Bu durumda ilk sütun index numaralarını, diğer sütun ise içeriği gösterir.
print(dataframe["Rakamlar"])
print(dataframe["Harfler"])
# Yukarıdaki kodu istersek print(dataframe_adı.sütun_adı) koduyla da sağlayabiliriz.
print(dataframe.Rakamlar)
print(dataframe.Harfler)
# Hatta eğer istersek daha önceden oluşturulmuş dataframeimize yeni sütunlar ekleyebiliriz. Bunun yolu da
# aşağıdaki şekilde bir koddur.
dataframe["Yeni sütun"]=["f",'g','h','i','j','k','l','m','n','o']
dataframe["New_column"]=['p','q','r','s','t','u',-9,-1,-3,-7]
print(dataframe)
print(dataframe.New_column)
# print(dataframe.Yeni sütun)
# dataframedeki sütun isimlerini boşluklu bir şekilde tanımlarsak print(dataframe_adı.boşluklu_sütun_ismi) kodu 
# hata verir. Sadece print(dataframe_adı) dediğimizde bu sütunlara ulaşabiliriz.
print(dataframe.loc[2:7,"Şifre"])
# Eğer istenirse dataframedeki istediğimiz sütunun istediğimiz bölümünü başlangıç ve bitiş indislerini belirterek
# print(dataframe_adı.loc[ilk_indis:son_indis,sütun_adı]) koduyla döndürebiliriz. Bunun numpydaki listten tek
# farkı iki noktanın sağındaki indisin pandasta dahil edilip numpyda hariç tutlmasıdır. 
print(dataframe.loc[:,"Şifre"])
# Pandas kütüphanesi de numpy gibi boş bırakılmış indisleri ilk veya son indis olarak algılar. 
# İstenirse dataframe_adı.loc[başlangıç_satırı:bitiş_satırı,başlangıç_sütunu:bitiş_sütunu] diyerek dataframein
# istediğimiz kısmını da yazdırabiliriz.
print(dataframe.loc[3:5,"Harfler":"New_column"])
print(dataframe.loc[3:5,["Harfler","New_column"]])
# Görülebileceği üzere dataframe_adı.loc[] fonksiyonunda aralık belirtmek zorunda değiliz. İstersek sadece
# belirttiğimiz sütunların belirttiğimiz satırlarını da yazdırabiliriz.
# Dataframei ters çevirmek istersek dataframe_adı.loc[::-1,:] kodunu kullanmamız gerekir.
print(dataframe.loc[::-1,:])
print(dataframe.loc[::-1,"Harfler":"New_column"]) 
# Yani eğer istersek belli bir aralıktaki tüm sütunları ters çevirebiliriz.
# dataframe_adı.loc[başlangıç_satırının_indisi:bitiş_satırının_indisi,sütun_adı] yazarken sütun isimlerini
# yazdığımız yere dataframe.iloc[] fonksiyonunda ilgili sütunun indis numarasını yazmalıyız.
print(dataframe.iloc[::-1,1])
#%% filtering Pandas dataframe
# Filtering(filtreleme) işlemi Pandas dataframeimizdeki istediğimiz özelliklere sahip elemanları bu özellik 
# bakımından True ya da False boolean değerlerini almalarına göre sırasıyla döndürür. 
# Döndürme şekli yine solda indis numaraları, sağda ise bu indislerdeki elemanların istenen özellik bakımından 
# True ya da False değerleri olacak şekildedir.
dictionary={"Rakamlar":[9,5,4,7,8,6,1,0,3,2],"Harfler":['a','b','c','d','e','...','w','x','y','z'],"Şifre":["a0","b9",
                                                                                                            "c5","d3",
                                                                                                            "e8","f4",
                                                                                                            "w2","x1",
                                                                                                            "y7","z8"]}
dataframe=pd.DataFrame(dictionary)
print(dataframe)
dataframe["New_column"]=[-1,-8,0,-4,-2,-6,-9,-5,-3,-7] 
filtre1=dataframe.Rakamlar>5
print(filtre1)
# Numpyda tek boyutlu dizilere vektör, çok boyutlulara ise matris denirken Pandasta da çok sayıda sütuna sahip 
# serilere dataframe denirken tek bir sütuna sahip(indis numaralarını sütun saymıyoruz) serilere ise sadece seri 
# denir.
print(type(filtre1))
# Eğer dataframedeki sadece filtrelenmiş elemanların özelliklerini döndürmek istersek dataframe_adı[filtre_adı]
# şeklinde bir kod parçası kullanmalıyız. 
print(dataframe[filtre1])
filtre2=dataframe[filtre1].New_column<-3
# Eğer istersek ilk filtrelememizin sonucunu tekrar tekrar(istediğimiz kadar) filtreleyerek son kalan elemanları
# da döndürebiliriz. Yani dataframe_adı[1.filtre][2.fitre]... diyerek döndürürüz.
print(filtre2)
print(dataframe[filtre1][filtre2])
dataframe["New_feature"]=['a','c','f',978,'g',-54,'h','i','b','k']
filtre3=dataframe[filtre1][filtre2].New_feature>0
print(filtre3,"\n")
print(dataframe[filtre1][filtre2][filtre3])
# Hatta eğer istersek dataframe_adı[filtre1 & filtre2 & ...] şeklinde bir kullanım da yapabiliriz.
print("\n\n\n")
print(dataframe[filtre1 & filtre2 & filtre3])
# Eğer istenirse print(dataframe_adı[dataframe.sütun_adı>x]) koduyla dataframedeki istediğimiz sütunun elemanlarından 
# sadece belirlediğimiz değerden büyük veya küçük elemanların yazılmasını sağlayabiliriz. Bu durumda elemanların 
# indis numarasına göre elemanlar tanımladığımız bütün özellikleriyle birlikte yazılır.
# tanımlı olan bütün özellikleri görünür.
print(dataframe[dataframe.Rakamlar<4])
# Görülebileceği üzere dizgeleri küçüklük/büyüklük olarak karşılaştırdığımızda ASCII tablosundaki sıralamayı dikkate
# alarak bu tabloya göre daha önce gelen dizgeleri daha küçük kabul eder ve ona göre sonuç döndürür.  
print(dataframe[dataframe.Harfler<'b'])
print(dataframe[dataframe.Harfler>='w'])
print(dataframe[dataframe.Harfler<'w'])
print(dataframe[dataframe.Şifre<'d8'])
#%% List Comprehension


dictionary={"Rakamlar":[9,5,4,7,8,6,1,0,3,2],"Harfler":['a','b','c','d','e','...','w','x','y','z'],"Şifre":["a0","b9",
                                                                                                            "c5","d3",
                                                                                                            "e8","f4",
                                                                                                            "w2","x1",
                                                                                                            "y7","z8"]}
dataframe=pd.DataFrame(dictionary)
print(dataframe)
dataframe["New_column"]=[-1,-8,0,-4,-2,-6,-9,-5,-3,-7] 
dataframe["New_feature"]=['a','c','f',978,'g',-54,'h','i','b','k']
#Ortalamanın Pandasla bulunma şekli;
Ortalama_Rakam = dataframe.Rakamlar.mean()
print("Pandasla bulunan ortalama=",Ortalama_Rakam)
#Ortalamanın Numpyla bulunma şekli;
ortalama_rakam_np= np.mean(dataframe.Rakamlar)
print("Numpyla bulunan ortalama=",ortalama_rakam_np)
dataframe["Rakam_büyüklüğü"]=["Küçük" if Ortalama_Rakam>each else "Büyük" for each in dataframe.Rakamlar]
print(dataframe)

#for each in dataframe.Rakamlar:
#   if each > Ortalama_Rakam:
#        print("Büyük")
#    else:
#        print("Küçük")

print(dataframe.columns)

dataframe.columns = [each.lower() for each in dataframe.columns]
print(dataframe.columns)

for each in dataframe.columns:
    for each in each:
        if "_" == each:
            each = "*"
            print(dataframe.columns)
#%%
dictionary={"Rakamlar":[9,5,4,7,8,6,1,0,3,2],"Harfler":['a','b','c','d','e','...','w','x','y','z'],"Şifre":["a0","b9",
                                                                                                            "c5","d3",
                                                                                                            "e8","f4",
                                                                                                            "w2","x1",
                                                                                                            "y7","z8"]}
dataframe=pd.DataFrame(dictionary)
Ortalama_Rakam=dataframe.Rakamlar.mean() 
dataframe["New_column"]=[-1,-8,0,-4,-2,-6,-9,-5,-3,-7] 
dataframe["New_feature"]=['a','c','f',978,'g',-54,'h','i','b','k']                                      
dataframe["Rakam_büyüklüğü"]=["Küçük" if Ortalama_Rakam>each else "Büyük" for each in dataframe.Rakamlar]
print(dataframe) 
dataframe.columns = [each.lower() for each in dataframe.columns]
print(dataframe)
# transforming data                                                                                    
dataframe["list_comprehension"]=[each*3 for each in dataframe.new_column]
print(dataframe)
# apply metodu
def mult(rakamlar):
    return rakamlar*2
dataframe["apply_metodu"] = dataframe.rakamlar.apply(mult)
print(dataframe)

        

















































