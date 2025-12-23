from ultralytics import YOLO
import cv2

# Modeli yükle
model = YOLO("best.pt")

# Kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

print("📸 Fotoğraf çekmek için 's'")
print("❌ Çıkmak için 'q'")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        img = frame.copy()
        print("Fotoğraf çekildi")
        break

    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()
cv2.destroyAllWindows()

# ==============================
# MODEL TAHMİNİ
# ==============================

results = model(img, conf=0.4)  # ❗ kritik satır

if len(results[0].boxes) == 0:
    print("❌ Hiç nesne bulunamadı")

for box in results[0].boxes:
    cls_id = int(box.cls.item())
    conf = float(box.conf.item())
    label = model.names[cls_id]

    # ekstra güvenlik
    if conf < 0.4:
        continue

    x1, y1, x2, y2 = map(int, box.xyxy[0])

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(
        img,
        f"{label} {conf:.2f}",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

cv2.imshow("Detection Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()