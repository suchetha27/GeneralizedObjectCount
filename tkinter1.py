import tkinter as tk
from tkinter import *
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
 
root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 800)
canvas1.pack()

label1 = tk.Label(root, text='Get Object count')#label for heading
label1.config(font=('Arial', 20))#font style and size
canvas1.create_window(400, 50, window=label1)

label2 = tk.Label(root, text='Enter file name')#label for file name
label2.config(font=('Arial', 14))
canvas1.create_window(400, 150, window=label2)  
entry1 = tk.Entry (root)
canvas1.create_window(400, 200, window=entry1) 

label2 = tk.Label(root, text='Enter number of features')#label to enter number no. of features
label2.config(font=('Arial', 14))
canvas1.create_window(400, 250, window=label2) 
entry2 = tk.Entry (root)
canvas1.create_window(400, 300, window=entry2) 
          
  

def getObjectCount ():  
    imageName = (entry1.get())#enter the image name where you want to search template
    noOfFeatures =int(entry2.get())#number of features

    img_rgb = cv2.imread('C:\\Users\\Suchetha Hegde\\photo for imagej\\'+imageName)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    count=0
    lspoint=[]
    lspoint2=[]
    n=noOfFeatures
    for i in range(1,n+1,1):
        strr='C:\\Users\\Suchetha Hegde\\photo for imagej\\crop'+str(i)+'.jpg'
        template = cv2.imread(strr,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)

    #searching for templates
        for pt in zip(*loc[::-1]):
            if pt[0] not in lspoint or pt[1] not in lspoint2:
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                for i in range(((pt[0])-9),((pt[0])+9),1):
                    lspoint.append(i)
                for k in range(((pt[1])-9),((pt[1])+9),1):
                    lspoint2.append(k)
                count+=1
            else:
                continue
    
    
    print(count)
    cv2.imwrite('C:\\res.png',img_rgb)
    c=str(count)
    label1 = tk.Label(root, text="Total number of selected objects are "+c)
    label2.config(font=('Arial', 12))
    canvas1.create_window(400,400, window=label1)

    
    
button1 = tk.Button(text='SUBMIT', command=getObjectCount)
canvas1.create_window(400,350, window=button1)
 
root.mainloop()