import tkinter as tk
import os
import fnmatch
from pygame import mixer
import win32api

def close():
	root.destroy()
def pause():
	mixer.music.pause()
def unpause():
	mixer.music.unpause() 
def stop():
	mixer.music.stop()
def play(event):
	index=songs.curselection()
	address=temp[index[0]]
	playingl=tk.Label(root,text="Currently Playing:\n"+address,bg="#0FC2EF")
	playingl.place(relx=0.715,rely=0.25)
	mixer.init() 
	mixer.music.load(address) 
	mixer.music.set_volume(1) 
	mixer.music.play() 
def find(pattern,path):
	result=[]
	for root,dirs,files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name,pattern):
				result.append(os.path.join(root,name))
	return result
def addsongs():
	global temp
	addr=locentry.get()
	temp=find("*.mp3",addr) 		
	global songs
	songs = tk.Listbox(root,width=105,height=30,bg="#ffd11a")
	for add in range(len(temp)):
		songs.insert(add,str(temp[add]))
	songs.place(relx=0.15,rely=0.15)	
	
	scrollbar =tk.Scrollbar(root, orient="vertical")
	scrollbar.config(command=songs.yview)
	scrollbar.place(relx=0.662,rely=0.15)
	songs.config(yscrollcommand=scrollbar.set)
	songs.bind('<Double-1>', play)
	songs.bind('<Return>',play)
def main():
	global root
	root=tk.Tk()
	root.resizable(0,0)
	root.title("DevMp3")

	mp3win=tk.Canvas(root,bg="#000000",width=1200,height=600)
	mp3win.pack()
	global locentry
	locentry=tk.Entry(root,width=105,bg="#33EC12")
	locentry.place(relx=0.15,rely=0.05)

	seacrhlabel=tk.Label(root,bg="#33EC12",fg="#000",text="Enter Your Music Location Folder")
	seacrhlabel.place(relx=0.15,rely=0.02)
	
	seacrhbutton=tk.Button(root,width=12,bg="#33EC12",text="SEARCH",command=addsongs)
	seacrhbutton.place(relx=0.6,rely=0.1)

	#song Listing
	msongs = tk.Listbox(root,width=105,height=30,bg="#ffd11a")
	msongs.place(relx=0.15,rely=0.15)

	player=tk.Frame(root,height=300,width=335,bg="#FF2500")
	player.place(relx=0.7,rely=0.05)

	unpausebutton=tk.Button(root,width=6,height=2,bg="#FF2500",command=unpause,text="PLAY")
	unpausebutton.place(relx=0.832,rely=0.6)

	pausebutton=tk.Button(root,width=6,height=2,bg="#33EC12",command=pause,text="PAUSE")
	pausebutton.place(relx=0.882,rely=0.6)

	stopbutton=tk.Button(root,width=6,height=2,bg="#ffd11a",command=stop,text="STOP")
	stopbutton.place(relx=0.932,rely=0.6)

	closebutton=tk.Button(root,text="CLOSE",width=12,bg="#33EC12",command=lambda:close())
	closebutton.place(relx=0.7,rely=0.8)
	root.mainloop()

if __name__=="__main__":
	main() #Calling Main Function
