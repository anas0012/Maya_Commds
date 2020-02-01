# E:\Courses\Projects_Folder\Python Projects\Maya
import maya.cmds as cmds

cmds.polyCube(name="cube_02")
cmds.select('cube_02')
# edit is flag takes True or False
cmds.setAttr("cube_02.t", edit=True)

# modify translation, rotation and scale
cmds.setAttr("cube_02.t", 0, 0, 0, type='double3')
cmds.setAttr("cube_02.s", 5, 5, 5, type='double3')
cmds.setAttr("cube_02.r", 0, 45, 0, type='double3')

# modify attribute lock
# lock is flag takes True or False
cmds.setAttr("cube_02.t", lock=True)
cmds.setAttr("cube_02.r", lock=False)
cmds.setAttr("cube_02.s", lock=False)

# modify attribute keyability tx, ty, tz
# modify attribute keyability sx, sy, sz
# modify attribute keyability rx, ry, rz
cmds.setAttr('cube_02.tx', keyable=True)
cmds.setAttr("cube_02.subdivisionsWidth")
