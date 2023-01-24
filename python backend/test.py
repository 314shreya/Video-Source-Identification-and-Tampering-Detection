# import numpy as np
# from PIL import Image

# # Creates a random image 100*100 pixels
# mat = np.random.random((1024,1024))

# # Creates PIL image
# img = Image.fromarray(mat, 'L')
# img.show()
"""import os
name=input('enter name of folder:')
path=os.getcwd()
path+="\\frames\\"+name
path1=path+"\\"+name+".txt"
print(path)
print(path1)"""

import numpy as np
from scipy.stats import pearsonr
arr = np.random.rand(1024,1024)
arr2= np.random.rand(1024,1024)
k, _=pearsonr(arr.flatten(),arr2.flatten())
j, _=pearsonr(arr2.flatten(),arr.flatten())
print(k)
print(j)

