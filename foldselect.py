import Tkinter as tk
import ttk
import tkFileDialog

class Rsync_Importer():
    def __init__(self,root):

        ttk.Frame.__init__(self,root)

        root = tk.Tk()
        root.title("Files to rsync")
        mainframe = ttk.Frame(root,padding = '10 10 10 10')
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="add file or folder to rsync",
                   command= self.askdirectory ).grid(column = 2, row = 2)
    def askdirectory(self):
        return tkFileDialog.askdirectory(**self.fileopt)

if __name__ == '__main__':
    root = tk.Tk()
    Rsync_Importer(root).pack()
    root.mainloop()

Rsync_Importer()
#file_path = tkFileDialog.askopenfilename()