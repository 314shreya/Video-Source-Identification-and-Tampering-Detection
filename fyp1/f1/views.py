from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from f1.calculateprnu import Prnu
from f1.tamper import tamper
from f1.queryprnu import PrnuVid

# Create your views here.
def home(request):
    return render(request, 'home.html');
def prnu_main(request):
    return render(request, 'prnu_main.html');
def prnu1(request):
    return render(request, 'prnu1.html');
def prnu2(request):
    return render(request, 'prnu2.html');
def tamp_main(request):
    return render(request, 'tamp_main.html');
def tamp1(request):
    if request.method == 'POST' and request.FILES['myfile']:
        #print("Hello World")
        myfile = request.FILES['myfile']
        print(type(myfile))
        print(myfile.name)
        print(myfile.size)
        print(os.getcwd())
        print("calling tamper function")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.getcwd()+"\\media\\"+myfile.name
        k = tamper(uploaded_file_url)
        print("tamper finish")
    return render(request, 'tamp1.html');
def prnu11(request):
    if request.method == 'POST' and request.FILES['myfile']:
    # if request.method == 'POST':
        #print("Hello World")
        myfile = request.FILES['myfile']
        print(type(myfile))
        print(myfile.name)
        print(myfile.size)
        print(os.getcwd())
        print("calling prnu function")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.getcwd()+"\\media\\"+myfile.name
        print(uploaded_file_url)
        # Mynamey = Prnu(uploaded_file_url=uploaded_file_url, =request.POST)
        Mynamey = Prnu(video_path=uploaded_file_url, data=request.POST)
        # Mynamey = Prnu(request.POST)
        if Mynamey.is_valid():
            namey = Mynamey.cleaned_data['namey']
            g=Mynamey.save()
            # k = prnu(uploaded_file_url)
            print("prnu finish")
            a=myfile.name
            b=myfile.size
            print('printing K')
            #print(k)
    return render(request, 'prnu11.html', {'namey':namey, 'name':a, 'size':b} );

def prnu22(request):
    if request.method == 'POST' and request.FILES['myfile']:
    # if request.method == 'POST':
        #print("Hello World")
        myfile = request.FILES['myfile']
        print(type(myfile))
        print(myfile.name)
        print(myfile.size)
        print(os.getcwd())
        print("calling prnu function")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.getcwd()+"\\media\\"+myfile.name
        print(uploaded_file_url)
        # Mynamey = Prnu(uploaded_file_url=uploaded_file_url, =request.POST)
        Mynamey = PrnuVid(video_path=uploaded_file_url, data=request.POST)
        # Mynamey = Prnu(request.POST)
        if Mynamey.is_valid():
            namey = Mynamey.cleaned_data['namey']
            g=Mynamey.save()
            # k = prnu(uploaded_file_url)
            if g :
                cov = round(abs(g[0][0]),4)
                model = g[0][1]
            else :
                cov = 0
                model = "No model found"
            print("prnu finish")
            a=myfile.name
            b=myfile.size
            print('printing K')
            #print(k)
    return render(request, 'prnu222.html',{'namey':namey, 'cov':cov, 'model':model});
def prnu222(request):
    return render(request, 'prnu222.html');
# def findprnu(request):
#     val1=request.POST["video"]
#     print("Hello World")
#     res = 23
#     return render(request,'prnu1.html',{'result':res})
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         print("Hello World")
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'prnu11.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'prnu11.html')
