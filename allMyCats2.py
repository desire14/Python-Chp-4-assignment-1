#program name: allMyCats2.py
#program description: Chp 4 assignment 1 Working with Lists
#programmer's Name: Dasaray Fyall

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or press "Enter" to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] 
    catNames.sort()
print('The cat names are:')
for name in catNames:
    print('  ' + name)