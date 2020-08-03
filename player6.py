import os
from tkinter.filedialog import askdirectory
 
import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from tkinter import *
import tkinter.messagebox 
from tkinter import ttk
from ttkthemes import themed_tk as tk 


root = tk.ThemedTk()
root.get_themes()
root.set_theme("scidgrey")
#root.set_theme("clam")
#root.set_theme("scidpurple")
root.configure(bg="#cecac8")
root.geometry("650x600+300+50")
root.title('music player') 
root.iconbitmap(r'D:\ostl\headphone.ico')

 
listofsongs = []
listofsongs1 = []
realnames = []
realnames1 = []
 
v = StringVar()
songlabel = ttk.Label(root,textvariable=v,width=42,relief=GROOVE)
 
index = 0
index1= -1
playindex=0
noofsongs=-1

def indexresult():
	global playindex
	cr=cb.get()
	if cr==1:
		playindex=0
	



cb=IntVar()
checkbutton=Checkbutton(root,text="play from playlist",bg="#cecac8",variable=cb,command=indexresult)
cr=cb.get()
checkbutton.place(x=450,y=310)



listbox = Listbox(root,width=42,height=17,relief=SOLID)
listbox.place(x=70,y=32)


label = Label(root,text='Music Player',relief= GROOVE,font = "Verdana 12 bold",bg="#cecac8",fg="#2c0e3a")
label.pack(fill=X)


scroll=Scrollbar(command=listbox.yview)
listbox.configure(yscrollcommand=scroll.set)
scroll.place(x=326,y=32,height=275)


listbox1 = Listbox(root,width=32,height=17,relief=SOLID)
listbox1.place(x=418,y=32)


scroll1=Scrollbar(command=listbox1.yview)
listbox1.configure(yscrollcommand=scroll1.set)
scroll1.place(x=614,y=32,height=275)


lengthlabel=Label(root,text="Total Length:--:--",font= "Airel 12 bold",bg="#cecac8",fg="#2c0e3a")
lengthlabel.place(x=455,y=500)



voldownphoto=PhotoImage(file ='D:\ostl\pvoldown.png')
voldownlabel=Label(root,image=voldownphoto,fg="#2c0e3a",bg="#cecac8")
voldownlabel.place(x=415,y=430)


volupphoto=PhotoImage(file ='D:\ostl\pvolup.png')
voluplabel=Label(root,image=volupphoto,fg="#2c0e3a",bg="#cecac8")
voluplabel.place(x=605,y=430)


def about():
	tkinter.messagebox.showinfo('About Project','\t\t Title = Music player\n\nMade by Amit Rane Anmol Shah and Neeraj Pal.\n\nOur OSTL project uses tkinter, pygame, mutagen and OS module for creating a GUI based audio player.\n\nThis audio player can play, pause and unpause songs .\n\nIt also has options for playing next and previous songs. \n\nApart from these basic features the player can also create a playlist. ')
		
    

def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
    global noofsongs
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            
            listofsongs.append(files)
 
 
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()
    

    realnames.reverse()
    for items in realnames:
        listbox.insert(0,items)
        noofsongs += 1 
 
    realnames.reverse()


menubar=Menu(root)
root.config(menu=menubar)

subMenu=Menu(menubar, tearoff=0)
subMenu1=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Browse",command=directorychooser)
subMenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="About", menu=subMenu1)
subMenu1.add_command(label="About project",command=about)




pygame.mixer.init()





def updatelabel():
	cr=cb.get()
	if(cr==1):
		global playindex
		global songname
		v.set(realnames1[playindex])
		songlabel.place(x=70,y=315)
	else:
		global index
		global songname
		v.set(realnames[index])
		songlabel.place(x=70,y=315)
		
	
    


def playsong():
	cr=cb.get()
	if (cr==1):
		try:
			global playindex
			pygame.mixer.music.load(listofsongs1[playindex])
			pygame.mixer.music.play()
			lengthdetail()
			updatelabel()  
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
	else:
		try:
			global index 
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			lengthdetail()
			updatelabel()  
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
		




 
 
def nextsong():
	cr=cb.get()
	if (cr==1):
		try:
			global playindex
			playindex += 1
			if playindex>index1:
				playindex=0
			pygame.mixer.music.load(listofsongs1[playindex])
			pygame.mixer.music.play()
			lengthdetail()
			updatelabel()
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
	else:
		try:
			global index
			global noofsongs
			index += 1
			if index > noofsongs:
				index=0
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			lengthdetail()
			updatelabel()
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
    	
	
 
def prevsong():
	cr=cb.get()
	if(cr==1):
		try:
			global playindex
			playindex -= 1
			if playindex < 0:
				playindex=index1
			pygame.mixer.music.load(listofsongs1[playindex])
			pygame.mixer.music.play() 
			lengthdetail()
			updatelabel()  
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
	else:
		try:
			global index
			global noofsongs
			index -= 1
			if index < 0:
				index=noofsongs
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play() 
			lengthdetail()
			updatelabel()  
		except:
			tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
     



def pausesong():
	try:
		pygame.mixer.music.pause()
		global paused
		paused=1
		v.set("")   
	except:
		tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
    

def unpausesong():
	try:
		global index
		pygame.mixer.music.unpause()
		global paused
		paused=0
		updatelabel()
	except:
		tkinter.messagebox.showerror('File not selected','Open file and browse for song.')
    


def setvol(val):
	volume=float(val)/100
	pygame.mixer.music.set_volume(volume)
     

     
def lengthdetail():
	cr=cb.get()
	if(cr==1):
		audio=MP3(listofsongs1[playindex])
		total_length=audio.info.length
		min,sec=divmod(total_length,60)
		min=round(min)
		sec=round(sec)
		timeformat='{:02d}:{:02d}'.format(min,sec)
		lengthlabel['text'] = "Total Length:"+timeformat
	else:
		audio=MP3(listofsongs[index])
		total_length=audio.info.length
		min,sec=divmod(total_length,60)
		min=round(min)
		sec=round(sec)
		timeformat='{:02d}:{:02d}'.format(min,sec)
		lengthlabel['text'] = "Total Length:"+timeformat
		

	
	    
def addsong():
	global index1
	index1+=1
	listofsongs1.append(listofsongs[index])
	realnames1.append(realnames[index])
	listbox1.insert(index1,realnames1[index1])


	


		 
	
def removesong():
	global index1
	listbox1.delete(index1)
	del listofsongs1[index1]
	del realnames1[index1]
	
	index1-=1
	


			
 

 



playphoto=PhotoImage(file = 'D:\ostl\play.png') 
playbutton = ttk.Button(root,image=playphoto,command=playsong)
playbutton.place(x=45,y=345)



nextphoto=PhotoImage(file = 'D:\ostl\pnext1.png') 
nextbutton = ttk.Button(root, image = nextphoto,command=nextsong)
nextbutton.place(x=225,y=450)            



previousphoto=PhotoImage(file = 'D:\ostl\previous1.png')
previousbutton = ttk.Button(root,image=previousphoto,command=prevsong)
previousbutton.place(x=105,y=450)    

pausephoto=PhotoImage(file = 'D:\ostl\pause.png')
pausebutton = ttk.Button(root,image=pausephoto,command=pausesong)
pausebutton.place(x=165,y=345) 


unpausephoto=PhotoImage(file ='D:\ostl\punpause.png')
unpausebutton=ttk.Button(root,image=unpausephoto,command=unpausesong)
unpausebutton.place(x=285,y=345)



scale=ttk.Scale(root,from_=0,to=100,orient=HORIZONTAL,length=158,command=setvol)
scale.set(70)
pygame.mixer.music.set_volume(0.7)
scale.place(x=440,y=430)


addbutton=Button(root,text="ADD",width=8,font="Airel 14 bold",relief=SOLID,fg="#2c0e3a",command=addsong)
addbutton.place(x=415,y=360)

removebutton=Button(root,text="REMOVE",width=8,font="Airel 14 bold",relief=SOLID,fg="#2c0e3a",command=removesong)
removebutton.place(x=530,y=360)


def playonenter(event):
	global play_label
	play_label=Label(text="Play Button",font="Verdana 8")
	play_label.place(x=48,y=414)

def playonleave(event):
		play_label.destroy()
	
def nextonenter(event):
	global next_label
	next_label=Label(text="Next Button",font="Verdana 8")
	next_label.place(x=226,y=516)

def nextonleave(event):
		next_label.destroy()
		
def prevsonenter(event):
	global prev_label
	prev_label=Label(text="Previous Button",font="Verdana 8")
	prev_label.place(x=94,y=516)

def prevsonleave(event):
		prev_label.destroy()

def pauseonenter(event):
	global pause_label
	pause_label=Label(text="Pause Button",font="Verdana 8")
	pause_label.place(x=164,y=414)

def pauseonleave(event):
		pause_label.destroy()		
	
def unpauseonenter(event):
	global unpause_label
	unpause_label=Label(text="Unpause Button",font="Verdana 8")
	unpause_label.place(x=277,y=412)

def unpauseonleave(event):
		unpause_label.destroy()		
		
	




playbutton.bind("<Enter>",playonenter) 
playbutton.bind("<Leave>",playonleave) 
nextbutton.bind("<Enter>",nextonenter)
nextbutton.bind("<Leave>",nextonleave)
previousbutton.bind("<Enter>",prevsonenter)
previousbutton.bind("<Leave>",prevsonleave)
pausebutton.bind("<Enter>",pauseonenter)
pausebutton.bind("<Leave>",pauseonleave)
unpausebutton.bind("<Enter>",unpauseonenter)
unpausebutton.bind("<Leave>",unpauseonleave)


 
 
 
 
 
 
 
root.mainloop()