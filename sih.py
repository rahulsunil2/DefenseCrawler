# Import tkinter as tk 
import tkinter as tk 
from os import system
# creating a new tkinter window 
master = tk.Tk()  
  
# assigning a title 
master.title("DATACRAWLER") 
  
# specifying geomtery for window size  
master.geometry("400x200")  
  
   
e1 = tk.Entry(master) 
e2 = tk.Entry(master)
e3 = tk.Entry(master)
def display():
	system("scrapy crawl flagger")

tk.Label(master, text="\t\t\t").grid(row=1, column=1) 
tk.Label(master, text="URL").grid(row=2, column=1) 
tk.Label(master, text="\t\t\t").grid(row=3, column=1) 
tk.Label(master, text="Keyword Dir").grid(row=4, column=1)  
tk.Label(master, text="\t\t\t").grid(row=5, column=1)
tk.Label(master, text="Csv Dir").grid(row=6, column=1)

e1=tk.Entry(master)   
e2=tk.Entry(master)
e3=tk.Entry(master) 
   
# organizing them in th e grid 
e1.grid(row=2, column=2) 
e2.grid(row=4, column=2) 
e3.grid(row=6, column=2)
tk.Label(master, text="\t\t\t").grid(row=7, column=1)    
button1=tk.Button(master, text="submit", bg="green", command=display) 
button1.grid(row=8, column=2) 

  
   
  
      
master.mainloop() 
   
 