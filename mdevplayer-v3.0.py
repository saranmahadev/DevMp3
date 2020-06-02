
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## DevMp3 Player ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


import tkinter as tk
import os
import fnmatch
import random
import webbrowser
import urllib.request


from pytube import YouTube 
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer




# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##



def down(loc):
	#try:
	print(loc) # Location
	link = pope.get()
	print(link)	# Link
	yt = YouTube(str(link))
	stream = yt.streams.first()
	stream.download(str(loc))
	#except:
	#	messagebox.showinfo("Check It","Check Your Internet Connection!") 

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def Youtube():
	pop=tk.Tk()
	pop.title("Location")
	pop.resizable(0,0)
	pop.geometry("300x100")
	popf=tk.Canvas(pop,width=300,height=100,bg="#000")
	popf.place(relx=0,rely=0)

	popl=tk.Label(pop,bg="#000",fg="#FF001B",text="Enter YouTube Link:")
	popl.place(relx=0.1,rely=0.02)

	global pope
	pope=tk.Entry(pop,width=39,bg="#fff",fg="#000")
	pope.place(relx=0.1,rely=0.25)

	popb=tk.Button(pop,width=9,bg="#FF001B",fg="#000",text="Download",command=lambda:down(filedialog.askdirectory()))
	popb.place(relx=0.655,rely=0.45)

	popb=tk.Button(pop,width=12,bg="#FF001B",fg="#000",text="Go To YouTube",command=lambda:webbrowser.open("https://www.youtube.com"))
	popb.place(relx=0.1,rely=0.45)

	pop.mainloop()


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def find(pattern,path):
	result=[]
	for root,dirs,files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name,pattern):
				result.append(os.path.join(root,name))
	return result

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

def close():
	ans=messagebox.askokcancel("Title","The application will be closed")
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
		if vol<101:
			mixer.music.set_volume(vol/100)
		else:
			messagebox.showinfo("High Volume","Choose Volume Between 0 and 100") 
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

		if event==1:
			address=temp[random.randint(0,len(temp))]
		else:
			address=temp[int(ls[0])]
		
		#Initialises the Mixer 
		
		mixer.init() 

		#Initialises the Load From the Address
		
		mixer.music.load(address) 

		
		#Sets The Volume of The Songs 

		mixer.music.set_volume(scale.get()) 
		mixer.music.play() 


		# Plays The Songs
		



	except:
		pass


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Adds Songs From The Location To the List
def addsongs(addr):


		global temp

		# Finds The Entry in The Location

		temp=find("*.mp3",addr) 
		

		# Sorts The Songs
		temp.sort()		



		global songs
		
		#Creates the List Box
		
		songs = tk.Listbox(root,width=105,height=30,bg="#ffd11a")
		


		#Adds The Songs To The List 
		for add in range(len(temp)):
			songs.insert(add,str(temp[add]))
		

		songs.place(relx=0.15,rely=0.15)	

		#########################################################################################################
		scrollbar =tk.Scrollbar(root, orient="vertical",command=songs.yview)									#
		scrollbar.place(relx=0.662,rely=0.15)																	# Unable To Fix :(
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
	google=tk.PhotoImage(file="assets\\google.png")
	helpp=tk.PhotoImage(file="assets\\help.png")
	uutube=tk.PhotoImage(file="assets\\youtube.png")
	selectf=tk.PhotoImage(file="assets\\select.png")

	#Window Size
	mp3win=tk.Canvas(root,bg="#000000",width=1200,height=600)
	mp3win.pack()


	# Choose Folder 
	

	selectbutton=tk.Button(root,width=48,height=48,bg="#000",image=selectf,command=lambda:addsongs(filedialog.askdirectory()))
	selectbutton.place(relx=0.05,rely=0.1)
	

	# Google Buttton

	
	googleb=tk.Button(root,width=48,height=48,bg="#000",image=google,command=lambda:webbrowser.open("https://www.google.com"))                             # Calls googleit Function
	googleb.place(relx=0.05,rely=0.3)


	
	#Youtube Button2

	yutube=tk.Button(root,width=48,height=48,bg="#000",image=uutube,command=Youtube)                               # Calls Youtube Function
	yutube.place(relx=0.05,rely=0.5)

	

	# Songs Placin4 Frame
	global msongsf
	msongsf = tk.Frame(root,width=635,height=485,bg="#ffd11a")
	msongsf.place(relx=0.15,rely=0.15)


	
	#Logo Label
	logol=tk.Label(root,height=300,width=335,image=logo)
	logol.place(relx=0.71,rely=0.15)



	# Play Button
	playbutton=tk.Button(root,width=8,height=2,bg="#000",command=lambda:play(0),text="Play",fg="#1CE221",font="fixedsys 8")  						#Calls unpause Function
	playbutton.place(relx=0.18,rely=0.045)	
	

	# Unpause Button
	unpausebutton=tk.Button(root,width=8,height=2,bg="#000",command=pause,text="Pause",fg="#1CE221",font="fixedsys 8")  						#Calls unpause Function
	unpausebutton.place(relx=0.28,rely=0.045)

	

	# Pause Button
	pausebutton=tk.Button(root,width=8,height=2,bg="#000",command=unpause,text="Unpause",fg="#1CE221",font="fixedsys 8")							# Calls Pause Function
	pausebutton.place(relx=0.38,rely=0.045)
	
	

	#Shuffle Button


	shufflebutton=tk.Button(root,width=8,height=2,bg="#000",command=lambda:play(1),text="Shuffle",fg="#1CE221",font="fixedsys 8") 					# Calls Randomsong Function
	shufflebutton.place(relx=0.48,rely=0.045)

	# Volume Scale
	global scale
	scale = tk.Scale(root,length=470,from_=0,to=100,fg="#ffd11a",troughcolor="#ffd11a",highlightbackground="#000",bg="#000",command=highlight,label="Volume",font="fixedsys 8")
	scale.place(relx=0.69,rely=0.155)


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
