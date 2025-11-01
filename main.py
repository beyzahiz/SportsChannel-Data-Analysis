import pandas as pd

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
print(veri.head())
print(veri.info())

