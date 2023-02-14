from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox as mb # importing the messagebox module from tkinter
import os # importing the os module
import shutil # importing the shutli module

# generating the window
root = Tk()
root.title("AI Image Enhancer")
root.iconbitmap("photo-icon-image.ico")

# pre-determining the size of the window
root.geometry("450x350")
# placing the window in the center of the screen
root.eval("tk::PlaceWindow . center")

# Resizing the logo image
photo = Image.open("logoipsum-223.png") # Open image
resized = photo.resize((110, 100), Image.ANTIALIAS) # Resize image
logo = ImageTk.PhotoImage(resized) # reset image
# Placing the logo image
label1 = Label(root, image=logo).pack()

# Introductory message
label2 = Label(root, text="\nThis is an AI Image Enhancer.\nIt will improve the quality of your photos.\n\nTry now!\n\n").pack()

# Function for opening the File Explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Choose a File", filetypes=(("JPG files", "*.jpg*"),("PNG files", "*.png*") , ("JPEG files", "*.jpeg*"), ("all files", "*.*")))  # choose a file from your computer
    reqd_filename = str(filename.split("/")[len(filename.split("/"))-1])  # modifying the variable such that it will show only the file name, not the whole path to it
    label_file_explorer.configure(text="File Selected: "+reqd_filename, fg="#3B3486")  # change label contents to display the file selected

    # select directory to paste
    # using the filedialog's askdirectory() method to select the directory
    directoryToPaste = filedialog.askdirectory(title = "Select the folder to paste the file")

    # Function to copy the file to required directory
    try:
      # using the copy() method of the shutil module to paste the selected file to the desired directory
      shutil.copy(filename, directoryToPaste)
      # showing success message using the messagebox's showinfo() method
      mb.showinfo(
         title = "File copied!",
         message = "The selected file has been copied to the selected location.")
    except:
      # using the showerror() method to display error
      mb.showerror(
         title = "Error!",  
         message = "Selected file is unable to copy to the selected location. Please try again!")

# file explorer label
label_file_explorer = Label(root, text="Choose a low-quality picture: ", width=100, height=3)
label_file_explorer.pack()

# ṣome other button
button_explore = Button(root, text="Browse Files", command=browseFiles, cursor="hand2", fg="#FF8FB1", bg="#3B3486", activebackground="#8D72E1", activeforeground="#FCE2DB")
button_explore.pack()


root.mainloop()
