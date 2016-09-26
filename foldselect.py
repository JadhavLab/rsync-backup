import Tkinter as tk
from Tkinter import StringVar
import ttk
import tkFileDialog


class RsyncImporter(ttk.Frame):
    def __init__(self,root):

        ttk.Frame.__init__(self,root)

        #root = tk.Tk()
        #root.title("Files to rsync")
        #mainframe = ttk.Frame(root,padding = '10 10 10 10')
        #mainframe.grid(column=0, row=0)
        #mainframe.columnconfigure(0, weight=1)
        #mainframe.rowconfigure(0, weight=1)

        dirbutton = ttk.Button(self, text="add file or folder to rsync",
                   command= self.askdirectory(dirstosync_list)).grid(column = 2, row = 1)
        self.diropt = options = {}
        dirstosync_list = ('rabbit', 'cat')
        dirnames = StringVar(value=dirstosync_list)
        dirstosync = tk.Listbox(self,listvariable=dirnames).grid(column = 1, row = 1)

    def askdirectory(self,dirstosync_list):
        dirstosync_list.append(tkFileDialog.askdirectory(**self.diropt))
        return #tkFileDialog.askdirectory(**self.diropt)

if __name__ == '__main__':
    root = tk.Tk()
    RsyncImporter(root).pack()
    root.mainloop()

#Rsync_Importer()
#file_path = tkFileDialog.askopenfilename()