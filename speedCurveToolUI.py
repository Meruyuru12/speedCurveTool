try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
	from PySide6.QtGui import QIntValidator
	import maya.cmds as cmds
	import maya.mel as mel

except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
	from PySide2.QtGui import QIntValidator
	import maya.cmds as cmds
	import maya.mel as mel

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
		self.imagePixmap01 = QtGui.QPixmap(f"{RESOURCES_PATH}/images/speedCurveLogo.png")
		scaled_pixmap01 = self.imagePixmap01.scaled(
			QtCore.QSize(600,200),
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
		self.curveCreatorButton.setStyleSheet(config.CURVEHOVERBUTTON)
		self.addAttributesButton.setStyleSheet(config.ADDATTRHOVERBUTTON)
		self.connectionEditorButton.setStyleSheet(config.CONNECTHOVERBUTTON)
		self.exitButton.setStyleSheet(config.EXITHOVERBUTTON)
		
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
		self.countName = ""
		self.num = 1
		self.colorRed = 0
		self.colorGreen = 0
		self.colorBlue = 0

		self.setWindowTitle("CurveCreatorTool")
		self.resize(350,400)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet("""
			background-color : #76799C;
			font-family : "Comic Sans MS", cursive;
			color : White;
		""")

		self.shapesLabel = QtWidgets.QLabel("Select shape")
		self.shapesLabel.setStyleSheet(
			'''
			background-color: 0;
			color : White;
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
		self.primitiveListWidgets.setStyleSheet(
			'''
			background-color : White; 
			color : Black;
			font-size : 8px;
			font-family : "Comic Sans MS", cursive;
			'''
			)
		self.mainLayout.addWidget(self.primitiveListWidgets)


		self.shapesLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.shapesLayout)

		self.colorLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.colorLayout)

		self.colorPickerButton = QtWidgets.QPushButton("Open Color Wheel")
		self.colorPickerButton.clicked.connect(self.pickColor)
		self.colorPickerButton.setStyleSheet("""background-color : #242E49""")

		self.colorDisplay = QtWidgets.QLabel()
		self.colorDisplay.setFixedSize(60, 60)
		self.colorDisplay.setStyleSheet("background-color: rgb(255,0,0);")

		self.colorLayout.addWidget(self.colorPickerButton)
		self.colorLayout.addWidget(self.colorDisplay)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)

		self.nameLabel = QtWidgets.QLabel("Name : ")
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet("background-color : #37415C")

		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.suffixSideLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.suffixSideLayout)

		self.sideComboBox = QtWidgets.QComboBox()
		self.sideLabel = QtWidgets.QLabel("Side : ")
		self.sideComboBox.addItems(config.SIDE)
		self.sideComboBox.setStyleSheet("background-color : #FDA481; color : Black")
		self.suffixLabel = QtWidgets.QLabel("Suffix : ")
		self.suffixComboBox = QtWidgets.QComboBox()
		self.suffixComboBox.addItems(config.SUFFIX)
		self.suffixComboBox.setStyleSheet("background-color : #FDA481; color : Black")

		self.suffixSideLayout.addWidget(self.sideLabel)
		self.suffixSideLayout.addWidget(self.sideComboBox)
		self.suffixSideLayout.addWidget(self.suffixLabel)
		self.suffixSideLayout.addWidget(self.suffixComboBox)

		self.groupCheckBox = QtWidgets.QCheckBox("CreateGroup")
		self.groupCheckBox.setStyleSheet("""color = White""")
		self.mainLayout.addWidget(self.groupCheckBox)

		self.constrainCheckBox = QtWidgets.QCheckBox("Constrain to Joint")
		self.constrainCheckBox.setStyleSheet("""color = White""")
		self.mainLayout.addWidget(self.constrainCheckBox)

		self.sizeLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.sizeLayout)

		self.sizeLabel = QtWidgets.QLabel("Size : ")
		self.sizeLineEdit = QtWidgets.QLineEdit("1")
		self.sizeLineEdit.setValidator(QIntValidator())
		self.sizeLineEdit.setStyleSheet("""background-color : #181A2F;color = White""")
		self.sizeLayout.addWidget(self.sizeLabel)
		self.sizeLayout.addWidget(self.sizeLineEdit)

		self.axisLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.axisLayout)

		self.axisLabel = QtWidgets.QLabel("Axis : ")
		self.XBTN = QtWidgets.QRadioButton("X")
		self.YBTN = QtWidgets.QRadioButton("Y")
		self.ZBTN = QtWidgets.QRadioButton("Z")
		self.YBTN.setChecked(True)
		self.axisRadio = QtWidgets.QButtonGroup()
		self.axisLayout.addWidget(self.axisLabel)
		self.axisLayout.addWidget(self.XBTN)
		self.axisLayout.addWidget(self.YBTN)
		self.axisLayout.addWidget(self.ZBTN)
		self.axisRadio.addButton(self.XBTN)
		self.axisRadio.addButton(self.YBTN)
		self.axisRadio.addButton(self.ZBTN)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		
		self.createButton = QtWidgets.QPushButton("Create")
		self.createButton.clicked.connect(self.doCreateCurve)
		self.createButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#B4182D"))

		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)
		self.backButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#54162B"))

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
		sizeQSpin = int(self.sizeLineEdit.text())
		inputAxis = self.axisRadio.checkedButton().text()
		check = self.groupCheckBox.isChecked()
		constrain = self.constrainCheckBox.isChecked()
		STIL.createCurve(name,side,suffix,curveShape,self.colorRed,self.colorGreen,self.colorBlue,sizeQSpin,inputAxis,check,constrain)

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
		self.setStyleSheet("""
			background-color : #577E89;
			font-family : "Comic Sans MS"; 
			cursive;color : White
			""")

		self.nameTypeLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameTypeLayout)

		self.nameLabel = QtWidgets.QLabel("Name : ")
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet("background-color : #6F9F9C;color : White")
		self.typeLabel = QtWidgets.QLabel("Type : ")
		self.typeComboBox = QtWidgets.QComboBox()
		self.typeComboBox.addItems(config.TYPE)
		self.typeComboBox.setStyleSheet("""background-color : #6F9F9C; color : White;""")
		self.nameTypeLayout.addWidget(self.nameLabel)
		self.nameTypeLayout.addWidget(self.nameLineEdit)
		self.nameTypeLayout.addWidget(self.typeLabel)
		self.nameTypeLayout.addWidget(self.typeComboBox)

		self.maxMinLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.maxMinLayout)

		self.maxLabel = QtWidgets.QLabel("Max : ")
		self.maxLineEdit = QtWidgets.QLineEdit()
		self.maxLineEdit.setValidator(QIntValidator())
		self.maxLineEdit.setStyleSheet("""background-color : #E2D8A5;color : Black""")
		self.minLabel = QtWidgets.QLabel("Min : ")
		self.minLineEdit = QtWidgets.QLineEdit()
		self.minLineEdit.setValidator(QIntValidator())
		self.minLineEdit.setStyleSheet("""background-color : #E2D8A5;color : Black""")
		
		self.maxMinLayout.addWidget(self.minLabel)
		self.maxMinLayout.addWidget(self.minLineEdit)
		self.maxMinLayout.addWidget(self.maxLabel)
		self.maxMinLayout.addWidget(self.maxLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		
		self.addButton = QtWidgets.QPushButton("Add")
		self.addButton.clicked.connect(self.doAddAttributes)
		self.addButton.setStyleSheet(config.GREENHOVERBUTTON.replace("#col","#DEC484"))

		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)
		self.backButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#E1A36F"))

		self.buttonLayout.addWidget(self.addButton)
		self.buttonLayout.addWidget(self.backButton)
	def goBack(self):
		self.close()
		run()
	def doAddAttributes(self):
		name = self.nameLineEdit.text()
		type = self.typeComboBox.currentText()
		maxValue = self.maxLineEdit.text()
		minValue = self.minLineEdit.text()
		STIL.addAttributes(name,type,maxValue,minValue)

class ConnectionEditorTool(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle("ConnectionEditorTool")
		self.resize(500,220)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			"""
				background-color : #FFDECA;
				font-family : "Comic Sans MS", cursive;
				color : Black;
			"""
			)

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
		self.outputLineEdit.setStyleSheet("""color : Blue;background-color : #F9B288""")
		self.inputLineEdit = QtWidgets.QLineEdit()
		self.inputLineEdit.setStyleSheet("""color : Red;background-color : #F9B288""")

		self.lineEditLayout.addWidget(self.outputLineEdit)
		self.lineEditLayout.addWidget(self.inputLineEdit)
		
		self.inputOutputButtonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.inputOutputButtonLayout)

		self.outputSelectButton = QtWidgets.QPushButton("Select")
		self.outputSelectButton.clicked.connect(self.selectOutPutLabel)
		self.outputSelectButton.setStyleSheet(config.GREENHOVERBUTTON.replace("#col","#DCEAF7"))

		self.outputCancelButton = QtWidgets.QPushButton("Clear")
		self.outputCancelButton.clicked.connect(self.clearOutputLabel)
		self.outputCancelButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#C4D6E7"))

		self.inputSelectButton = QtWidgets.QPushButton("Select")
		self.inputSelectButton.clicked.connect(self.selectInPutLabel)
		self.inputSelectButton.setStyleSheet(config.GREENHOVERBUTTON.replace("#col","#DCEAF7"))

		self.inputCancelButton = QtWidgets.QPushButton("Clear")
		self.inputCancelButton.clicked.connect(self.clearInputLabel)
		self.inputCancelButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#C4D6E7"))

		self.inputOutputButtonLayout.addWidget(self.outputSelectButton)
		self.inputOutputButtonLayout.addWidget(self.outputCancelButton)
		self.inputOutputButtonLayout.addWidget(self.inputSelectButton)
		self.inputOutputButtonLayout.addWidget(self.inputCancelButton)

		self.outputAttributeLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.outputAttributeLayout)

		self.outputAttributeLabel = QtWidgets.QLabel("Output Attributes : ")
		self.outputAttributeLineEdit = QtWidgets.QLineEdit()
		self.outputAttributeLineEdit.setStyleSheet("""color : Blue;background-color : #F7D379""")
		self.outputAttributeSelectButton = QtWidgets.QPushButton("Select")
		self.outputAttributeSelectButton.setStyleSheet(config.GREENHOVERBUTTON.replace("#col","#DCEAF7"))
		self.outputAttributeSelectButton.clicked.connect(self.selectOutputA)
		self.outputAttributeClearButton = QtWidgets.QPushButton("Clear")
		self.outputAttributeClearButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#C4D6E7"))
		self.outputAttributeClearButton.clicked.connect(self.clearOutputA)

		self.outputAttributeLayout.addWidget(self.outputAttributeLabel)
		self.outputAttributeLayout.addWidget(self.outputAttributeLineEdit)
		self.outputAttributeLayout.addWidget(self.outputAttributeSelectButton)
		self.outputAttributeLayout.addWidget(self.outputAttributeClearButton)

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

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		self.connectButton = QtWidgets.QPushButton("Connect")
		self.connectButton.clicked.connect(self.doConnection)
		self.connectButton.setStyleSheet(config.GREENHOVERBUTTON.replace("#col","#DCEAF7"))

		self.backButton = QtWidgets.QPushButton("Back")
		self.backButton.clicked.connect(self.goBack)
		self.backButton.setStyleSheet(config.REDHOVERBUTTON.replace("#col","#C4D6E7"))

		self.buttonLayout.addWidget(self.connectButton)
		self.buttonLayout.addWidget(self.backButton)

	def selectOutPutLabel(self):
		outputLabel = cmds.ls(sl=True)
		cmds.select(cl=True)
		self.outputLineEdit.setText(outputLabel[0])
	def selectInPutLabel(self):
		inputLabel = cmds.ls(sl=True)
		cmds.select(cl=True)
		self.inputLineEdit.setText(inputLabel[0])
	def selectOutputA(self):
		obj = cmds.ls(sl=True)[0]
		selectedAttb = mel.eval('channelBox -q -selectedMainAttributes mainChannelBox;')
		self.outputAttributeLineEdit.setText(selectedAttb[0])
	def clearOutputA(self):
		self.outputAttributeLineEdit.setText("")
	def clearInputLabel(self):
		self.inputLineEdit.setText("")
	def clearOutputLabel(self):
		self.outputLineEdit.setText("")
	def doConnection(self):
		output = self.outputLineEdit.text()
		outputAttr = self.outputAttributeLineEdit.text()
		input = self.inputLineEdit.text()
		inputTransform = self.transformRadio.checkedButton().text()
		inputAxis = self.axisRadio.checkedButton().text()
		STIL.connectionEditor(output,outputAttr,input,inputTransform,inputAxis)
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

