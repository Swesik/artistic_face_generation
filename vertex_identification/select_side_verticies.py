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
    global canvas, core_features
    lasx, lasy = event.x, event.y
    update_type = input("add, update, or cancel [a,u,c]? -----")
    if update_type == 'a':
        core_features.append((lasx,lasy))
        canvas.create_oval(lasx-5, lasy-5, lasx+5, lasy+5,fill="green", tags="circle"+str(len(core_features)))
        canvas.create_text(lasx, lasy, text=str(len(core_features)), fill="black", font=('Helvetica 15 bold'), tags="circle"+str(len(core_features)))
    elif update_type == 'u':
        to_update = input("which number do you want to update? ----- ")
        core_features[int(to_update)] = core_features.append((lasx,lasy))
        canvas.delete("circle"+to_update)
        canvas.create_oval(lasx-6, lasy-6, lasx+6, lasy+6,fill="green", tags="circle"+to_update)
        canvas.create_text(lasx, lasy, text=to_update, fill="black", font=('Helvetica 13 bold'), tags="circle"+to_update)
    elif update_type == 'c':
        pass
    else:
        print('error, wrong input')
        return
    
    
    print("(" + str(lasx) + "," + str(lasy) + ")")

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

    update_panel = PanedWindow(orient ='horizontal')

    
    canvas.bind("<Button-1>", get_x_and_y)
    # canvas.bind("<B1-Motion>", draw_smth)

    tkimg = ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image = tkimg, anchor = 'nw')

    # ttk.Label(root, image = tkimg).place(x=0,y=0)

    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    return

if __name__ == "__main__":
    main()