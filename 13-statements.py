import maya.cmds as cmds
import maya.OpenMaya as om
# IMPORTANT: >>you MUST run all code to get result<<
# cmds.SelectAll()
selection = cmds.ls(sl=True)
selection_length = len(selection)
# cmds.select(cl=True)
cmds.select(cl=False)
if selection_length < 1:
    om.MGlobal.displayError(">_<, Pick at least one object!")
elif 1 <= selection_length < 2:
    om.MGlobal.displayWarning('Ok!, Pick another Two!')
elif 2 <= selection_length < 3:
    om.MGlobal.displayWarning('Good!, Pick another one!')
else:
    om.MGlobal.displayInfo('selected items are: {}'.format(selection))


