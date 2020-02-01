# E:\Courses\Projects_Folder\Python Projects\Maya
import maya.cmds as cmds

# craeting polySphere with
cmds.polySphere()
# flags >> radius = 5
cmds.polySphere(radius=5)

# flags >> help
cmds.help('polySphere')

# Modes >> create, Query, Edit
# Query sphere radius
# prints radius value
cmds.polySphere('polySphere1', query=True, radius = True) # Must select or type name

# edit radius sphere
cmds.polySphere("polySphere1", edit=True, radius=3)

# ls, select
cmds.ls()
cmds.ls(selection=True)
cmds.select("pSphere1")
cmds.select("pSphere1", add=True)
cmds.select("pCube1", replace=True)

