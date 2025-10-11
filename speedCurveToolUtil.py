import importlib
from . import config
import maya.cmds as cmds
import maya.mel as mel
importlib.reload(config)

#ขาดใส่num
def createCurve(name,side,suffix,selectShape,r,g,b):	
	curveShape = selectShape
	countName = ""
	num =1

	LOCSELS = cmds.ls(sl=True)
	if not LOCSELS:
		if side == "":
			newname = f"{name}{num:02d}_{suffix}"
		else :
			newname = f"{side}_{name}{num:02d}_{suffix}"

		if config.SHAPE.get(curveShape):
			if name != "":
				curveName = mel.eval(config.SHAPE.get(curveShape))
				cmds.rename(curveName,newname)
				if newname == countName:
					num += 1
				else :
					num = 1
					countName = newname
				cmds.select(newname)

			else :
				curveName = mel.eval(config.SHAPE.get(curveShape))
				newCurveName = f"{curveShape}{num:02d}_{suffix}"
				cmds.rename(curveName,newCurveName)
				if newCurveName == countName:
					num += 1
				else :
					num = 1
					countName = newCurveName
				cmds.select(newCurveName)

		sels = cmds.ls(sl=True)

		if not sels:
			return
		cmds.setAttr(f"{sels[0]}.overrideEnabled",1)
		cmds.setAttr(f"{sels[0]}.overrideRGBColors",1)
		cmds.setAttr(f"{sels[0]}.overrideColorR",r)
		cmds.setAttr(f"{sels[0]}.overrideColorG",g)
		cmds.setAttr(f"{sels[0]}.overrideColorB",b)
		cmds.select(cl=True)
	else:	
		res = cmds.xform(LOCSELS, q = True, t = True, ws = True)
		if side == "":
			newname = f"{name}{num:02d}_{suffix}"
		else :
			newname = f"{side}_{name}{num:02d}_{suffix}"

		if config.SHAPE.get(curveShape):
			if name != "":
				curveName = mel.eval(config.SHAPE.get(curveShape))
				cmds.rename(curveName,newname)
				if newname == countName:
					num += 1
				else :
					num = 1
					countName = newname
				cmds.select(newname)
				cmds.setAttr("{}.tx".format(newname),(res[0]))
				cmds.setAttr("{}.ty".format(newname),(res[1]))
				cmds.setAttr("{}.tz".format(newname),(res[2]))
			else :
				curveName = mel.eval(config.SHAPE.get(curveShape))
				newCurveName = f"{curveShape}{num:02d}_{suffix}"
				cmds.rename(curveName,newCurveName)
				if newCurveName == countName:
					num += 1
				else :
					num = 1
					countName = newCurveName
				cmds.select(newCurveName)
				cmds.setAttr("{}.tx".format(newCurveName),(res[0]))
				cmds.setAttr("{}.ty".format(newCurveName),(res[1]))
				cmds.setAttr("{}.tz".format(newCurveName),(res[2]))
		sels = cmds.ls(sl=True)

		if not sels:
			return
		cmds.setAttr(f"{sels[0]}.overrideEnabled",1)
		cmds.setAttr(f"{sels[0]}.overrideRGBColors",1)
		cmds.setAttr(f"{sels[0]}.overrideColorR",r)
		cmds.setAttr(f"{sels[0]}.overrideColorG",g)
		cmds.setAttr(f"{sels[0]}.overrideColorB",b)
		cmds.select(cl=True)
#finish
def addAttributes(name,type,maxValue,minValue):
	sel = cmds.ls(selection=True)
	ctrl = sel[0]

	value = name

	if not cmds.attributeQuery(value, node=ctrl, exists=True):
		cmds.addAttr(ctrl, longName=value, attributeType="double", defaultValue=1, maxValue = float(maxValue) , minValue = float(minValue))

	if type == "Keyable":
		cmds.setAttr(ctrl + ".{}".format(value), keyable=True, edit=True)

	if type == "Displayable":
		cmds.setAttr(ctrl + ".{}".format(value), channelBox=True, edit=True)
	if type == "Hidden":
		cmds.setAttr(ctrl + ".{}".format(value), channelBox=False, edit=False)
#finish
def connectionEditor(output,outputAttr,input,inputTransform,inputAxis):
	outputName = f"{output}.{outputAttr}"
	inputName = f"{input}.{inputTransform}{inputAxis}"

	if not cmds.isConnected(outputName, inputName):
		cmds.connectAttr(outputName, inputName, force=True)