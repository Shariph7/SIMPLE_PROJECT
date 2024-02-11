# Project Prerequisites
# Tkinter is a standard GUI library and it is one of the easiest ways to build a GUI application.
# pytube used for downloading videos from youtube

# Importing Libraries
from tkinter import *
from pytube import YouTube

# Create Display Window
root = Tk() # Tk() used to initialize tkinter to create display window
root.geometry('500x300') # used to set the window’s width and height
root.resizable(0,0) # set the fix size of window
root.title("Python Youtube Vdo Downloader! ") # used to give the title of window

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
# Label() widget use to display text that users can’t able to modify.
# root is the name of the window
# text which we display the title of the label
# font in which our text is written
# pack organized widget in block

# Field to enter link.
link = StringVar() # link is a string type variable that stores the youtube video link that the user enters.
# Entry() widget is used when we want to create an input text field.
# width sets the width of entry widget
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
# place() use to place the widget at a specific position.

# Create Function to Start Downloading
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()