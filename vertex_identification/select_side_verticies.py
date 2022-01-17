from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# import cv2
# import numpy
# import math

# side_features = []
# def select_point(event, x, y, flags, param):
# 	# grab references to the global variables
# 	global side_features
# 	# if the left mouse button was clicked, record the starting
# 	# (x, y) coordinates and indicate that cropping is being
# 	# performed
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 	    side_features.append((x,y))

def get_x_and_y(event):
    global lasx, lasy, core_features
    update_type = input("add, update, or cancel? [a,u,c]")
    if update_type == 'a':
        pass
    elif update_type == 'u':
        to_update = input("which number do you want to update")
        pass
    elif update_type == 'c':
        pass
    else:
        print('error, wrong input')
        return
    lasx, lasy = event.x, event.y

    print("(" + str(lasx) + "," + str(lasy) + ")")

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), 
                      fill='red', 
                      width=2)
    lasx, lasy = event.x, event.y

def main():

    global root, canvas, core_features
    core_features = []
    path = "vertex_identification/Riely_front.png"
    img = Image.open(path)
    width,height = img.size
    root = Tk()
    root.title("frontal view")
    root.geometry(str(width) + "x" + str(height))
    root.configure(background='grey')

    canvas = Canvas(root,bg= 'grey')
    canvas.pack(anchor = 'nw', fill = 'both', expand = 1)

    
    canvas.bind("<Button-1>", get_x_and_y)
    canvas.bind("<B1-Motion>", draw_smth)

    tkimg = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image = tkimg, anchor = 'nw')

    # ttk.Label(root, image = tkimg).place(x=0,y=0)

    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    return

if __name__ == "__main__":
    main()