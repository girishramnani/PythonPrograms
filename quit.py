from tkinter import *
from tkinter import ttk

class Application(Tk):
    
    def column_c(self):
        self.count_cl+=1
        return self.count_cl
    def row_c(self):
        self.count_row+=1
        return self.count_row
    
    def __init__(self,title):
        self.count_cl=0
        self.count_row=0
        Tk.__init__(self)
        self.title(title)
        self.frame=ttk.Frame(self,padding="3 3 12 12" )
        self.frame.grid(column=5,row=5,sticky=(W,E,N,S))
    def create_widget(self,text="label1"):
        ttk.Label(self.frame,text=text).grid(column=self.column_c(),row=self.row_c())
        
        
        
        
    

##class Application(tk.Frame):             
##    def __init__(self, master=None):
##        tk.Frame.__init__(self, master)  
##        self.grid()                      
##        self.createWidgets()
##
##    def createWidgets(self):
##        top=self.winfo_toplevel()
##        self.rowconfigure
##        self.quitButton = tk.Button(self, text='Quit',
##            command=self.quit)           
##        self.quitButton.grid()           
##
##app = Application()                      
##app.master.title("sdfsdf")  
###app.mainloop()  
app=Application("girish")
app.create_widget("enter the port:")



