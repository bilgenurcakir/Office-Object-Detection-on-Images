from ultralytics import YOLO
import cv2
import os


IMAGE_PATH = "test4.jpg"   # Tahmin yapılacak resim
MODEL_PATH = "best.pt"    # Eğitilmiş model
CONF_THRESHOLD = 0.4      # Güven eşiği
BOX_THICKNESS = 4
FONT_SCALE = 1.0
FONT_THICKNESS = 2


#modeli al

model = YOLO(MODEL_PATH)


img = cv2.imread(IMAGE_PATH)

if img is None:
    print("❌ Resim bulunamadı!")
    exit()

# tahmin
results = model(img, conf=CONF_THRESHOLD)


#nesne varsa

if results[0].boxes is None or len(results[0].boxes) == 0:
    print("❌ Hiç nesne bulunamadı")
    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()


#kutu ciz

for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = float(box.conf[0])
    cls_id = int(box.cls[0])
    label = model.names[cls_id]

    text = f"{label} {conf:.2f}"


    cv2.rectangle(
        img,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        BOX_THICKNESS
    )


    (w, h), _ = cv2.getTextSize(
        text,
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        FONT_THICKNESS
    )


    cv2.rectangle(
        img,
        (x1, y1 - h - 15),
        (x1 + w + 10, y1),
        (0, 255, 0),
        -1
    )


    cv2.putText(
        img,
        text,
        (x1 + 5, y1 - 7),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        (0, 0, 0),
        FONT_THICKNESS
    )


# kaydet ve çiz

output_path = "output.jpg"
cv2.imwrite(output_path, img)

print(f"✅ Tahmin yapıldı ve kaydedildi: {output_path}")

cv2.imshow("Detection Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()