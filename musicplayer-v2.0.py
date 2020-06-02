
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## DevMp3 Player ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


import tkinter as tk
import os
import fnmatch
import random
import webbrowser
import urllib.request
import pytube
import pkg_resources.py2_warn

from tkinter import messagebox
from bs4 import BeautifulSoup
from pygame import mixer
from googlesearch import search



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def down():
	try:
		y2index=yysongs.curselection()
		link = videos[y2index[0]]
		#print(link)
		yt = pytube.YouTube(str(link))
		stream = yt.streams.first()
		locc=pope.get()
		#print(locc)
		stream.download(str(locc))

	except:	
		messagebox.showinfo("Select First!","Select The Link First!")


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def popup():
	pop=tk.Tk()
	pop.title("Location")
	pop.resizable(0,0)
	pop.geometry("300x100")
	popf=tk.Canvas(pop,width=300,height=100,bg="#000")
	popf.place(relx=0,rely=0)

	popl=tk.Label(pop,bg="#000",fg="#FF001B",text="Enter Location:")
	popl.place(relx=0.1,rely=0.02)

	global pope
	pope=tk.Entry(pop,width=39,bg="#fff",fg="#000")
	pope.place(relx=0.1,rely=0.25)

	popb=tk.Button(pop,width=9,bg="#FF001B",fg="#000",text="Download",command=down)
	popb.place(relx=0.655,rely=0.45)

	pop.mainloop()

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def playv(event2):
	yindex=yysongs.curselection()
	webbrowser.open_new_tab(videos[yindex[0]])

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def youtubew():
	try:
		textToSearch = uentry.get()
		query = urllib.parse.quote(textToSearch)
		url = "https://www.youtube.com/results?search_query=" + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		global yysongs
		yysongs = tk.Listbox(utube,width=68,height=20,bg="#fff")
		global videos
		videos=[]
		for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
			videos.append('https://www.youtube.com' + vid['href'])
		for vv in range(len(videos)):
			yysongs.insert(vv,str(videos[vv]))
		yysongs.place(relx=0.05,rely=0.15)
		yysongs.bind('<Double-1>',playv)
	except:
		messagebox.showinfo("Check InterNet","Check Your Internet Connection!")


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def googlesearch():
	query = gentry.get()  
	sqb=[]
	scount=0
	s2count=0
	try:
		for j in search(query, tld="co.in", num=11, stop=11, pause=2): 
			if (scount+1)%2!=0:
				sqb.append(tk.Button(googlee,width=10,bg="#00C944",text="Results",command=lambda:webbrowser.open_new_tab(j)))
			else:
				sqb.append(tk.Button(googlee,width=10,bg="#ffd11a",text="Results",command=lambda:webbrowser.open_new_tab(j)))
			if(scount<=5):
				sqb[scount].place(relx=0.035+(scount/5),rely=0.65)
			else:
				sqb[scount].place(relx=0.035+(s2count/5),rely=0.75)
				s2count+=1
			scount+=1
	except:
		messagebox.showinfo("Chech It","Check Your Internet Connection Or Retry")



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
		messagebox.showinfo("First Choose","Enter The Folder!")  


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Unpauses The Function
def unpause():
	

	# Trys To Play The Paused Songs
	

	try:
		mixer.music.unpause()



	# Shows Errror Message
	except:
		messagebox.showinfo("First Choose","Enter The Folder!")  

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Plays Random Songs
def randomsong():
	try:
		
		# Gets The Loaction 
		
		address2=locentry.get()

		
		# Finds The Mp3
		
		tempoo=find("*.mp3",address2)


		# Initialises The Mixer

		mixer.init() 
		
		
		# Loads Random Songs 

		mixer.music.load(tempoo[random.randint(0,len(tempoo))]) 
		


		#Sets The Volume
		mixer.music.set_volume(1) 
		

		# Plays The Songs
		mixer.music.play()

	except:
		messagebox.showinfo("First Choose","Enter The Folder!") 




# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Plays The Songs
def play(event):
	
	# Gets The Current Selection In The List


	index=songs.curselection()


	global ls
	ls=list(index)
	
	address=temp[int(ls[0])]
	
	#Initialises the Mixer 
	
	mixer.init() 

	#Initialises the Load From the Address
	
	mixer.music.load(address) 

	
	#Sets The Volume of The Songs 
	
	mixer.music.set_volume(1) 


	# Plays The Songs
	mixer.music.play() 



# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Adds Songs From The Location To the List
def addsongs():


	global temp
	
	#Gets The Address From the Entry
	
	addr=locentry.get()


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
	
	

	# Initialtes The Scroll Bar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  Needs To Be Fixed  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	scrollbar =tk.Scrollbar(root, orient="vertical",command=songs.yview)
	scrollbar.place(relx=0.662,rely=0.15)
	songs.config(yscrollcommand=scrollbar.set)
	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


	# Binds The Double Click To The Fuction
	songs.bind('<Double-1>', play)

	# Binds The Enter Key To The Function
	songs.bind('<Return>',play)


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# YouTube Function
def Youtube():
	global utube
	utube=tk.Tk()
	utube.resizable(0,0)
	utube.title("YouTube")
	
	# Youtube Window

	uwin=tk.Canvas(utube,bg="#FF001B",width=600,height=400)
	uwin.pack()

	
	# Label

	titlelabel=tk.Label(utube,font="fixedsys 32",text="YouTube",fg="#FF001B",bg="#000",height=4)
	titlelabel.place(relx=0.75,rely=0.4)


	# Youtube Search Entry

	global uentry 
	uentry=tk.Entry(utube,width=68,text="Search Here",bg="#000",fg="#fff")
	uentry.place(relx=0.05,rely=0.1)

	# Label

	ulabel=tk.Label(utube,text="Song:",bg="#FF001B",font="fixedsys")
	ulabel.place(relx=0.05,rely=0.04)
	

	# Search Button


	ubutton=tk.Button(utube,width=14,text="Search",bg="#000",fg="#FF001B",font="fixedsys 10",command=youtubew) 						# Calls youtubew function
	ubutton.place(relx=0.75,rely=0.09)


	# Download Button

	udbutton=tk.Button(utube,width=14,text="Download",bg="#000",fg="#FF001B",font="fixedsys 10",command=popup)						# Calls popup function
	udbutton.place(relx=0.75,rely=0.9)

	
	# Opens Youtube in Browser


	ucutton=tk.Button(utube,width=14,text="Go To Youtube",bg="#000",fg="#FF001B",font="fixedsys 10",command=lambda:webbrowser.open_new_tab("https://www.youtube.com/"))
	ucutton.place(relx=0.75,rely=0.19)


	# Youtube Listbox
	ysongs = tk.Listbox(utube,width=68,height=20,bg="#fff")
	ysongs.place(relx=0.05,rely=0.15)
	
	utube.mainloop()

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# Google Function
def googleit():

	global googlee
	googlee=tk.Tk()
	googlee.title("Google")
	googlee.resizable(0,0)
	

	#Google Window

	gwin=tk.Canvas(googlee,bg="#000000",width=600,height=400)
	gwin.pack()


	# Google Label
	gblabel=tk.Label(googlee,text="Google",font="fixedsys 72",bg="#000",fg="#33EC12")
	gblabel.place(relx=0.25,rely=0.1)

	global gentry 

	# Seacrh Entry
	gentry=tk.Entry(googlee,width=71,text="Search Here",bg="#8327D7")
	gentry.place(relx=0.15,rely=0.4)


	# Search Button
	sbutton=tk.Button(googlee,width=14,text="Search",bg="#ffd11a",command=googlesearch)						#Calls googlesearch function
	sbutton.place(relx=0.4,rely=0.55)

	googlee.mainloop()


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


# Main Funtion 
def main():
	global root
	

	root=tk.Tk()
	
	root.resizable(0,0)
	
	root.title("MDevPlayer")


	# PHOTOS
	logo=tk.PhotoImage(file="assets\\logo.png")
	pausepic=tk.PhotoImage(file="assets\\pause.png")
	playpic=tk.PhotoImage(file="assets\\play.png")
	shuffle=tk.PhotoImage(file="assets\\shuffle.png")
	google=tk.PhotoImage(file="assets\\google.png")
	helpp=tk.PhotoImage(file="assets\\help.png")
	uutube=tk.PhotoImage(file="assets\\youtube.png")


	#Window Size
	mp3win=tk.Canvas(root,bg="#000000",width=1200,height=600)
	mp3win.pack()


	# Location Entry Bar
	global locentry																							# GLobal Variable locentry		
	
	locentry=tk.Entry(root,width=105,bg='#8327D7')#"#33EC12")
	locentry.place(relx=0.15,rely=0.05)
	
	#Label 
	seacrhlabel=tk.Label(root,fg="#DF00FF",bg="#000",text="Folder Address:",font="verdana 10 ")
	seacrhlabel.place(relx=0.15,rely=0.013)


	#Enter Button
	seacrhbutton=tk.Button(root,width=12,bg="#00C944",text="ENTER",command=addsongs)
	seacrhbutton.place(relx=0.6,rely=0.1)

	
	#song Listing
	msongs = tk.Listbox(root,width=105,height=30,bg="#ffd11a")
	msongs.place(relx=0.15,rely=0.15)

	
	#Logo Label
	logol=tk.Label(root,height=300,width=335,image=logo)
	logol.place(relx=0.7,rely=0.05)

	
	

	# Play Button


	unpausebutton=tk.Button(root,width=64,height=64,bg="#000",command=unpause,image=playpic)  						#Calls unpause Function
	unpausebutton.place(relx=0.72,rely=0.6)

	

	# Pause Button


	pausebutton=tk.Button(root,width=64,height=64,bg="#000",command=pause,image=pausepic)							# Calls Pause Function
	pausebutton.place(relx=0.80,rely=0.6)
	
	

	#Shuffle Button


	shufflebutton=tk.Button(root,width=64,height=64,bg="#000",command=randomsong,image=shuffle) 					# Calls Shuffle Function
	shufflebutton.place(relx=0.88,rely=0.6)


	
	#Close Button
	

	closebutton=tk.Button(root,text="CLOSE",width=12,bg="#000",fg="#0096FF",command=lambda:close())					# Calls Close Function
	closebutton.place(relx=0.86,rely=0.9)
	
	
	# Help Button


	helppb=tk.Button(root,width=16,height=16,bg="#000",image=helpp)                                               
	helppb.place(relx=0.98,rely=0.003)
	
	
	# Google Buttton

	
	googleb=tk.Button(root,width=130,height=48,bg="#000",image=google,command=googleit)                             # Calls googleit Function
	googleb.place(relx=0.02,rely=0.15)


	
	#Youtube Button


	yutube=tk.Button(root,width=130,height=48,bg="#000",image=uutube,command=Youtube)                               # Calls Youtube Function
	yutube.place(relx=0.02,rely=0.25)

	
	root.mainloop()


# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ###








# Main Function
if __name__=="__main__":
	main() #Calling Main Function
