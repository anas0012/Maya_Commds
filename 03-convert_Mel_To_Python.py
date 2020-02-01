# E:\Courses\Projects_Folder\Python Projects\Maya
import maya.cmds as cmds

cmds.file(f=True, new=True)

# Creation in python >> Maya Commands <<
cmds.polyCube(w=2, d=2, h=2, name='my_cube_01', sw=1, sd=1, sh=1, ax=(0,1,0))
cmds.polyCube(w=2, d=2, h=2, name='my_cube_02', sw=2, sd=2, sh=2, ax=(0,1,0))
cmds.polyCube(w=2, d=2, h=2, name='my_cube_03', sw=3, sd=3, sh=3, ax=(0,1,0))
cmds.polyCube(w=2, d=2, h=2, name='my_cube_04', sx=4, sy=4, sz=4, ax=(0,1,0))

# Selection in python >> Maya Commands <<
cmds.select(clear=True)
cmds.select("my_cube_03", replace=True)
cmds.select("my_cube_03", toggle=True)
cmds.select("my_cube_04", replace=True)
cmds.select("my_cube_04", toggle=True)
cmds.select("pCylinder1", replace=True)
cmds.select("my_cube_03", "my_cube_04",replace=True)

