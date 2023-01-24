import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
'''folder="C:/Users/vborh/Desktop/Final year papers/MS_Image_Dataset/Dataset_MSecurity/temporary"
images=[]
for filename in os.listdir(folder):
    img=cv.imread(os.path.join(folder,filename))
    if img is not None:
        images.append(img)
cv.imshow('fine',images[0])
cv.waitKey(0)
imagegray=[]
for img in images:
    imagegray.append(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
imagedenoise=[]
for img in imagegray:
    dst=cv.fastNlMeansDenoising(img,None,9,13)
    imagedenoise.append(dst)
a=np.zeros([1024,1024])
b=np.zeros([1024,1024])
for i in range(len(images)):
    temp1=(imagedenoise[i]*imagegray[i])
    temp2=(imagegray[i])^2
    a+=temp1
    b+=temp2
k=a/b
print(k)'''

def findprnu(folder):
    print('in prnu')
    images=[]
    for filename in os.listdir(folder):
        img=cv.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    print('1')
    imagegray=[]
    for img in images:
        imagegray.append(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
    print('2')
    imagedenoise=[]
    for img in imagegray:
        dst=cv.fastNlMeansDenoising(img,None,9,13)
        imagedenoise.append(dst)
    print('3')
    a=np.zeros([1024,1024])
    b=np.zeros([1024,1024])
    for i in range(len(images)):
        temp1=(imagedenoise[i]*imagegray[i])
        temp2=(imagegray[i])^2
        #a+=temp1
        #b+=temp2
    k=temp1/temp2
    print(k)
    return k

"""k=findprnu("C:/Users/vborh/Desktop/Final year papers/MS_Image_Dataset/Dataset_MSecurity/temporary")
img = Image.fromarray(k, 'L')
img.show()
"""


