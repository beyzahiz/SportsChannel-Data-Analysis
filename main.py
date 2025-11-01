import pandas as pd

#csv'nin olduğu dosya yolunu yazmak gerekiyor
veri = pd.read_csv("data/yt_sports_channels_stats.csv")

first =veri.head()
print(first)

bilgi = veri.info()
print(bilgi)

nan = veri.isna().sum()
print(nan)

#start_date sütunundaki veriyi datetime tipine dönüştürdüm dönüşemeyenler NaT oldu
veri["start_date"] = pd.to_datetime(veri["start_date"], errors="coerce")
veri.info()

veri = veri.dropna(subset=["start_date"])
veri.shape
veri.info()
veri.head()

