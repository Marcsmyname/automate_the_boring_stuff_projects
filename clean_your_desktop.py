#! python3
#Clean Your Desktop
#Marc Leon
import, os, shutil

for folderName, subfolders, filenames in os.walk('C:\\Users\\Marc\\Desktop'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')


for file in filenames:
    if file endswith.('.txt'):
        shutil.move('C:\\Users\\Marc\\Desktop\\notes')
