# E:\Courses\Projects_Folder\Python Projects\Maya
# Channel Box Attributes
# Modifying poly
import maya.cmds as cmds

# create cube
cmds.polyCube(name="cube_01")

# select
cmds.select("cube")

# get attribute information using getAttr
cmds.getAttr("cube.translate")
cmds.getAttr("cube.tx", keyable=True)
cmds.getAttr("cube.tx", size=True)
cmds.getAttr("cube.tx", type=True)
















