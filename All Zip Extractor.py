import os
from zipfile import ZipFile
path=raw_input('Enter path to the folder: ')    #Folder which contains the zip files
pathList=[]

for i in os.listdir(path):
    if i[len(i)-4:len(i)]=='.zip':              #If extension is .zip:
        if os.name=='posix':
            pathList.append(path+'/'+i)        #then add filename+path to a new list
        else:
           pathList.append(path+"\\"+i)

for j in pathList:
    with ZipFile(j, 'r') as zip:                #Open file
        zip.extractall(path)                    #Extract all contents to 'path'
        zip.close()                             #Close zip file

print 'Done!'

