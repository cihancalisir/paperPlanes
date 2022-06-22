import sys
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from uid import UID
from loadmodel import loadmodel
import imutils
import time

global app
global start

class MainWindow(QWidget):
    # class constructor
    def __init__(self, videopath=None):
        # call QWidget constructor
        super().__init__()
        self.baseUI = UID() # load GUI
        self.model = loadmodel() # load YOLO model
        self.baseUI.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.baseUI.START.clicked.connect(self.controlTimer)
        self.baseUI.PAUSE.clicked.connect(self.pause)
        self.baseUI.RESUME.clicked.connect(self.resume)
        self.baseUI.CLOSE.clicked.connect(self.close)

        self.video = 0 if videopath == None else videopath
        self.logic = 0
        self.value = 1

    def pause(self):
        self.timer.stop()

    def resume(self):
        self.timer.start(20)

    def close(self):
        sys.exit(app.exec_())

    def getPaperPlanes(self, image): # detect paper planes
        results = self.model([image])  # pass YOLOv5x model
        stop = time.time()
        try:
            results_bboxes = results.pandas().xyxy[0]  # convert dataframe
            results_bboxes = results_bboxes.values[:, :4].astype("int32")  # iloc only bbox coordinates from results

            for c in range(results_bboxes.shape[0]):
                xmin, ymin, xmax, ymax = results_bboxes[c][0], results_bboxes[c][1], results_bboxes[c][2], \
                                         results_bboxes[c][3]
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2) # draw bbox
                interval = stop - start
                fps = int((1 / interval))
                cv2.putText(image,"FPS: {}".format(str(fps)), (int((xmin+xmax)/2)-20, ymin-10), 0, 1, 255) # write FPS on bbox
        except:
            print("no plane detected")
            pass
        return image

    def viewCam(self):
        global start
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = imutils.resize(image, width=640)
        # convert image to RGB format 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        start = time.time()
        image = self.getPaperPlanes(image) # paper plane detection function

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.baseUI.imgLabel_1.setPixmap(QPixmap.fromImage(qImg))
    
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(self.video)
            self.cap.set(cv2.CAP_PROP_FPS, 60)
            # start timer
            self.timer.start(20)

        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()

def main(path=None):
    app = QApplication(sys.argv)
    mainWindow = MainWindow(videopath=path)
    mainWindow.show()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    main(path="./data/test.mp4") # to use camera, don't set "path", default is None
    





