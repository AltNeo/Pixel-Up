from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox as mb # importing the messagebox module from tkinter
import os # importing the os module
import shutil # importing the shutli module
import subprocess

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
    # Use askopenfilename() to select the input file
    input_file = filedialog.askopenfilename(title = "Select the low-quality image")
    
    # Move the input file to the 'media' folder in the root directory
    try:
        shutil.copy(input_file, "media")
        # Show success message
        mb.showinfo(
            title="File moved!",
            message="The selected file has been moved to the 'media' folder.")
        
        # Run the Conda command in the "gfpgan-image" environment
        cmd = "conda activate gfpgan-image && conda run -n gfpgan-image python inference_gfpgan.py --upscale 2 -i media -o results"
        subprocess.run(cmd, shell=True, check=True)

        
        # Show success message
        mb.showinfo(
            title="Process completed!",
            message="The process has completed successfully.")
        
        # Open the 'results' folder
        os.startfile("results\restored_imgs")
    except:
        # Show error message
        mb.showerror(
           title = "Error!",  
           message = "Unable to move the file or run the Conda command. Please try again!")

# file explorer label
label_file_explorer = Label(root, text="Choose a low-quality picture: ", width=100, height=3)
label_file_explorer.pack()

# ṣome other button
button_explore = Button(root, text="Browse Files", command=browseFiles, cursor="hand2", fg="#FF8FB1", bg="#3B3486", activebackground="#8D72E1", activeforeground="#FCE2DB")
button_explore.pack()

root.mainloop()
