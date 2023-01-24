import os
import numpy as np
from scipy.stats import pearsonr
import scipy.misc
def findCorrelation(filepath,ospath):
    ls=[]
    for a,b,c in os.walk(os.getcwd()+'\\frames'):
        for i in c:
            if i.endswith(".npy"):
                ls.append(a+"\\"+i)
    arr=np.load(filepath)
    cov_list=[]
    flag=0
    for i in ls:
        arr2=np.load(i)
        if(len(arr.flatten())==len(arr2.flatten())):
            flag=1
            scipy.misc.imsave('outfile.jpg',arr2)
            scipy.misc.imsave('outfile1.jpg', arr)
            cov, _=pearsonr(arr.flatten(),arr2.flatten())
            cov_list.append([cov,i])
    if(flag==1):
        for i in range(len(cov_list)):
            print(cov_list[i])
    else:
        print("No Matching Model in DB")