import cv2 as cv
import numpy as np
import os
import sys
def prnu(video):
    path=os.getcwd()
    #path2=path+"\\videos\\"+vidName+".mp4"
    #path4=path+"\\videos\\"+vidName+".mov"
    vidcap=cv.VideoCapture(video)
    #print(vidcap)
    
    namey=input('enter name of camera model:') #brand name
    path1=path+"\\model\\"+namey
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
    return true






def findprnu(ls_frame):
    print('in prnu')
    images=ls_frame
    # for filename in os.listdir(folder):
    #     img=cv.imread(os.path.join(folder,filename))
    #     if img is not None:
    #         images.append(img)
    print('block 1')
    imagegray=[]
    for img in images:
        imagegray.append(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
    print('block 2')
    imagedenoise=[]
    for img in imagegray:
        dst=cv.fastNlMeansDenoising(img,None,9,13)
        imagedenoise.append(dst)
    print('block 3')
    # a=np.zeros([1024,1024])
    # b=np.zeros([1024,1024])
    for i in range(len(images)):
        temp1=(imagedenoise[i]*imagegray[i])
        temp2=(imagegray[i])^2
        #a+=temp1
        #b+=temp2
    k=temp1/temp2
    print(k)
    return k
