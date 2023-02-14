import os
import tkinter
dest="D:\Projects\EnhanceIt\GFPGAN\results\restored_imgs"
def openFolder():
    if os.path.exists(dest):
        os.startfile(dest)
    else:
        mb.showerror("Error", "The specified directory does not exist")
button_explore = Button(root, text="Get Result", command=openFolder, cursor="hand2", fg="#FF8FB1", bg="#3B3486", activebackground="#8D72E1", activeforeground="#FCE2DB")
button_explore.pack()

