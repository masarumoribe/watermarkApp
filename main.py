from PIL import Image, ImageTk, ImageGrab
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Watermark your photos')
root.geometry('1000x800')

# Upload and display image to be wartermarked
def upload_file(self):
    global my_image
    filename = filedialog.askopenfilename()
    if filename != '':
        image = Image.open(filename)
        print(image.size)
        new_width = image.size[0]
        new_height = image.size[1]
        if image.size[0] > 800:
            new_width = 800
            new_height = 800 * image.size[1] / image.size[0]
            print(new_height)
        if new_height > 650:
            new_height = 650
            new_width = 650 * image.size[0] / image.size[1]
        # print(new_width)
        # print(new_height)
        image = image.resize((int(new_width), int(new_height)))
        my_image = ImageTk.PhotoImage(image)
        new_image = my_canvas.create_image(400, 325, anchor="center", image=my_image)
        self.destroy()
        create_logo_bttn()

# Upload and display logo
def upload_logo(self):
    global my_logo
    global logo_image
    filename = filedialog.askopenfilename()
    if filename != '':
        logo_image = Image.open(filename)
        # print(logo_image.size)
        new_width = logo_image.size[0]
        new_height = logo_image.size[1]
        if logo_image.size[0] > 400:
            new_width = 400
            new_height = 400 * logo_image.size[1] / logo_image.size[0]
        if new_height > 325:
            new_height = 325
            new_width = 325 * logo_image.size[0] / logo_image.size[1]
        logo_image = logo_image.resize((int(new_width / 2), int(new_height / 2)))
        my_logo = ImageTk.PhotoImage(logo_image)
        new_logo = my_canvas.create_image(400, 325, anchor="center", image=my_logo)
        self.destroy()
        display_save_bttn()
        
# Create button to upload logo
def create_logo_bttn():
    logo_bttn = tk.Button(left_frame, highlightcolor='#FFFBEB', font=('Helvetica', '20'), text="Upload a Logo", bd=3, highlightbackground="#251749", height=7, width=12, command= lambda: upload_logo(logo_bttn))
    logo_bttn.grid(column=0, row=1)

def display_save_bttn():
    save_bttn = tk.Button(left_frame, highlightcolor='#FFFBEB', font=('Helvetica', '20'), text="Save Image", bd=3, highlightbackground="#251749", height=7, width=12, command= save_img)
    save_bttn.grid(column=0, row=1)

def save_img():
    global my_canvas
    
    my_canvas.postscript(file='canvas.eps')
    img = Image.open('canvas.eps')
    print(img)
    file = filedialog.asksaveasfilename(defaultextension='.png')
    img.save(file, "png")


#Create editing menu for the logo
# def edit_menu():
#     resize_bttn = tk.Button(left_frame, highlightcolor='#FFFBEB', font=('Helvetica', '20'), text="Resize Logo", bd=3, highlightbackground="#251749", height=7, width=12, command= resize())
#     resize_bttn.grid(column=0, row=1)

#     move_bttn = tk.Button(left_frame, highlightcolor='#FFFBEB', font=('Helvetica', '20'), text="Move Logo", bd=3, highlightbackground="#251749", height=7, width=12, command= move_option())
#     move_bttn.grid(column=0, row=2)
    

#Move logo function
def move(e):
    global my_logo
    my_logo = ImageTk.PhotoImage(logo_image)
    new_logo = my_canvas.create_image(e.x, e.y, anchor="center", image=my_logo)
    
    
#Resize logo function
# def resize():
#     global logo_image
#     logo_image = logo_image.resize((50, 50))
#     my_logo = ImageTk.PhotoImage(logo_image)
#     resized_logo = my_canvas.create_image(200, 200, image=my_logo)

#Create top frame for the title
top_frame = tk.Frame(root, bg='#495579', width=1000, height=150).grid(column=0, row=0, columnspan=2, sticky="NESW")
title = tk.Label(top_frame, bg='#495579', font=('Helvetica', '30'), fg='black', text='Watermark your Photos').grid(column=0, row=0, columnspan=2)

#Create left frame for the menu
left_frame = tk.Frame(root, bg="#251749", width=200, height=650).grid(column=0, row=1, sticky="NESW", rowspan=4)

#Create canvas
my_canvas = tk.Canvas(root, bg='black', width=800, height=650)
my_canvas.grid(column=1, row=1, sticky="NESW", rowspan=4)

# Bind the move method when we move the logo
my_canvas.bind('<B1-Motion>', move)

#Create button for image uploading
upload_bttn = tk.Button(left_frame, highlightcolor='#FFFBEB', font=('Helvetica', '20'), text="Upload an image", bd=3, highlightbackground="#251749", height=7, width=12, command= lambda: upload_file(upload_bttn))
upload_bttn.grid(column=0,row=1)

root.update()

print(root.winfo_rootx())
print(root.winfo_rooty())
print(my_canvas.winfo_rootx())
print(my_canvas.winfo_rooty())

root.mainloop()