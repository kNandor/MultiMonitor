import Tkinter as Tkinter
import ttk
import time
import threading

from Tkinter import *

class View(threading.Thread):
	def __init__(self,rootWindow):
		threading.Thread.__init__(self)
		self.root=rootWindow
	def run(self):
		time.sleep(1.0)
		master=ttk.Frame(self.root,name='master')
		master.pack(fill=Tkinter.BOTH)
		self.root.title('EZ')
		self.root.protocol("WM_DELETE_WINDOW", master.quit)
		

		nb=ttk.Notebook(master,name='nb')
		nb.pack(fill=Tkinter.BOTH, padx=2, pady=3)
		f1=ttk.Frame(nb)
		f2=ttk.Frame(nb)
		nb.add(f1,text='One')
		nb.add(f2,text='Two')

		t=Tkinter.Text(f1,height=2,width=30)
		t.pack()
		
		t.insert(Tkinter.END,"JJ 1\n")
		t.insert(Tkinter.END,"ssd 2\n")
		time.sleep(2.0)
		t.delete('1.0','end')
		t.insert(Tkinter.END,"JJ 3\n")
		t.insert(Tkinter.END,"ssd 4\n")


class Application(Tkinter.Frame):
	def say_hi(self):
		print("hi there, everyone!")
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		# self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit
		self.QUIT.pack({"side": "left"})
		self.notebook=ttk.Notebook(self,name='nb')
		self.notebook.pack(fill=Tkinter.BOTH,padx=2,pady=3)
	def addNew(self,name):
		l_frame1=ttk.Frame(self.notebook)
		self.notebook.add(l_frame1,text=name)
		l_text1=Tkinter.Text(l_frame1,height=10,width=100)
		l_text1.pack()
		return (l_frame1,l_text1)		
	def __init__(self,master=None):
		Tkinter.Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

class TextHandler:
	def __init__(self,(frame,text),nrLine=10):
		self.frame=frame
		self.text=text
		self.added=False
		self.nrLine=nrLine
	def addNewText(self,line):
		content=self.text.get('1.0',Tkinter.END).encode('ascii')[:-1]
		if self.added:
			try:
				content=self.text.get('1.0',Tkinter.END).encode('ascii')[:-1]
			 	index=content.index('\n')
			 	count=content.count('\n')
		 		newcontent=content[index+1:]
		 		if count>self.nrLine-1:
		 			self.text.delete('1.0',Tkinter.END)
		 			self.text.insert(Tkinter.END,newcontent)
		 	except:
		 		pass
		self.text.insert(Tkinter.END,line)
		self.added=True
		
def main():
	print('Main')
	root=Tkinter.Tk()
	root.title('Manager')
	app = Application(master=root)
	t1=TextHandler(app.addNew('Aoo'))
	t2=TextHandler(app.addNew('Boo'))
	t1.addNewText('Text11\n')
	t1.addNewText('Text12\n')
	for i in range(20):
		t2.addNewText('Text2'+str(i))
	for i in range(12):
		t2.addNewText('Text2'+str(i+20)+'\n')
	app.mainloop()
	# root.destroy()

	# master=ttk.Frame(root,name='master')
	# master.pack(fill=Tkinter.BOTH)
	# root.title('EZ')
	# root.protocol("WM_DELETE_WINDOW", master.quit)
	# v=View(root)
	# v.start()
	# root.mainloop()

	# nb=ttk.Notebook(master,name='nb')
	# nb.pack(fill=Tkinter.BOTH, padx=2, pady=3)
	# f1=ttk.Frame(nb)
	# f2=ttk.Frame(nb)
	# nb.add(f1,text='One')
	# nb.add(f2,text='Two')

	# t=Tkinter.Text(f1,height=2,width=30)
	# t.pack()
	
	# t.insert(Tkinter.END,"JJ 1\n")
	# t.insert(Tkinter.END,"ssd 2\n")
	# time.sleep(2.0)
	# t.delete('1.0','end')
	# t.insert(Tkinter.END,"JJ 3\n")
	# t.insert(Tkinter.END,"ssd 4\n")
	# 

if __name__=='__main__':
	main()