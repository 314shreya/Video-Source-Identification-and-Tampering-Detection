import matlab.engine
eng=matlab.engine.start_matlab()
name=input("Enter Filename:")
filename='dataset//'+name+'.mp4'
print(filename)
a=eng.filetemp(filename,nargout=2)
print("no of frames ",a[0])

print(a[1])
