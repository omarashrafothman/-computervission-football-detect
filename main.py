from ultralytics import YOLO

model = YOLO('yolov8n-football.pt')

model.predict('Real Madrid 3-2 AC Milan TEST VIDEO.mp4',save=True)

print("hello")