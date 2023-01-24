import cv2 as cv
from findprnu import findprnu
import numpy as np
import os
import sys
from correlation import findCorrelation
def prnu(vidName):
    path=os.getcwd()
    path2=path+"\\videos\\"+vidName+".mp4"
    #path4=path+"\\videos\\"+vidName+".mov"
    vidcap=cv.VideoCapture(path2)
    #print(vidcap)
    name=input('enter name of camera model:')
    path1=path+"\\model\\"+name
    print(path1)
    try:
        os.makedirs(path1)
    except OSError:
        print ("Creation of the directory %s failed" % path1)
        sys.exit()
    else:
        print ("Successfully created the directory %s " % path1)
    success,image = vidcap.read()
    count = 0

    while success:
        cv.imwrite(str(path1) +"\\frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1
        if(count==50):
            break
    print("Done")
    k=findprnu(path1)
    path3=path1+"\\"+name+".npy"
    np.save(path3,k)
def sfind(vidName):
    path=os.getcwd()
    path2=path+"\\videos\\"+vidName+".mp4"
    vidcap=cv.VideoCapture(path2)
    name=vidName
    path1=path+"\\result\\"+name
    print(path1)
    try:
        os.makedirs(path1)
    except OSError:
        print ("Creation of the directory %s failed" % path1)
        sys.exit()
    else:
        print ("Successfully created the directory %s " % path1)
    success,image = vidcap.read()
    count = 0
    while success:
        cv.imwrite(str(path1) +"\\frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1
        if(count==50):
            break
    print("Done")
    k=findprnu(path1)
    path3=path1+"\\"+name+".npy"
    np.save(path3,k)
    findCorrelation(path3,path)
if __name__  == '__main__':
    n=1
    while(n<3 and n>0):
        print("1 : estimate  PRNU fingerprint of Camera \n2 : Source Identification of Camera\n3 : exit")
        n=int(input("Enter your choice: "))
        if n==1 or n==2:
            name=input('enter name of video:')
            if(n == 1):
                prnu(name)
            if(n == 2):
                sfind(name)

