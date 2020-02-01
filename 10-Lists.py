# E:\Courses\Projects_Folder\Python Projects\Maya
# ctrl + / for commenting
print("--------------------------------------------------")
double_list = [1,2,3,[1,2,3]]
print(double_list)
# To Access Multi Dimension List
print("The[2] Element in [3] Item_List is:", double_list[3][2])
print("--------------------------------------------------")
List_Items = []
steng = "we have offers"
# convert string into list through >> list[string_name] <<
# convert string into list through >> string_name.split <<
print(list(steng))
print(steng.split())
print("--------------------------------------------------")
steng_splitted = steng.split()
for item in steng_splitted:
    List_Items.append(item)
print(List_Items)
print("--------------------------------------------------")
# append, extend, remove, insert
x = ['c', 'a', 'v']
y = ['d', 'e', 'f']
z = ['g', 'h', 'i']
x.append('q') # append item
print("x.item_appended = ", x)
y.remove('e') # remove specified item
# del y[0] remove by index
print("y.item_removed = ", y)
y.insert(1, 'e') # insert specific item in specific index
print("y.item_inserted = ", y)
z.extend(['j', 'k', 'l']) # convert extended_list into items and append items into it
print("z.List_items_extended = ", z)
z.extend('python') # convert string into items and append items into it
print("z.string_items_extended = ", z)
print("--------------------------------------------------")
# sorting list
print("x not sorted is:", x)
x.sort()
print("x sorted is:", x)



