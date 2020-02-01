# E:\Courses\Projects_Folder\Python Projects\Maya
import os

maya_script_paths_result = os.environ["MAYA_SCRIPT_PATH"]
paths = maya_script_paths_result.split(";")
for path in paths:
    print(path)



