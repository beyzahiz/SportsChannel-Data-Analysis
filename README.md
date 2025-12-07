# 📊 SportsChannel Veri Analizi

Bu proje, YouTube’da yayın yapan spor kanallarına ait istatistikleri analiz ederek **kanal büyümesi, izlenme davranışları ve performans metrikleri** üzerine anlamlı çıkarımlar üretmeyi amaçlar.

Veri seti her kanal için aşağıdaki bilgileri içerir:

- Abone sayısı
- Toplam izlenme sayısı
- Video sayısı
- Kanal açılış tarihi
- Video başına ortalama izlenme
- İzlenme başına abone oranı

Proje, veri temizleme → veri dönüştürme → görselleştirme adımlarını içeren uçtan uca bir analiz süreci sunar.

---

## 🚀 Proje İçeriği

### 🔧 Veri İşleme Adımları

- Eksik değerlerin tespiti ve temizlenmesi  
- `start_date` değerlerinin datetime formatına dönüştürülmesi  
- Kanal yaşı (`channel_age`) hesaplanması  
- Yeni metriklerin türetilmesi:
  - `views_per_video`
  - `subs_per_view`
- Korelasyon matrisi oluşturulması  

---

## 📈 Üretilen Grafikler

Tüm grafik dosyaları **images/** klasöründe saklanmaktadır:

- **channel_age_vs_subs.png** — Kanal yaşı ve abone sayısı ilişkisi  
- **channel_age_vs_views.png** — Kanal yaşı ve toplam izlenme ilişkisi  
- **subscribers_vs_views.png** — Abone → izlenme ilişkisi  
- **correlation_matrix.png** — Tüm metrikler arası korelasyon haritası  

---

## 📂 Proje Klasör Yapısı
SportsChannel-Data-Analysis/
│
├── data/
│ └── yt_sports_channels_stats.csv
│
├── images/
│ ├── channel_age_vs_subs.png
│ ├── channel_age_vs_views.png
│ ├── subscribers_vs_views.png
│ └── correlation_matrix.png
│
├── src/
│ └── main.py
│
├── README.md
└── requirements.txt



---

## 🛠 Kullanılan Teknolojiler

- Python 3  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 🎯 Projenin Amacı

Bu proje, veri analizi ve veri görselleştirme yeteneklerini geliştirmek ve YouTube kanal performans dinamiklerini incelemek amacıyla hazırlanmıştır.  
Aynı zamanda portföyde sergilenebilecek profesyonel bir analiz örneği sunar.

---




