import os 
i = 1
path = input('Enter Path: ')
setName = input('Enter new name: ')
path = path + '/'
for filename in os.listdir(path):
    file_extension = filename.split('.')
    file = setName + str(i) + '.' + file_extension[1]
    Sourcefile = path + filename
    file = path + file
    os.rename(Sourcefile + file)
    i += 1
print('All file was rename !')    
    
