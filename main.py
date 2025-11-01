import pandas as pd

#csv'nin olduğu dosya yolunu yazmak gerekiyor
veri = pd.read_csv("data/yt_sports_channels_stats.csv")

first =veri.head()
print(first)

bilgi = veri.info()
print(bilgi)

nan = veri.isna().sum()
print(nan)

veri["start_date"] = pd.to_datetime(veri["start_date"], errors="coerce")
veri.info()
