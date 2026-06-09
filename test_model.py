from ultralytics import YOLO

model = YOLO('path/to/best.pt')

results = model('image.png')

print(results)