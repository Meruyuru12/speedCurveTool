try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
	from PySide6.QtGui import QIntValidator
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
	from PySide2.QtGui import QIntValidator
import importlib
import maya.OpenMayaUI as omui
import os 
from . import config
from . import speedCurveToolUtil as STIL
importlib.reload(config)
importlib.reload(STIL)

RESOURCES_PATH = os.path.join(os.path.dirname(__file__),'resources').replace("\\","/")
ICON_PATH = os.path.join(os.path.dirname(__file__),'resources',"icons").replace("\\","/")

class SpeedCurveTool(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.setWindowTitle("SpeedCurveTool")
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("background-color : qlineargradient(x1:0,y1:0,x2:0,y2:1,stop : 0 #BEA896,stop:1 #8D7B6C);")

		self.imageLabel01 = QtWidgets.QLabel()
		self.imagePixmap01 = QtGui.QPixmap(f"{RESOURCES_PATH}/images/mambo.png")
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
		self.curveCreatorButton.clicked.connect(self.runCurveCreatorButton)
		self.addAttributesButton = QtWidgets.QPushButton("Add Attributes")
		self.addAttributesButton.clicked.connect(self.runAddAttributesButton)
		self.connectionEditorButton = QtWidgets.QPushButton("Connection Editor")
		self.connectionEditorButton.clicked.connect(self.runConnectionEditorButton)
		self.exitButton = QtWidgets.QPushButton("Exit")
		self.exitButton.clicked.connect(self.close)
		self.curveCreatorButton.setStyleSheet(

			'''
				QPushButton {
					background-color : #DEB68E;
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
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
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
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
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
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
					color : white;
					border-radius : 10px;
					font-size : 20px;
					padding : 8px;
					font-family : "Comic Sans MS", cursive;
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

	def runProgram(self, name):
		global ui
		ui = name
		try :
			ui.close()
		except:
			pass

		ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
		if ui == "CurveCreatorTool":
			ui = CurveCreatorTool(parent = ptr)
			ui.show()
		elif ui == "AddAttributesTool":
			ui = AddAttributesTool(parent = ptr)
			ui.show()
		elif ui == "ConnectionEditorTool":
			ui = ConnectionEditorTool(parent = ptr)
			ui.show()

	def runCurveCreatorButton(self):
		self.close()
		self.runProgram("CurveCreatorTool")

	def runAddAttributesButton(self):
		self.close()
		self.runProgram("AddAttributesTool")

	def runConnectionEditorButton(self):
		self.close()
		self.runProgram("ConnectionEditorTool")

class CurveCreatorTool(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.num = 1
		self.colorRed = 0
		self.colorGreen = 0
		self.colorBlue = 0

		self.setWindowTitle("CurveCreatorTool")
		self.resize(350,400)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		# self.setStyleSheet("background-color : qlineargradient(x1:0,y1:0,x2:0,y2:1,stop : 0 #B1DBA4,stop:1 #667D5F);")

		self.shapesLabel = QtWidgets.QLabel("Select shape")
		self.shapesLabel.setStyleSheet(
			'''
			background-color: 0;
			color : #000000;
			font-size : 20px;
			font-family : "Comic Sans MS", cursive;
			font-weight : bold;
			 '''
			 )
		self.shapesLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.shapesLabel)

		self.primitiveListWidgets = QtWidgets.QListWidget()
		self.primitiveListWidgets.setIconSize(QtCore.QSize(50,50))
		self.primitiveListWidgets.setSpacing(12)
		self.primitiveListWidgets.setViewMode(QtWidgets.QListView.IconMode)
		self.primitiveListWidgets.setMovement(QtWidgets.QListView.Static)
		self.primitiveListWidgets.setResizeMode(QtWidgets.QListView.Adjust)
		self.primitiveListWidgets.setStyleSheet('background-color : black;')
		self.mainLayout.addWidget(self.primitiveListWidgets)


		self.shapesLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.shapesLayout)

		self.colorLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.colorLayout)

		self.colorPickerButton = QtWidgets.QPushButton("Open Color Wheel")
		self.colorPickerButton.clicked.connect(self.pickColor)

		self.colorDisplay = QtWidgets.QLabel()
		self.colorDisplay.setFixedSize(60, 60)
		self.colorDisplay.setStyleSheet("background-color: rgb(0,0,0); border-radius: 4px;")

		self.colorLayout.addWidget(self.colorPickerButton)
		self.colorLayout.addWidget(self.colorDisplay)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)

		self.nameLabel = QtWidgets.QLabel("Name : ")
		self.nameLineEdit = QtWidgets.QLineEdit()

		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.suffixSideLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.suffixSideLayout)

		self.sideComboBox = QtWidgets.QComboBox()
		self.sideLabel = QtWidgets.QLabel("Side : ")
		self.sideComboBox.addItems(config.SIDE)
		self.suffixLabel = QtWidgets.QLabel("Suffix : ")
		self.suffixComboBox = QtWidgets.QComboBox()
		self.suffixComboBox.addItems(config.SUFFIX)

		self.suffixSideLayout.addWidget(self.sideLabel)
		self.suffixSideLayout.addWidget(self.sideComboBox)
		self.suffixSideLayout.addWidget(self.suffixLabel)
		self.suffixSideLayout.addWidget(self.suffixComboBox)


		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		
		self.createButton = QtWidgets.QPushButton("Create")
		self.createButton.clicked.connect(self.doCreateCurve)
		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)

		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.backButton)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = config.SHAPE_NAME
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f"{prim}.png")))
			# item.setText(None)
			self.primitiveListWidgets.addItem(item)

	def pickColor(self):
		color = QtWidgets.QColorDialog.getColor(QtGui.QColor(0, 0, 0), self)
		if color.isValid():
			r = color.redF()
			g = color.greenF()
			b = color.blueF()

			self.colorRed = r
			self.colorGreen = g
			self.colorBlue = b

			self.colorDisplay.setStyleSheet(
                f"background-color: rgb({color.red()}, {color.green()}, {color.blue()}); border-radius: 4px;")

	def doCreateCurve(self):

		name = self.nameLineEdit.text()
		side = self.sideComboBox.currentText()
		suffix = self.suffixComboBox.currentText()
		curveShape = self.primitiveListWidgets.currentItem().text()
		print("curveShape")
		STIL.createCurve(name,side,suffix,curveShape,self.colorRed,self.colorGreen,self.colorBlue,self.num)
	

	def goBack(self):
		self.close()
		run()

class AddAttributesTool(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle("AddAttributesTool")
		self.resize(500,200)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.nameTypeLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameTypeLayout)

		self.nameLabel = QtWidgets.QLabel("Name : ")
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.typeLabel = QtWidgets.QLabel("Type : ")
		self.typeComboBox = QtWidgets.QComboBox()
		self.typeComboBox.addItems(config.TYPE)
		self.nameTypeLayout.addWidget(self.nameLabel)
		self.nameTypeLayout.addWidget(self.nameLineEdit)
		self.nameTypeLayout.addWidget(self.typeLabel)
		self.nameTypeLayout.addWidget(self.typeComboBox)

		self.maxMinLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.maxMinLayout)

		self.maxLabel = QtWidgets.QLabel("Max : ")
		self.maxLineEdit = QtWidgets.QLineEdit()
		self.maxLineEdit.setValidator(QIntValidator())
		self.minLabel = QtWidgets.QLabel("Min : ")
		self.minLineEdit = QtWidgets.QLineEdit()
		self.minLineEdit.setValidator(QIntValidator())

		self.maxMinLayout.addWidget(self.maxLabel)
		self.maxMinLayout.addWidget(self.maxLineEdit)
		self.maxMinLayout.addWidget(self.minLabel)
		self.maxMinLayout.addWidget(self.minLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		
		self.addButton = QtWidgets.QPushButton("Add")
		self.addButton.clicked.connect(self.doAddAttributes)
		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)

		self.buttonLayout.addWidget(self.addButton)
		self.buttonLayout.addWidget(self.backButton)
	def goBack(self):
		self.close()
		run()
	def doAddAttributes(self):
		pass

class ConnectionEditorTool(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle("ConnectionEditorTool")
		self.resize(500,220)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)

		self.inputOutputLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.inputOutputLayout)

		self.outputLabel = QtWidgets.QLabel("Output")
		self.inputLabel = QtWidgets.QLabel("Input")

		
		self.inputOutputLayout.addWidget(self.outputLabel)
		# self.inputOutputLayout.addStretch()
		self.inputOutputLayout.addWidget(self.inputLabel)

		self.lineEditLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.lineEditLayout)
		self.outputLineEdit = QtWidgets.QLineEdit()
		self.inputLineEdit = QtWidgets.QLineEdit()

		self.lineEditLayout.addWidget(self.outputLineEdit)
		self.lineEditLayout.addWidget(self.inputLineEdit)
		
		self.inputOutputButtonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.inputOutputButtonLayout)

		self.outputSelectButton = QtWidgets.QPushButton("Select")
		self.outputCancelButton = QtWidgets.QPushButton("Cancel")
		self.inputSelectButton = QtWidgets.QPushButton("Select")
		self.inputCancelButton = QtWidgets.QPushButton("Cancel")

		self.inputOutputButtonLayout.addWidget(self.outputSelectButton)
		self.inputOutputButtonLayout.addWidget(self.outputCancelButton)
		self.inputOutputButtonLayout.addWidget(self.inputSelectButton)
		self.inputOutputButtonLayout.addWidget(self.inputCancelButton)

		self.transformLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.transformLayout)

		self.transformLabel = QtWidgets.QLabel("Transform : ")
		self.translateBTN = QtWidgets.QRadioButton("translate")
		self.rotateBTN = QtWidgets.QRadioButton("rotate")
		self.scaleBTN = QtWidgets.QRadioButton("scale")
		self.rotateBTN.setChecked(True)
		self.transformRadio = QtWidgets.QButtonGroup()
		self.transformLayout.addWidget(self.transformLabel)
		self.transformLayout.addWidget(self.translateBTN)
		self.transformLayout.addWidget(self.rotateBTN)
		self.transformLayout.addWidget(self.scaleBTN)
		self.transformRadio.addButton(self.translateBTN)
		self.transformRadio.addButton(self.rotateBTN)
		self.transformRadio.addButton(self.scaleBTN)
		self.transformRadio.buttonClicked.connect(self.doAddTransform)


		self.axisLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.axisLayout)

		self.axisLabel = QtWidgets.QLabel("Axis : ")
		self.XBTN = QtWidgets.QRadioButton("X")
		self.YBTN = QtWidgets.QRadioButton("Y")
		self.ZBTN = QtWidgets.QRadioButton("Z")
		self.ZBTN.setChecked(True)
		self.axisRadio = QtWidgets.QButtonGroup()
		self.axisLayout.addWidget(self.axisLabel)
		self.axisLayout.addWidget(self.XBTN)
		self.axisLayout.addWidget(self.YBTN)
		self.axisLayout.addWidget(self.ZBTN)
		self.axisRadio.addButton(self.XBTN)
		self.axisRadio.addButton(self.YBTN)
		self.axisRadio.addButton(self.ZBTN)
		self.axisRadio.buttonClicked.connect(self.doAddAxis)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		self.connectButton = QtWidgets.QPushButton("Connect")
		self.connectButton.clicked.connect(self.doConnection)
		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)

		self.buttonLayout.addWidget(self.connectButton)
		self.buttonLayout.addWidget(self.backButton)

	def doAddTransform(self):
		transformChecked = self.transformRadio.checkedButton()
		print(transformChecked.text())

	def doAddAxis(self):
		axisChecked = self.axisRadio.checkedButton()
		print(axisChecked.text())
	def doConnection(self):
		pass
	def goBack(self):
		self.close()
		run()

def run():
	global uiSpeedCurveTool
	try :
		uiSpeedCurveTool.close()
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	uiSpeedCurveTool = SpeedCurveTool(parent = ptr)
	uiSpeedCurveTool.show()