import importlib
from . import config
import maya.cmds as cmds
import maya.mel as mel
importlib.reload(config)

def createCurve(name,side,suffix,selectShape,r,g,b):
	num = 1
	curveShape = selectShape
	print("curveShape")
	newname = f"{side}_{name}{(num+1):01d}_{suffix}"
	if config.SHAPE.get(curveShape):
		print("got")
		curveName = mel.eval(config.SHAPE.get(curveShape))
		cmds.rename(curveName,newname)
	cmds.select(newname)
	sels = cmds.ls(sl=True)
	if not sels:
		return
	# cmds.setAttr(f"{sels[0]}.overrideEnabled", r, g, b, type="double3")