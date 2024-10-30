import cv2

image_path = 'image.jpg'

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread(image_path)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)
print(faces)

for (x, y, w, h) in faces:
    print(f"Координаты лица: ({x},{y}), ({x},{y+h}), ({x+w},{y+h}), ({x+w},{y})")
