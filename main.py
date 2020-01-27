# Import tkinter as tk 
import tkinter as tk 
from os import system
#https://mbcet.ac.in/
#https://mbcet.ac.in
class gui:
	def __init__(self):
		pass
	def display(self):
		system("scrapy crawl flagger")
	def interface(self):
		# creating a new tkinter window 
		master = tk.Tk()  
		  
		# assigning a title 
		master.title("DATACRAWLER") 
		  
		# specifying geomtery for window size  
		master.geometry("350x250")  
		  
		   
		self.e1 = tk.Entry(master)
		self.e4 = tk.Entry(master) 
		self.e2 = tk.Entry(master)
		self.e3 = tk.Entry(master)


		tk.Label(master, text="\t\t\t").grid(row=1, column=1) 
		tk.Label(master, text="URL").grid(row=2, column=1) 
		tk.Label(master, text="\t\t\t").grid(row=3, column=1) 
		tk.Label(master, text="Domain").grid(row=4, column=1) 
		tk.Label(master, text="\t\t\t").grid(row=5, column=1) 
		tk.Label(master, text="Keyword Dir").grid(row=6, column=1)  
		tk.Label(master, text="\t\t\t").grid(row=7, column=1)
		tk.Label(master, text="Csv Dir").grid(row=8, column=1)

		self.e1=tk.Entry(master)   
		self.e4=tk.Entry(master)
		self.e2=tk.Entry(master) 
		self.e3=tk.Entry(master)

		# organizing them in th e grid 
		self.e1.grid(row=2, column=2) 
		self.e4.grid(row=4, column=2) 
		self.e2.grid(row=6, column=2)
		self.e3.grid(row=8, column=2)
		tk.Label(master, text="\t\t\t").grid(row=9, column=1)    
		button1=tk.Button(master, text="submit", bg="green", command=self.display) 
		button1.grid(row=10, column=2)
		master.mainloop() 
	def keywords(self):
		f= open("key.txt","w+")
		f.write(self.e2.get())
		f.close()
	def url(self):
		f= open("url.txt","w+")
		f.write(self.e1.get())
		f.write(self.e4.get())
		f.close()

	def csv(self):
		f= open("csv.txt","w+")
		f.write(self.e3.get())
		f.close()
g=gui()
if __name__ == '__main__': 
	g.interface()