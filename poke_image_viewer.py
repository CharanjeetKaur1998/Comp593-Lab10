"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import ctypes
import poke_api
from PIL import ImageTk
import image_lib
# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
    os.mkdir(images_dir)
else:
    pass
# Create the main window
root = Tk()
root.title("Pokemon Viewer")

# TODO: Set the icon
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
pokemon_ball_file_path = os.path.join(script_dir,'poke_ball.ico')
root.iconbitmap(pokemon_ball_file_path )
a=0

#Function for getting combobox value
def handle_pokemon_sel(event):
    sel_pokemon_index = cbox.current()
    pokemon_nm = L[sel_pokemon_index]
    image_file_path = poke_api.pokemon_artwork_download_and_save(pokemon_nm,images_dir)
    img_logo['file'] = image_file_path
    selected_pokemon = cbox.get()
    if selected_pokemon != "":
      Button1.config(state="normal")
      
    return 



#Function for Button click
def button_click():
    selected_pokemon = cbox.get()
    pokemon_image_filepath = os.path.join(images_dir,f"{selected_pokemon}.png")
    image_lib.set_desktop_background_image(pokemon_image_filepath)
  
    
    

# TODO: Create frames
frame1 = ttk.Frame(root)
frame1.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
frame1.rowconfigure(0,weight=1)
frame1.columnconfigure(0,weight=1)

frame2 = ttk.Frame(root)
frame2.grid(row=1,column=0,padx=10,pady=10)

frame3 = ttk.Frame(root)
frame3.grid(row=2,column=0,padx=5,pady=5)

# TODO: Populate frames with widgets and define event handler functions
# Inserting poke_ball image in frame1
file_path = os.path.join(script_dir,'poke_ball.png')
img_logo = PhotoImage(file = file_path)
lbl_logo = ttk.Label(frame1, image=img_logo)
lbl_logo.grid(padx=10, pady=10)

#Inserting the Combobox in frame2
L=poke_api.pokemon_list(1000)
cbox = ttk.Combobox(frame2,values=L,state='readonly')
cbox.set("Select a Pokemon")
cbox.grid(row=1,column=2,padx=5,pady=5)

#Displaying image after user selection from Combobox
cbox.bind('<<ComboboxSelected>>', handle_pokemon_sel)

#Inserting button in frame3
Button1 = Button(frame3,text="Set as Desktop image",command=button_click,state="disabled")
Button1.grid(row=2,column=2,padx=5,pady=5)



root.mainloop()