from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap # TODO import screen-optimised

import os
from PIL import Image 
from PIL import ImageFilter #TODO import image filter library 

app = QApplication([])
win = QWidget()

#create widgets
folder_btn = QPushButton("Folder")
file_lst = QListWidget()
img_lb = QLabel("Image")
left_btn = QPushButton("Left")
right_btn = QPushButton("Right")
mirror_btn = QPushButton("Mirror")
sharpen_btn = QPushButton("Sharpness")
bw_btn = QPushButton("Black&White")

#create layouts 
main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()

left_layout.addWidget(folder_btn)
left_layout.addWidget(file_lst)

right_layout.addWidget(img_lb, 80)
btn_row = QHBoxLayout()
btn_row.addWidget(left_btn)
btn_row.addWidget(right_btn)
btn_row.addWidget(mirror_btn)
btn_row.addWidget(sharpen_btn)
btn_row.addWidget(bw_btn)
right_layout.addLayout(btn_row)

main_layout.addLayout(left_layout, 20)
main_layout.addLayout(right_layout, 80)

win.setLayout(main_layout)

#* save the working directory
workDir = ""
#* adding functions
def chooseWorkDir():
	global workDir
	workDir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
	img_files = []
	for file in files:
		for ext in extensions:
			if file.endswith(ext):
				img_files.append(file)
	
	return img_files

def showFilenamesList():
	# let the user choose a folder
	chooseWorkDir()
	# take only the image files
	extensions = [".jpg", ".jpeg", ".png"]
	files = os.listdir(workDir)
	filter(files, extensions)

	# add items to list widget
	file_lst.clear() #TODO clear the space - make sure that it's blank
	file_lst.addItems(files)

folder_btn.clicked.connect(showFilenamesList)

#TODO create an ImageProcessor class
class ImageProcessor():
	def __init__(self): 
		self.image = None 			# * saving the images
		self.filename = None		# * current image name 
		self.currDir = None 		# * workDir
		self.saveDir = "Modified/"	# * save processed image

	def loadImage(self, filename):
		self.filename = filename 
		fullname = os.path.join(workDir, self.filename)
		self.image = Image.open(fullname)
	
	#TODO define a save Image function 
	def saveImage(self):
		path = os.path.join(workDir, self.saveDir) # /Desktop/Mandarin/Modified/
		if not (os.path.exists(path) or os.path.isdir(path)): 
			os.mkdir(path)
		self.image.save(os.path.join(path, self.filename)) # /Desktop/Mandarin/Modified/<img_file_name>.png

	
	#TODO photo editor function
	def do_bw(self):
		self.image = self.image.convert("L") # * change this line for different function

		# ! this part stays the same for all other function
		self.saveImage()
		self.showImage(os.path.join(workDir, self.saveDir, self.filename))
	
	def do_left(self):
		self.image = self.image.transpose(Image.ROTATE_90)

		# ! this part stays the same for all other function
		self.saveImage()
		self.showImage(os.path.join(workDir, self.saveDir, self.filename))

	def do_right(self):
		self.image = self.image.transpose(Image.ROTATE_)

		# ! this part stays the same for all other function
		self.saveImage()
		self.showImage(os.path.join(workDir, self.saveDir, self.filename))

	def do_sharp(self):
		self.image = self.image.filter(ImageFilter.SHARPEN)

		# ! this part stays the same for all other function
		self.saveImage()
		self.showImage(os.path.join(workDir, self.saveDir, self.filename))


	def showImage(self, path):
		img_lb.hide()
		pixmapImage = QPixmap(path)
		w, h = img_lb.width(), img_lb.height() 
		# w = img_lb.width()
		# h = img_lb.height()
		pixmapImage = pixmapImage.scaled(w, h, Qt.KeepAspectRatio) 
		img_lb.setPixmap(pixmapImage)
		img_lb.show()


def showImageHandler():
	if file_lst.currentRow() > 0:
		#TODO take the filename 
		filename = file_lst.currentItem().text()
		#TODO load image
		imgProc.loadImage(filename)
		#TODO show image
		imgProc.showImage(os.path.join(workDir, filename))


imgProc = ImageProcessor()

file_lst.currentRowChanged.connect(showImageHandler)
bw_btn.clicked.connect(imgProc.do_bw)
left_btn.clicked.connect(imgProc.do_left)
right_btn.clicked.connect(imgProc.do_right)









win.show()
app.exec()