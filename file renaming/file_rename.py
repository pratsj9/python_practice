        #now this is a python program for renaming all files in a directory that have numbers in their names
        #This program is a part of the udacity python programming foundations course
        #it makes use of the os library in python
        #This program renames image files in the images folder that contain numbers in their names to simply names
        #use the old images folder to regain the numeric named files for practice

import os
import re   #Pyton 3 needs the re library to replace string characters unlike previous versions

def rename_files():
                file_list = os.listdir(r"C:\Users\Pratik Joshi\Desktop\Udacity Courses\Python foundations\file renaming\images")
                print (file_list)
                directory = os.getcwd()
                print ("Current Working Directory is "+directory)
                os.chdir(r"C:\Users\Pratik Joshi\Desktop\Udacity Courses\Python foundations\file renaming\images")
                print ("Changed Working Directory for adding images path"+os.getcwd())
                for file_name in file_list:
                        print("Old file name:"+file_name)
                        print("New File name:"+re.sub('[0-9]','',file_name))
                        os.rename(file_name,re.sub('[0-9]','',file_name))
                os.chdir(directory)
rename_files()
