import os
import numpy as np
from scipy.stats import pearsonr
from django import forms
import cv2 as cv
import numpy as np
import sys

class PrnuVid(forms.Form):
    #print("in class Prnu")
    #path=os.getcwd()
    #path2=path+"\\videos\\"+vidName+".mp4"
    #path4=path+"\\videos\\"+vidName+".mov"

    namey=forms.CharField(max_length=100)

    def __init__(self, video_path, *args, **kwargs):
        super(PrnuVid, self).__init__(*args, **kwargs)
        self.video_path = video_path
        self.path = os.getcwd()

    def save(self):
        print('in save')
        path = os.getcwd()
        video_path = self.video_path
        vidcap=cv.VideoCapture(video_path)
        #print(vidcap)
        print('before namey')
        namey=self.cleaned_data.get('namey')
        print('after namey')
        self.namey=self.path+"\\video\\"+namey
        path1 = self.namey
        print(path1)
        # namey=input('enter name of camera model:') #brand name
        # namey=forms.CharField(max_length=100)
        # path1=path+"\\model\\"+namey
        # print(path1)
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
        k=self.findprnu(path1)
        path3=path1+"\\"+namey+".npy"
        np.save(path3,k)
        s = self.findCorrelation(path3,path)
        return s
        # return True
    def findprnu(self,folder):
        print('in prnu')
        images= []
        for filename in os.listdir(folder):
            img=cv.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(img)
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
    def findCorrelation(self,filepath,ospath):
        ls=[]
        k = []
        for a,b,c in os.walk(os.getcwd()+'\\model'):
            print(a)
            print(b)
            if b:
                for i in b:
                    k.append(i)
            for i in c:
                if i.endswith(".npy"):
                    ls.append(a+"\\"+i)
        arr=np.load(filepath)
        cov_list=[]
        flag=0
        for i in range(len(ls)):
            arr2=np.load(ls[i])
            if(len(arr.flatten())==len(arr2.flatten())):
                flag=1
                #scipy.misc.imsave('outfile.jpg',arr2)
                #scipy.misc.imsave('outfile1.jpg', arr)
                cov, _=pearsonr(arr.flatten(),arr2.flatten())
                cov_list.append([cov,k[i]])
        if(flag==1):
            for i in range(len(cov_list)):
                print(cov_list[i])
        else:
            print("No Matching Model in DB")
        return cov_list
