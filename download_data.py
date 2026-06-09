from roboflow import Roboflow
from ultralytics import YOLO

my_api_key,my_id,my_proj_name = None,None,None

rf = Roboflow(api_key=my_api_key)
project = rf.workspace(my_id).project(my_proj_name)
dataset = project.version(1).download("yolov5")