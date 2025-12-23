# Office-Object-Detection-on-Images

Bu proje, **kendi oluşturduğun ve Roboflow’da etiketlediğin dataset** kullanılarak nesne tespiti yapan bir modeli eğitmek ve bu modeli bir **React Native** uygulamasında kullanmak amacıyla geliştirilmiştir. Uygulama, fotoğraf çekip modeli çalıştırarak tespit edilen nesnenin sınıfını ekranda göstermektedir.

## Dosyaların Açıklamaları

### `model_train.ipynb`
- Kendi oluşturduğun dataset’i kullanarak modelimzi eğitir.
- Eğitim tamamlandığında **`best.py`** dosyası üretilir; bu dosya en iyi model ağırlıklarını içerir.

### `best.py`
- `model_train.ipynb` ile eğitilmiş model ağırlıklarını içerir.
- Modeli kullanarak görseller üzerinde nesne tespiti yapabilirsiniz.

### `main.py`
- Modeli kullanarak **tekil görsellerden nesne tespiti** yapar.
- 
### server.py
- Modeli kullanarak **canlı kamera üzerinden nesne tespiti** yapar.
- 
  
