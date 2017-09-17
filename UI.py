import Logic
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile as fo
d= 'Stock3.jpg'
leftvideolist= []
def leftvideoframe(event):
    global  leftvideolist
    loc = leftvideolist[lslaider.get()-1]
    loc = cvtotk(loc)
    leftwindow.create_image(0, 0, image=loc, anchor="nw")
    leftwindow.pack(side="left")
    print("there")
    print(lslaider.get())
    root.mainloop()
def rightvideoframe(event):
    global rightvideolist
    rightwindow.create_image(0, 0, image=rightvideolist[rslaider.get()], anchor="nw")
    root.mainloop()
def printer (event):
    print ("hello world")
def cvtotk(a):
    alo = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    alo = Image.fromarray(alo)
    alo = ImageTk.PhotoImage(alo)
    return alo
def selectimage(event):
    global d
    global acv
    z = fo()
    if z!=None:
        d = z.name
        print(d)
        acv = cv2.imread(d)
        a= cvtotk(cv2.resize(acv, (400, 400)))
        leftwindow.create_image(0, 0, image=a, anchor="nw")
        leftwindow.pack(side="left")
    root.mainloop()
def creategird(event):
    global leftvideolist
    Logic.createVideoWithNoise(acv, cv2.imread('out.png', cv2.IMREAD_UNCHANGED), 'myvideo1.avi')
    video = cv2.VideoCapture('myvideo1.avi')
    print ("done")
    i=0
    leftvideolist = []
    while i<99:
        rate, frame = video.read()
#        frame = cv2.imread('Stock2.jpg')
        leftvideolist.append(frame)
        i= i+1
    leftvideolist.append(cv2.imread('Stock2.jpg'))
    print (len(leftvideolist))
    global  rightvideolist
    rightvideolist = leftvideolist
#    global acv
#    acv = Logic.Logic.creategrid(cv2.imread(d), wid.get(), count.get()+1, color =(blue.get()
#                                                                                 ,green.get(),
#                                                                                 red.get()))
#    a = acv
#    a = cv2.resize(a, (400, 400))
#    a= cvtotk(a)
#    leftwindow.create_image(0, 0, image=a, anchor="nw")
#    leftwindow.pack(side="left")
#    root.mainloop()
#    print("Решетка")
def findgird(event):
#    cv2.imshow('234', acv)
#    cv2.waitKey(0)
    global acv
    res, frame =Logic.noiseDetection('myvideo1.avi')
    print(res)
    tgreen.create_text((14,15), text=res)
    tgreen.update()
    cv2.imshow('noise',frame)
    cv2.waitKey(0)
##    a = Logic.Logic.findgrid(cv2.resize(acv, (0,0), fx=1.7, fy=1.7))
#    a = Logic.Logic.findgrid(cv2.resize(acv, (400,400)))
#    a = cv2.resize(a, (400, 400))
#    a= cvtotk(a)
#    rightwindow.create_image(0, 0, image=a, anchor="nw")
#    rightwindow.pack(side="right")
#    root.mainloop()
#    print("Нашли решетку")


root = tk.Tk()
acv= cv2.imread(d)
acv = cv2.resize(acv, (400,400))
Logic.createVideo(acv, 'myvideo.avi')
video = cv2.VideoCapture('myvideo.avi')
i=0
poi = [0,1,2,3,4,5,6,7,8,9]
while i<99:
    ret, frame=video.read()
    leftvideolist.append(frame)
    i= i+1
#Настройка окон
#print(len(leftvideolist))
rightvideolist = leftvideolist
toptool = tk.Frame(root,width = 400, height = 50)
righttoll = tk.Frame(root,width = 400, height = 50)
toolbar = tk.Frame(root, width=800, height = 50)
leftimage = tk.Frame(root, width = 400, height = 500)
rightimage = tk.Frame(root, width = 400, height = 500)
leftwindow = tk.Canvas(leftimage, width=400, height = 400)
rightwindow = tk.Canvas(rightimage, width = 400, height= 400)
#Настройка кнопок
selectim = tk.Button(toolbar, text = "Выберете текстуру")
selectim.bind("<Button-1>", selectimage)
selectim.pack(side = "left")
crtgird = tk.Button(toolbar, text ="Создать помеху")
crtgird.bind("<Button-1>", creategird )
fndgird = tk.Button(toolbar, text = "Найти помеху")
fndgird.bind("<Button-1>",findgird)
fndgird.pack(side = "left")
crtgird.pack(side = "left")

#Текст
tred = tk.Canvas(toptool, width= 116, height =26)
tred.create_text((59,15), text="Помеха на кадре:")
tgreen = tk.Canvas(toptool, width= 20, height =26)
tgreen.create_text((4,15), text=" ")
tblue = tk.Canvas(righttoll, width= 70, height =26)
tblue.create_text((22,15), text="Синий:")
textforwidth = tk.Canvas(toolbar, width = 60, height = 40)
textforwidth.create_text((35,10), text= "Ширина:")
textcount = tk.Canvas(toolbar, width = 60, height = 40)
textcount.create_text((35,10), text ="Кол-во:")
#Настройка ползунков
rslaider = tk.Scale(rightimage, from_=0, to= 100, length = 400, orient = tk.HORIZONTAL)
rslaider.pack(side = "bottom")
rslaider.bind("<ButtonRelease-3>", leftvideoframe)
lslaider = tk.Scale(leftimage, from_=1, to= 100, length = 400, orient = tk.HORIZONTAL)
lslaider.pack(side = "bottom")
lslaider.bind("<ButtonRelease-3>", leftvideoframe)
red = tk.Scale(righttoll, from_=255, to=0)
tred.pack(side ="left")
red.pack(side ="top")
green = tk.Scale(righttoll, from_=255, to=0)
tgreen.pack(side ="left")
toptool.pack(side = "top")
green.pack(side ="top")
blue = tk.Scale(righttoll, from_=255, to=0)
tblue.pack(side ="top")
blue.pack(side ="top")
wid= tk.Scale(toolbar,from_=0, to=50, orient = tk.HORIZONTAL)
#textforwidth.pack(side="left")
#wid.pack(side = "left")
count = tk.Scale(toolbar, from_=0, to=20, orient = tk.HORIZONTAL)
#textcount.pack(side = "left")
#count.pack(side = "left")
#настройка содержимого окон
a = cvtotk(cv2.resize(acv, (400, 400) ))
rightwindow.create_image(0,0, image =a, anchor = "nw")
toolbar.pack(side = "bottom")
#righttoll.pack(side ="right")
rightwindow.pack(side = "bottom")
#rightimage.pack(side = "right")
leftwindow.create_image(0,0, image=a,anchor ="nw")
leftwindow.pack(side = "bottom")
leftimage.pack(side = "left")

#tk.Label(root, text = "/home/anton/Downloads/345.jpg").pack()
root.mainloop()

