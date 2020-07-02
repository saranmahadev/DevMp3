
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## DevMp3 Player ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


import tkinter as tk
import os
import fnmatch
import random
import webbrowser
import urllib.request
import speedtest
 
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer

def createplayl():
	pass
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

def ops(dd):
	if dd==1:
		dlabel=tk.Label(netwin,text=str(int(st.download())/1000)+'  kb/s',bg="#000",fg="#6EFF00")
		dlabel.place(relx=0.05,rely=0.5)
	else:
		uplabel=tk.Label(netwin,text=str(int(st.upload())/1000)+'  kb/s',bg="#000",fg="#6EFF00")
		uplabel.place(relx=0.55,rely=0.5)



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
def netsd():
	global netwin

	netwin=tk.Tk()
	netwin.title("NetSpeed")
	
	netwinb=tk.Canvas(netwin,bg="#000",width=300,height=150)
	netwinb.pack()

	global st
	st=speedtest.Speedtest()
	connected=tk.Label(netwin,text="###Connected###",bg="#000",fg="#6EFF00")
	connected.place(relx=0.05,rely=0.05)
	
	downbutton=tk.Button(netwin,text="Download Speed",bg="#000",fg="#6EFF00",command=lambda:ops(1))
	downbutton.place(relx=0.05,rely=0.3)
	
	uploadbutton=tk.Button(netwin,text="Upload Speed",bg="#000",fg="#6EFF00",command=lambda:ops(2))
	uploadbutton.place(relx=0.55,rely=0.3)


	netwin.mainloop()
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def find(pattern,path):
	result=[]
	names=[]
	for root,dirs,files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name,pattern):
				result.append(os.path.join(root,name))
				names.append(os.path.join("",name))
	return result,names

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

def close():
	ans=messagebox.askokcancel("Exit","The application will be closed")
	if ans==True:
		root.destroy()



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def pause():
	try:
		mixer.music.pause()
	except:
		pass 

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Unpauses The Function
def unpause():
	

	# Trys To Play The Paused Songs
	

	try:
		mixer.music.unpause()



	# Shows Errror Message
	except:
		pass 

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

def highlight(event3):
	try:
		vol=scale.get()
		mixer.music.set_volume(vol/100) 
	except:
		pass



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Plays The Songs
def play(event):
	
	# Gets The Current Selection In The List
	try:

		index=songs.curselection()

		global ls
		ls=list(index)

		# Shuffle Option
		if event==1:
			address=temp[random.randint(0,len(temp))]
		# Normal
		else:
			address=temp[int(ls[0])]
		
		#Initialises the Mixer 
		
		mixer.init() 

		#Initialises the Load From the Address
		
		mixer.music.load(address) 

		
		#Sets The Volume of The Songs 

		mixer.music.set_volume(scale.get()) 
		
		mixer.music.play()


		



	except:
		addsongs(filedialog.askdirectory())


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Adds Songs From The Location To the List
def addsongs(addr):


		global temp,tempnames

		# Finds The Entry in The Location

		temp,tempnames=find("*.mp3",addr) 
		
		# Sorts The Songs
		#temp.sort()		
		#tempnames.sort()
		#print(tempnames)
		#print(temp)


		global songs
		
		#Creates the List Box
		
		songs = tk.Listbox(root,width=111,height=29,bg="#ffd11a")
		


		#Adds The Songs To The List 
		for add in range(len(temp)):
			songs.insert(add,str(tempnames[add]))
		

		songs.place(relx=0.08,rely=0.15)	

		#########################################################################################################
		scrollbar =tk.Scrollbar(root, orient="vertical",command=songs.yview)									#
		scrollbar.place(relx=0.623,rely=0.15)																	# Unable To Fix :(
		songs.config(yscrollcommand=scrollbar.set)																#
		#########################################################################################################

		# Binds The Double Click To The Fuction
		songs.bind('<Double-1>', play)

		# Binds The Enter Key To The Function
		songs.bind('<Return>',play)



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Main Funtion 
def main():
	global root
	

	root=tk.Tk()
	
	root.resizable(0,0)
	
	root.title("MDevPlayer")


	# PHOTOS
	logo=tk.PhotoImage(file="assets\\logo.png")
	helpp=tk.PhotoImage(file="assets\\help.png")
	selectf=tk.PhotoImage(file="assets\\select.png")
	download=tk.PhotoImage(file="assets\\download.png")
	net=tk.PhotoImage(file="assets\\net.png")
	netspeed=tk.PhotoImage(file="assets\\wifi.png")

	#Window Size
	mp3win=tk.Canvas(root,bg="#000000",width=1200,height=600)
	mp3win.pack()


	# Choose Folder 
	

	selectbutton=tk.Button(root,width=48,height=48,bg="#000",image=selectf,command=lambda:addsongs(filedialog.askdirectory(parent=root,title="Songs Folder",mustexist=True)))
	selectbutton.place(relx=0.02,rely=0.18)
	

	# Browser

	browser=tk.Button(root,image=net,width=16,height=16,bg="#000",command=lambda:webbrowser.open("https://www.google.com"))
	browser.place(relx=0.03,rely=0.95)

	#Net Speed
	nnet=tk.Button(root,image=netspeed,width=16,height=16,bg="#000",command=netsd)
	nnet.place(relx=0.01,rely=0.95)

	# Songs Placing Frame
	global msongsf
	msongsf = tk.Frame(root,width=670,height=470,bg="#ffd11a")
	msongsf.place(relx=0.08,rely=0.15)


	
	#Logo Label
	logol=tk.Label(root,bg="#000",activebackground="#000",activeforeground="#000",bd=1,height=300,width=250,image=logo)#,command=lambda:webbrowser.open("http://mdevplayer.eu5.org"))
	logol.place(relx=0.752,rely=0.25)



	# Play Button
	playbutton=tk.Button(root,width=8,height=2,bg="#000",command=lambda:play(0),text="Play",fg="#1CE221",font="fixedsys 8")  						#Calls unpause Function
	playbutton.place(relx=0.08,rely=0.045)	
	

	# Unpause Button
	unpausebutton=tk.Button(root,width=8,height=2,bg="#000",command=pause,text="Pause",fg="#1CE221",font="fixedsys 8")  						#Calls unpause Function
	unpausebutton.place(relx=0.18,rely=0.045)

	

	# Pause Button
	pausebutton=tk.Button(root,width=8,height=2,bg="#000",command=unpause,text="Unpause",fg="#1CE221",font="fixedsys 8")							# Calls Pause Function
	pausebutton.place(relx=0.28,rely=0.045)
	
	

	#Shuffle Button


	shufflebutton=tk.Button(root,width=8,height=2,bg="#000",command=lambda:play(1),text="Shuffle",fg="#1CE221",font="fixedsys 8") 					# Calls Randomsong Function
	shufflebutton.place(relx=0.38,rely=0.045)

	
	# Creates a Playlist
	createplay=tk.Button(root,width=16,height=2,bg="#000",command=createplayl,text="Create Playlist",fg="#9C11ED",font="fixedsys 6") 					# Calls Randomsong Function
	createplay.place(relx=0.5,rely=0.045)

	# Available Playlist
	avaiplay=tk.Menubutton(root,width=18,height=2,bg="#000",text="Play Playlist",fg="#9C11ED",font="fixedsys 6") 					# Calls Randomsong Function
	avaiplay.place(relx=0.63,rely=0.045)


	# Delete Playlist
	deleteplay=tk.Button(root,width=16,height=2,bg="#000",command=lambda:play(1),text="Delete Playlist",fg="#9C11ED",font="fixedsys 4") 					# Calls Randomsong Function
	deleteplay.place(relx=0.77,rely=0.045)





	# Volume Scale
	global scale
	scale = tk.Scale(root,length=460,from_=0,to=100,fg="#ffd11a",troughcolor="#ffd11a",highlightbackground="#000",bg="#000",command=highlight,label="Volume",font="fixedsys 8")
	scale.set(100)
	scale.place(relx=0.64,rely=0.155)


	#Close Button

	closebutton=tk.Button(root,text="CLOSE",width=12,bg="#000",fg="#0096FF",command=lambda:close())					# Calls Close Function
	closebutton.place(relx=0.86,rely=0.9)
	
	
	# Help Button


	helppb=tk.Button(root,width=16,height=16,bg="#000",image=helpp)                                               
	helppb.place(relx=0.98,rely=0.003)
	
	

	
	root.mainloop()


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ###



# Calling Main Function
if __name__=="__main__":
	main()
