from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from PIL import Image

import os 

app = QApplication([])
win  = QWidget()

#TODO create widgets
lb_image = QLabel("Image")
btn_dir = QPushButton("Folder")
lw_files = QListWidget()
 
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")

#TODO create layouts
row = QHBoxLayout()          # Main line
col1 = QVBoxLayout()         # divided into two columns
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # in the first - directory selection button
col1.addWidget(lw_files)     # and file list
col2.addWidget(lb_image, 95) # in the second - image
row_tools = QHBoxLayout()    # and button bar
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

#TODO choose the directory 
workdir = ''

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

# * create an ImageProcessor() class 
class ImageProcessor():
    def __init__(self):
        self.image = None 
        self.dir = None
        self.filename = None 
        self.save_dir = "Modified/"
    #* load image file to the self.image variable
    def loadImage(self, filename):
        self.filename = filename 
        fullname = os.path.join(workdir, self.filename)
        self.image = Image.open(fullname)

    #* show the selected image
    def showImage(self, path):
        lb_image.hide()
        pixmapImage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        # * w = lb_image.width() 
        # * h = lb_image.height() 
        pixmapImage = pixmapImage.scaled(w,h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapImage)
        lb_image.show()

    #TODO define a save Image function
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path)) or not(os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename) 
        self.image.save(fullname)
    
    def do_mirror(self):
        #TODO change this line base on the function 
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)

        # ! keep this part for every other function
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_bw(self):
        #TODO change this line base on the function 
        self.image = self.image.convert("L")

        # ! keep this part for every other function
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    

#TODO show the image
# * define showChosenImage() function
def showChosenImage():
    if lw_files.currenRow() >= 0:
        imagefile = lw_files.currentItem().text()
        imgProc.loadImage(imagefile)
        imgProc.showImage(os.path.join(workdir, imagefile))

imgProc = ImageProcessor()

lw_files.currentRowChanged.connect(showChosenImage)
#TODO connect buttons
btn_flip.clicked.connect(imgProc.do_mirror)
btn_bw.clicked.connect(imgProc.do_bw)


win.show()
app.exec()