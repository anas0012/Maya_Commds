import maya.cmds as cmds

# display all commands as a list
ls = cmds.ls()
# deselect all
cmds.select(clear=True)
# display all cameras in the viewport as a list
cmds.ls(cameras=True)
# select all polys in the viewport as a list
allselect = cmds.SelectAll()
# dispaly selected items in viewport as a list
cmds.ls(sl=True)
# display transforme items as a list
cmds.ls(tr=True)
# To Hide selected
selection_list = cmds.ls(sl=True)
for selected in selection_list:
    cmds.setAttr('{}.v'.format(selected), False)
# To Show selected
for selected in selection_list:
    cmds.setAttr('{}.v'.format(selected), True)

# filter what to see in ls list
cmds.ls(type="transform") # filter by type
cmds.ls("p*", transforms=True)
cmds.ls("*Cube*", transforms=True) # cubes only
cmds.ls("*Plane*", transforms=True) # planes only


