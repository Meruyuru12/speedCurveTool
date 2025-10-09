import importlib
from . import config
import maya.cmds as cmds
import maya.mel as mel
importlib.reload(config)

def createCurve(name,side,suffix,selectShape,r,g,b,num):
	
	countName = ""
	curveShape = selectShape
	if side == "":
		newname = f"{name}{num:02d}_{suffix}"
	else :
		newname = f"{side}_{name}{num:02d}_{suffix}"
	if config.SHAPE.get(curveShape):
		curveName = mel.eval(config.SHAPE.get(curveShape))
		cmds.rename(curveName,newname)
		if newname == countName:
			num += 1
		else :
			num = 1
			countName = newname
		print(countName)
		countName = newname
	cmds.select(newname)
	sels = cmds.ls(sl=True)
	if not sels:
		return
	# cmds.setAttr(f"{sels[0]}.overrideEnabled", r, g, b, type="double3")