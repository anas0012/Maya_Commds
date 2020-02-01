# E:\Courses\Projects_Folder\Python Projects\Maya

# >>creating new dictionary<<
d = {'red':150, 'blue':250, 'green':350}
# get value of a key
d['first']
# >>change value of key<<
# d['second'] = 450
# >>add new key with value<<
d['black'] = 0
'''
>>The benefit of using get function is that<<
>>it handles error and return None if there is no value  for the key<<
'''
#d.get('black')
#d.get('cyan')
# >>loop through dict elements<<
for item in d.items():
    print('{}: {}'.format(item[0], item[1]))
