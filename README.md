# Office-Object-Detection-on-Images

Bu proje, **kendi oluşturduğum ve Roboflow’da etiketlediğim dataseti** kullanılarak nesne tespiti yapan bir modeli eğitmek ve bu modeli kameradan aldığı  görsellerlekullanmak amacıyla geliştirilmiştir ileride **react native uygulamasi haline getirilecektir.** Uygulama, fotoğraf çekip modeli çalıştırarak tespit edilen nesnenin sınıfını ekranda göstermektedir.

## Dosyaların Açıklamaları

### `model_train.ipynb`
- Kendi oluşturduğum dataset’i kullanarak modelimizi eğitir.
- Eğitim tamamlandığında **`best.py`** dosyası üretilir; bu dosya en iyi model ağırlıklarını içerir.

### `best.py`
- `model_train.ipynb` ile eğitilmiş model ağırlıklarını içerir.
- Modeli kullanarak görseller üzerinde nesne tespiti yapabilirsiniz.

### `main.py`
- Modeli kullanarak **tekil görsellerden nesne tespiti** yapar.
  
### server.py
- Modeli kullanarak **canlı kamera üzerinden nesne tespiti** yapar.

  [![Video’yu izle](https://img.youtube.com/vi/acMw_eLZSTk/maxresdefault.jpg)](https://youtu.be/acMw_eLZSTk)

