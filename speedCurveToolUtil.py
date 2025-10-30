import importlib
from . import config
import maya.cmds as cmds
import maya.mel as mel
importlib.reload(config)

curve_counters = {} #{left_test_circle_ctrl : 1}
#finish
def createCurve(name, side, suffix, selectShape, r, g, b, size, axis, check,constrain):
	global curve_counters
	curveShape = selectShape
	list = []
	LOCSELS = cmds.ls(sl=True)
	list.append(LOCSELS)
	key = f"{side}_{name}_{curveShape}_{suffix}"
	num = curve_counters.get(key, 1)

	if side == "":
		if name !="":
			newname = f"{name}{num:02d}_{suffix}"
		else:
			newname = f"{curveShape}{num:02d}_{suffix}"
	else:
		if name !="":
			newname = f"{side}_{name}{num:02d}_{suffix}"
		else:
			newname = f"{side}_{curveShape}{num:02d}_{suffix}"

	if config.SHAPE.get(curveShape):
		curveName = mel.eval(config.SHAPE.get(curveShape))
		cmds.rename(curveName, newname)
		list.append(newname)
		ro = cmds.xform(LOCSELS,q=True, ws= True , ro = True)
		if len(LOCSELS) == 0:
			pass
		else:
			res = cmds.xform(LOCSELS, q=True,ws=True, t=True)
			cmds.setAttr(f"{newname}.tx", res[0])
			cmds.setAttr(f"{newname}.ty", res[1])
			cmds.setAttr(f"{newname}.tz", res[2])
		cmds.setAttr(f"{newname}.sx", size)
		cmds.setAttr(f"{newname}.sy", size)
		cmds.setAttr(f"{newname}.sz", size)
		if axis == "X":
			cmds.setAttr(f"{newname}.rz",90)
		if axis == "Z":
			cmds.setAttr(f"{newname}.rx",90)
		cmds.setAttr(f"{newname}.overrideEnabled", 1)
		cmds.setAttr(f"{newname}.overrideRGBColors", 1)
		cmds.setAttr(f"{newname}.overrideColorR", r)
		cmds.setAttr(f"{newname}.overrideColorG", g)
		cmds.setAttr(f"{newname}.overrideColorB", b)
		cmds.makeIdentity( f'{newname}', apply=True, translate=True, rotate =True , scale = True)
		if check == True :
			grp01 = cmds.group(n = f"{newname}_grp")
		if constrain == True:
			try:
				cmds.setAttr(f"{grp01}.rx", ro[0])
				cmds.setAttr(f"{grp01}.ry", ro[1])
				cmds.setAttr(f"{grp01}.rz", ro[2])
			except:
				pass
			cmds.parentConstraint(list[1],list[0])
		curve_counters[key] = num + 1

	cmds.select(cl=True)
#finish
def addAttributes(name,type,maxValue,minValue):
	sel = cmds.ls(selection=True)
	ctrl = sel[0]

	value = name

	if not cmds.attributeQuery(value, node=ctrl, exists=True):
		if len(maxValue) == 0 and len(minValue) == 0:
			cmds.addAttr(ctrl, longName=value, attributeType="double")
		else :
			cmds.addAttr(ctrl, longName=value, attributeType="double", defaultValue=0, maxValue = float(maxValue) , minValue = float(minValue))

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