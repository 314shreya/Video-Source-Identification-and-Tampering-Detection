import matlab.engine
def tamper (file_path):
    eng=matlab.engine.start_matlab()
    # name=input("Enter Filename:")
    # filename='dataset//'+name+'.mp4'
    # print(filename)
    a=eng.filetemp(file_path,nargout=2)
    print("no of frames ",a[0])
    print(a[1])
    return True
# def tamper(file_path):
#     return True
