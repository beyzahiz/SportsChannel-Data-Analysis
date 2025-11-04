import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#csv'nin olduğu dosya yolunu yazmak gerekiyor
veri = pd.read_csv("data/yt_sports_channels_stats.csv")

#veri.head()
#veri.info()
nan = veri.isna().sum()
#print(nan)

#start_date sütunundaki veriyi datetime tipine dönüştürdüm dönüşemeyenler NaT oldu
veri["start_date"] = pd.to_datetime(veri["start_date"], errors="coerce")
veri.info()

#start_date'deki nan verileri sildim
veri = veri.dropna(subset=["start_date"]) 
# veri.shape
# veri.info()
# veri.head()

veri["start_date"] = veri["start_date"].dt.tz_convert(None) #saat dilimi bilgisini kaldırır
today = pd.Timestamp.today()
veri["channel_age"] = (today-veri["start_date"]).dt.days/365
veri["views_per_video"] = veri["view_count"] / veri["video_count"]
veri["subs_per_view"] = veri["subscriber_count"] / veri["view_count"]
#print(veri.head())
#print(veri.info())

#eksik değerleri temizliyorum
veri = veri.dropna(subset=["views_per_video", "subs_per_view"])
#print(veri.head())
#print(veri.info())

#Grafik çiziyorum
plt.scatter(veri["channel_age"], veri["subscriber_count"], color="r")
plt.xlabel("Kanal Yaşı (Yıl)")
plt.ylabel("Abone Sayısı")
plt.title("Abone-Kanal Yaşı Grafiği")
#plt.show()

plt.scatter(veri["channel_age"], veri["view_count"], color="b")
plt.xlabel("Kanal Yaşı (yıl)")
plt.ylabel("Toplam İzlenme Sayısı")
plt.title("İzlenme Sayısı - Kanal Yaşı İlişkisi")
#plt.show()

plt.scatter(veri["subscriber_count"], veri["view_count"], color="g")
plt.xlabel("Abone Sayısı")
plt.ylabel("Toplam İzlenme Sayısı")
plt.title("İzlenme Sayısı - Abone Sayısı İlişkisi")
#plt.show()

#Correlation
correlation = veri["subscriber_count"].corr(veri["view_count"])
print("Abone sayısı ile izlenme sayısı arasındaki korelasyon: ",correlation)

#Correlation matrixi
corr_matrix = veri[["subscriber_count","view_count","video_count", "channel_age", "views_per_video", "subs_per_view"]].corr()

#görselleştirme
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm",fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.show(block=True)