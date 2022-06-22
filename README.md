**Paper Plane Detection with YOLOv5** 

Follow the steps below to run the program that detects paper airplanes \
 with YOLOv5.

a.) Build hardreset container on machine AY.

  ````python
pip install -r requirements.txt
  ````
b.) Build hardreset container on machine AY.

  ````python
python main.py
  ````

To train your model with custom data, use a data labelling tool like [roboflow](https://app.roboflow.com/chn-lghf8) and save your \
data in YOLOv5-PyTorch format. This format split data imgs and txts which has bbow coordinates \
with class ID to train/valid/test folder and creates data.yaml to give data paths to YOLOv5 model. \

If you created data, go to the [project](https://drive.google.com/drive/folders/1f6CqA6WaNmoNv985smUoA1q07_Tdu3hu?usp=sharing) 
and update train, valid and test folder. \
 Run "YOLOv5_paperPlaneDetection.ipynb" and save your model weights from "./yolov5/runs/train/expX/weights/best-last.pt" \
to local and add project folder. Update your weight path in "loadmodel.py".


