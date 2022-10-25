import sys
import os

import numpy as np
import cv2

from pathlib import Path

ROOT_DIR = Path(".")

import mrcnn.config
import mrcnn.utils
from mrcnn.model import MaskRCNN


class MaskRCNNConfig(mrcnn.config.Config):
    NAME = "pretrained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NOM_CLASSES = 1 + 80
    DETECTION_MIN_CONFIDENCE = 0.6


def get_car_boxes(boxes, class_ids):
    car_boxes = []
    for i, box in enumerate(boxes):
        if class_ids[i] in [3, 8, 6]:
            car_boxes.append(box)
    return np.array(car_boxes)


# Lokalna ścieżka do zapisywania logów
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Lokalna ścieżka do pliku z przetrenowanym modelem
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

if not os.path.exists(COCO_MODEL_PATH):
    mrcnn.utils.download_trained_weights(COCO_MODEL_PATH)


IMAGE_DIR = os.path.join(ROOT_DIR, "images")

VIDEO_SOURCE = "https://www.youtube.com/watch?v=c38K8IsYnB0"

model = MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=MaskRCNNConfig())

# Wczytywanie przetrenowanego modelu
model.load_weights(COCO_MODEL_PATH, by_name=True)

parked_car_boxes = None
video_capture = cv2.VideoCapture(VIDEO_SOURCE)

size = (
    int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)

codec = cv2.VideoWriter_fource(*"DIVX")
output = cv2.VideoWriter("videofile masked.avi", codec, 30.0, size)

while video_capture.isOpened():
    success, frame = video_capture.read()
    if not success:
        break
    
    rgb_image = frame[:, :, ::-1]
    results = model.detect([rgb_image], verbose=0)

    x = results[0]

    car_boxes = get_car_boxes(["rois"], ["class_ids"])

    print("Samochody znalezione w ramce granicznej :")

    for box in car_boxes:
        print("Samochód: ", box)
        y1, x1, y2, x2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()


from twilio.rest import Client 
# importovanie biblioteki

#Dane dotyczące konta

twilio account_sid = 'Twilio SID'

twilio_auth_token= 'Token Twilio'

Twilio_source_phone_number = 'Numer telefonu'

#Tworzenie obiektu klienta

client Client (twilio_account_sid, twilio_auth_token)

#Wysyłanie wiadomości
message client.messages.create(
                            body = "Zwolnione miejsce parkingowe!",
                            from = twilio_source_phone_number,
                            to="Numer klienta końcowego")
