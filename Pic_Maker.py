from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy
def create_img(img_dest,w):
    print(img_dest)
    print(w)
    # try:
    img=Image.open(img_dest)
    thresh = w
    x,y = img.size[0],img.size[1]
    img = img.resize((round((50*x)/y*2.5), 50), Image.ANTIALIAS)
    fn = lambda x : 255 if x > thresh else 0
    final_img = img.convert('L').point(fn, mode='1')
    final_img = numpy.array(final_img)
    txt = open('new.txt','w')
    for i in range(img.size[1] - 1):
        for j in range(img.size[0] - 1):
            txt.writelines(' ' if final_img[i][j] == True else '*')
        txt.writelines('\n')
    txt.close()
    os.popen('start new.txt')

    # except:
    #     messagebox.showwarning("Warning", "Invalid file type")
    # quit()

def fileDialog(w):
    filename = filedialog.askopenfilename(initialdir="Pictures", title="Select A File", filetype=(("png files", "*.png"),("jpg files", "*.jpg"),("jpeg files", "*.jpeg"),("All Types", "*.*")))
    create_img(filename,w)


root = Tk()
root.title('Image Generator')
root.geometry('300x300')
root.resizable(False, False)
a = Label(root)
a.place(y=10,x=95)
a.config(text = 'Select the Threshold')
w = 0
s = Scale(root, from_=0, to=255,length=275,showvalue=1, orient=HORIZONTAL)
s.set(128)
s.place(y=30,x=10)
print(s.get())
btn1 = Button(root,text='Create Image',command= lambda:os.popen('start C:\WINDOWS\system32\mspaint.exe'))
btn2 = Button(root,text='Open Image',command=lambda:fileDialog(s.get()))
btn1.place(height=50,width=120, x=90, y=100)
btn2.place(height=50,width=120, x=90, y=180)
root.mainloop()