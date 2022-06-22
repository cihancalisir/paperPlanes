import torch
import cv2

def loadmodel(showResults=False):
    # load model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp2/weights/best.pt', force_reload=True)
    model.conf = 0.6  # model confidence >= 0.5
    model.classes = 0 # only plane class
    if showResults:
        im = cv2.imread(
            'test/images/Paper-Airplane-Trick-Shots-_-That-s-Amazing_mp4-11_jpg.rf.fcfd738f743387a7c0a503fcff9c1a6a.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)
        img = [im]
        results = model(img) # pass YOLO-v5 model for detection
        results.show() # show a img with detected contours
        print(results.pandas().xyxy[0]) # print result as a dataframe
    return model