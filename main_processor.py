from tkinter import *
from app import App
    
root = Tk()
root.title("Image Cropper")

# # set icon
# photo = PhotoImage(file = "icon.png")
# root.iconphoto(False, photo)

# Adjust size
root.geometry("800x800")
 
# set minimum window size value
# root.minsize(800, 800)
 
# set maximum window size value
# root.maxsize(800, 800)

App(root, 800, 800)

root.mainloop()