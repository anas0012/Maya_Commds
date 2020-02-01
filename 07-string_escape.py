# E:\Courses\Projects_Folder\Python Projects\Maya
# searching string!
double = "double"
"do" in double
len(double)
print(double[::-1])
print(double[0:5:2])

name = "maya is good"
for char in name:
    print(char)

s = 'beginning python for maya'
num = '1'
path = 'devi3e'
s.upper()
num.lower()

s.isupper()
num.islower()

s.find('python')
s[10:16]

s.isdigit()
num.isdigit()
path.isdigit()
# add zeros befor the string >> useful for increasing file version number like scene_01, scene_02, ...<<
# zfill takes number above string length
num.zfill(3)
path.zfill(9)


