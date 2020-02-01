# E:\Courses\Projects_Folder\Python Projects\Maya
import maya.cmds as cmds

# create PolySphere
cmds.polySphere(name="pSphere", radius=4)

# rename..
cmds.rename("pCylinder1", "Oil_Lamp_01")
cmds.rename("pSphere", "bomb")

# select..
cmds.select(clear=True)
cmds.select("Oil_Lamp_01",replace=True)
cmds.select("bomb",replace=True)


