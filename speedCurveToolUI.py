try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import os 

ICON_PATH = os.path.join(os.path.dirname(__file__),'resources').replace("\\","/")
print(ICON_PATH)
class SpeedCurveTool(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.setWindowTitle("SpeedCurveTool")
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("background-color : qlineargradient(x1:0,y1:0,x2:0,y2:1,stop : 0 #BEA896,stop:1 #8D7B6C);")


		self.imageLabel01 = QtWidgets.QLabel()
		self.imagePixmap01 = QtGui.QPixmap(f"{ICON_PATH}/images/mambo.png")
		scaled_pixmap01 = self.imagePixmap01.scaled(
			QtCore.QSize(128,128),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)
		self.imageLabel01.setPixmap(scaled_pixmap01)
		self.imageLabel01.setStyleSheet("background-color: 0;")
		self.imageLabel01.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageLabel01)




		self.buttonLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.curveCreatorButton = QtWidgets.QPushButton("Curve Creator")
		self.addAttributesButton = QtWidgets.QPushButton("Add Attributes")
		self.connectionEditorButton = QtWidgets.QPushButton("Connection Editor")
		self.exitButton = QtWidgets.QPushButton("Exit")
		self.curveCreatorButton.setStyleSheet(

			'''
				QPushButton {
					background-color : #DEB68E;
					color = white;
					border-radius : 10px;
					font-size = 16px;
					padding : 8px;
					font-family : Papyrus;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #629C7D;
				}
				QPushButton:pressed {
					background-color : #B1F0CF;
				}
			'''
		)
		self.addAttributesButton.setStyleSheet(

			'''
				QPushButton {
					background-color : #A67B58;
					color = white;
					border-radius : 10px;
					font-size = 16px;
					padding : 8px;
					font-family : Papyrus;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #D4AD77;
				}
				QPushButton:pressed {
					background-color : #EDD3AF;
				}
				
			'''
		)
		self.connectionEditorButton.setStyleSheet(

			'''
				QPushButton {
					background-color : #5C3210;
					color = white;
					border-radius : 10px;
					font-size = 16px;
					padding : 8px;
					font-family : Papyrus;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #A48DB5;
				}
				QPushButton:pressed {
					background-color : #DDC2F2;
				}
				
			'''
		)
		self.exitButton.setStyleSheet(

			'''
				QPushButton {
					background-color : #AB483A;
					color = white;
					border-radius : 10px;
					font-size = 16px;
					padding : 8px;
					font-family : Papyrus;
					font-weight : bold;
				}
				QPushButton:hover {
					background-color : #A16480;
				}
				QPushButton:pressed {
					background-color : #DE8EB4;
				}
				
			'''
		)
		

		self.buttonLayout.addWidget(self.curveCreatorButton)
		self.buttonLayout.addWidget(self.addAttributesButton)
		self.buttonLayout.addWidget(self.connectionEditorButton)
		self.buttonLayout.addWidget(self.exitButton)


		self.mainLayout.addStretch()

def run():
	global ui
	try :
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = SpeedCurveTool(parent = ptr)
	ui.show()