from Tkinter import *

import subprocess	
import config
import tempfile
import os

class App:
		
	def __init__(self,master):
		frame = Frame(master)
			
		master.geometry('600x400')
		master.title("Brew Module Manager")
	
		e = Entry(master)
	
		scrollbar = Scrollbar(master, orient="vertical")
		scrollbar2 = Scrollbar(master, orient="vertical")	
		
		self.listbox2 = Listbox(master,bg="grey",width=20,height=20,yscrollcommand=scrollbar2.set)

	
		self.listbox = Listbox(master,bg="grey",width=20,height=20,yscrollcommand=scrollbar.set)
		
		
		listM = os.popen('brew list').readlines()
		listP = os.popen('brew search').readlines()
		
		def update():
		
			for item in listM:
				self.listbox.insert(END, item)
		
			for item in listP:
				self.listbox2.insert(END, item)

		
		def add():
			bCom = "brew install " + self.listbox2.get(self.listbox2.curselection())
			process = subprocess.Popen(bCom.split(),stdout=subprocess.PIPE)
			output=process.communicate()[0]		
		
		def addCus():
			bCom2 = "brew install " + e.get();
			process2 = subprocess.Popen(bCom2.split(),stdout=subprocess.PIPE)
			output2 = process2.communicate()[0]
			
		def remove():
			bCom3 = "brew uninstall " + self.listbox.get(self.listbox.curselection())
			process3 = subprocess.Popen(bCom3.split(), stdout=subprocess.PIPE)
			output3=process3.communicate()[0]

		addM = Button(master, text="Add", command=add).grid(row=0,column=3)
		addCM = Button(master, text="Add Custom", command=addCus).grid(row=0,column=2)
		
		rm = Button(master, text="Remove", command=remove).grid(row=0,column=4)

		scrollbar.config(command=self.listbox.yview)
		
		scrollbar2.config(command=self.listbox2.yview)
		
		update()
		
		e.grid(row=0,column=0)
		self.listbox.grid(row=1,column=0)
		self.listbox2.grid(row=1,column=10)
		
		
		
		
mm = Tk()	

app = App(mm)

mm.mainloop()
