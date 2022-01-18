from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def select_point(event):
    global lasx_front, lasy_front, lasx_side, lasy_side
    if event.y > max(height1,height2):
        pass
    elif event.x < width1:
        lasx_front, lasy_front = event.x, event.y
        canvas.delete("las_front_circle")
        canvas.create_oval(lasx_front-5, lasy_front-5, lasx_front+5, lasy_front+5,fill="cyan", tags="las_front_circle")
    elif event.x < width1 + 10:
        pass
    else:
        lasx_side, lasy_side = event.x, event.y
        canvas.delete("las_side_circle")
        canvas.create_oval(lasx_side-5, lasy_side-5, lasx_side+5, lasy_side+5,fill="cyan", tags="las_side_circle")


def add_vertex():
    # global canvas, core_features
    # print(canvas.find_withtag("las_front_circle"))
    try:
        lasx_front
    except NameError:
        print('no points selected')
        return
    if len(canvas.find_withtag("las_front_circle")) < 1:
        print('no frontal point selected')
        return
    if len(canvas.find_withtag("las_side_circle")) < 1:
        print('no frontal point selected')
        return

    # print(canvas.find_withtag("las_front_circle"))

    canvas.delete("las_front_circle")
    canvas.delete("las_side_circle")
    r = 5
    canvas.create_oval(lasx_front-r, lasy_front-r, lasx_front+r, lasy_front+r,fill="green", tags="circle"+str(len(core_features)))
    canvas.create_text(lasx_front, lasy_front, text=str(len(core_features)), fill="white", font=('Helvetica 10'), tags="circle"+str(len(core_features)))

    canvas.create_oval(lasx_side-r, lasy_side-r, lasx_side+r, lasy_side+r,fill="green", tags="circle"+str(len(core_features)))
    canvas.create_text(lasx_side, lasy_side, text=str(len(core_features)), fill="white", font=('Helvetica 10'), tags="circle"+str(len(core_features)))
    
    front_point = ((lasx_front/width1)*front_width,(lasy_front/height1)*front_height)
    side_point = (((lasx_side-10-width2)/width2)*side_width,(lasy_front/height2)*side_height)
    
    core_features.append((front_point,side_point))
    
    # lasx_front, lasy_front, lasx_side, lasy_side = -1, -1, -1, -1
    # del lasx_front, lasy_front, lasx_side, lasy_side
    # core_features.append((lasx,lasy))

def save_vertecies():
    # global canvas
    file1 = open("save_verticies.txt","a")
    for i in core_features:
        file1.write(str(i[0])+" "+str(i[1])+"\n")
    file1.close()

def delete_last_vertex():
    if len(core_features) < 1:
        print("no points to remove")
        return
    canvas.delete("circle"+str(len(core_features)-1))
    core_features.pop()

def main():
    global root, canvas, core_features, front_width, front_height, \
        side_width, side_height, width1, height1, width2, height2
    core_features = []
    #read images
    frontal_image_path = "vertex_identification/images/vincent_front.jpg"
    frontal_img = Image.open(frontal_image_path)
    front_width, front_height = frontal_img.size
    width1 = 500
    height1 = int(width1 * (front_height/front_width))
    if height1 > 700:
        height1 = 700
        width1 = int(height1 * (front_width/front_height))
    frontal_img = frontal_img.resize((width1,height1))

    side_image_path = "vertex_identification/images/vincent_side.jpg"
    side_img = Image.open(side_image_path)
    side_width, side_height = side_img.size
    height2 = height1
    width2 = int(height1 * (side_width/side_height))
    side_img = side_img.resize((width2,height2))

    #create tkinter window
    root = Tk()
    root.title("frontal view")
    root.geometry(str(width1+width2+10) + "x" + str(max(height1,height2)+120))
    root.configure(background='grey')

    #create canvas
    canvas = Canvas(root,bg= 'white')
    canvas.pack(anchor = 'nw', fill = 'both', expand = 1)

    #add images to canvas
    tkimg_front = ImageTk.PhotoImage(frontal_img)
    canvas.create_image(0,0,image = tkimg_front, anchor = 'nw')

    tkimg_side = ImageTk.PhotoImage(side_img)
    canvas.create_image(width1+10,0,image = tkimg_side, anchor = 'nw')

    #add buttons to canvas
    add_button = Button(canvas, text = "add", command = add_vertex)
    add_button.place(relx = .025, y = height1+20, relwidth = 0.3, height = 80)

    delete_button = Button(canvas, text = "delete last", command = delete_last_vertex)
    
    delete_button.place(relx = .35, y = height1+20, relwidth = 0.3, height = 80)

    save_button = Button(canvas, text = "save verticies", command = save_vertecies)
    save_button.place(relx = .675, y = height1+20, relwidth = 0.3, height = 80)

    
    canvas.bind("<Button-1>", select_point)
    # canvas.bind("<B1-Motion>", draw_smth)

    

    # ttk.Label(root, image = tkimg).place(x=0,y=0)

    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    return

if __name__ == "__main__":
    main()