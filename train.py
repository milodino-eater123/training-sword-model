from roboflow import Roboflow
from ultralytics import YOLO

path = 'None'

model = YOLO('yolov8n-pose.pt')
results = model.train(data='./path/to/coco8-pose.yaml', epochs=100, imgsz=640)