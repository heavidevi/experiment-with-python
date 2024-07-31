import os,shutil #TO READ A PATH
path=r"/workspaces/experiment-with-python/"  #write  raw (signifies "r")path of the file here
#os.listdir(path) #toccheck file existing here
#checking if path exist.
#os.path.exists(path+".csv") #    /checking if path already exist(a folder to store respective files)
file_name=os.listdir(path) #tells about path of directory
folder_names=['py files','ipynb files']
for loop in range(2):
    if not os.path.exists(folder_names[loop]) :#checking one by one if the folder for that file exist
        
        os.makedirs(path+folder_names[loop]) #if not exist , it will make a folder for that file.
for file in file_name: #checking if the above filename is present in folder or directory
    #if in directory add it to the folder with respective file name
    if ".py" in file and not os.path.exists(path+"py files/"+file):#checking if the path of the file is already present inside by comparing it :
        shutil.move(path+file,path+"py files/"+file) #moving the file from one apth to another
    elif ".ipynb" in file and not os.path.exists(path+".ipynb/"+file):#checking if the path of the file is already present inside by comparing it :
        shutil.move(path+file,path+"ipynb files/"+file)
    else:
        print("can move")