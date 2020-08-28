#!/usr/bin/python
# Basic Image Viewer that will keep the window on top

import tkinter as tk
import tkinter.filedialog as filedialog
from PIL import ImageTk, Image, ImageOps
from os import path

DEFAULT_SIZE = 500
first_time = True
base_title = "Ref Viewer"

window = tk.Tk()

window.title(base_title)
window.configure(background='black')
window.attributes("-topmost", True)
window.geometry("200x200")

def delay_resize(event):
    newsize_w = event.width
    newsize_h = event.height
    window.after(16, resize_image, newsize_w, newsize_h)

def resize_image(newsize_w, newsize_h):
    if image_height > image_width:
        custom_width = newsize_w

        width_percentage = (custom_width/float(image_width))
        h_size = int(float(raw_ref_image.size[1]*float(width_percentage)))
        final_width = custom_width
        final_height = h_size

    elif image_width > image_height:
        custom_height = newsize_h

        height_percentage = (custom_height/float(image_height))
        w_size = int(float(raw_ref_image.size[0]*float(height_percentage)))
        final_width = w_size
        final_height = custom_height
    else:
        final_height = newsize_h
        final_width = newsize_w
    
    copy_image = raw_ref_image.copy()
    copy_image = ImageOps.fit(copy_image, (final_width, final_height), Image.ANTIALIAS)
    ref_image = ImageTk.PhotoImage(copy_image)
    panel.config(image = ref_image)
    panel.image = ref_image
    dynamic_size = '{}x{}'.format(final_width, final_height)
    window.geometry(dynamic_size)

def default_resize(copy_image):
    if image_height > image_width:
        custom_width = DEFAULT_SIZE

        width_percentage = (custom_width/float(image_width))
        h_size = int(float(copy_image.size[1]*float(width_percentage)))
        final_width = custom_width
        final_height = h_size

    elif image_width > image_height:
        custom_height = DEFAULT_SIZE

        height_percentage = (custom_height/float(image_height))
        w_size = int(float(copy_image.size[0]*float(height_percentage)))
        final_width = w_size
        final_height = custom_height
    else:
        final_height = DEFAULT_SIZE
        final_width = DEFAULT_SIZE

    copy_image = ImageOps.fit(copy_image, (final_width, final_height), Image.ANTIALIAS)
    ref_image = ImageTk.PhotoImage(copy_image)
    panel.config(image = ref_image)
    panel.image = ref_image
    dynamic_size = '{}x{}'.format(final_width, final_height)
    window.geometry(dynamic_size)

ref_image_path = filedialog.askopenfilename(
    initialdir="V:/anime_girls",
    title="Select a Ref",
    filetypes=[("Image","*.png"),("Image","*.jpg"),("Image","*.jfif")]
    )

raw_ref_image = Image.open(ref_image_path)
copy_image = raw_ref_image.copy()

image_width, image_height = raw_ref_image.size

ref_image = ImageTk.PhotoImage(copy_image)

panel = tk.Label(window, image = ref_image)
panel.bind('<Configure>', delay_resize)
if first_time is True:
    default_resize(copy_image)
    window.title("{} {}".format(base_title, path.basename(ref_image_path)))
    first_time = False
panel.pack(side = "bottom", fill = "both", expand = 1)

window.mainloop()
