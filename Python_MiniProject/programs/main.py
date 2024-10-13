import tkinter as tk
from tkinter import filedialog
import numpy as np
import coordsData
import getPixel
#import RefAlpha


end,pv=[0,0],[0,0]
Y=15
pvKey=""

def Main(image_path):
    x=1
    root = tk.Tk()
    root.title("Mini Project")
    root.geometry("850x700")
    #image_path = "C:\\Users\\Piyush\\Desktop\\Code\\Python_MiniProject\\database\\alphabets_config\\alpbhabets2.png"
    coordinates = coordsData.getData(image_path)
    
    #RefCoordinates = RefAlpha.getData(r"C:\Users\Piyush\Desktop\Code\Python_MiniProject\database\alphabets_config\table.jpg")
    pixels = {
        'a': coordinates[0],
        'b': coordinates[1],
        'c': coordinates[2],
        'd': coordinates[3],
        'e': coordinates[4],
        'f': np.subtract(coordinates[5],[5,0])*np.array([x,x]),
        'g':coordinates[6],
        'h':coordinates[7],
        'i': coordinates[8],
        'j': coordinates[9],
        'k': coordinates[10],
        'l':coordinates[11],
        'm': coordinates[12]*np.array([x,x]),
        'n':coordinates[13]*np.array([x,x]),
        'o':coordinates[14],
        'p': coordinates[15]*np.array([x,x]),
        'q': coordinates[16]*np.array([x,x]),
        'r': coordinates[17],
        's': coordinates[18],
        't': coordinates[19],
        'u': coordinates[20],
        'v': coordinates[21],
        'w': coordinates[22],
        'x': coordinates[23],
        'y': coordinates[24],
        'z': coordinates[25],
    }
    #print(pixels['t'])
    refmin,refmax =min(coord[1] for coord in pixels["a"]), max(coord[1] for coord in pixels["a"] )
    ref=(refmin,refmax)
    #print(ref)
    #print(ref)
    for key in pixels:
        pixels[key]=getPixel.align(pixels[key],ref,key)
    #print(pixels["a"])
    #pixels = getPixel.scaling(pixels,RefCoordinates)
    def draw_coordinates(canvas, coordinates,sx=1, sy=1, end=[0,0],col='#000000'):
        global Y
        coordinate = coordinates*np.array([sx,sy])
        coordinate = coordinates.tolist()
        #print(coordinates[1])
        for (x, y) in coordinate:
            canvas.create_line(x+end[0]+20,y+40+Y, x+end[0]+21.5, y+41+Y, fill=col,width=0.1,splinesteps=100)
        return coordinate[len(coordinate)-1]

    def draw_ruled_page(canvas):
        for i in range(0,20):
            canvas.create_line(50, 60 * i, 1550, 60 * i, fill='black')
    def new_page(canvas):
        canvas.delete("all")

    def save_page(canvas):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = canvas.itemcget('all', 'text')
                file.write(content)
    def on_key_press(event):
        global end,pvKey,Y,pv
        #print(end[1])
        if(end[1]<-1000):
            #print('greater')
            Y=Y+60
            end=[0,0]
        key = event.char
        if key==" ":
            end=[end[0]+20,end[1]]
        elif key == "\r":
            Y=Y+45 
            end=[0,0]
        elif key =='\x08':
            end=pv
            pv=draw_coordinates(canvas, pixels[pvKey],0.1,0.1,end,col="White")
        elif key:
            pv=draw_coordinates(canvas, pixels[key],0.1,0.1,end)
            pvKey=key
            end=np.add(pv,end)
            pv=np.subtract(end,pv)
        

    root.title("Notebook")
    # Create canvas
    canvas = tk.Canvas(root, bg='white', width=1100, height=830)
    canvas.pack()

    #draw_ruled_page(canvas)

    # Create file menu
    menu = tk.Menu(root)
    root.config(menu=menu)
    canvas.pack()
    root.bind('<KeyPress>', on_key_press)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=lambda: new_page(canvas))
    file_menu.add_command(label="Save", command=lambda: save_page(canvas))

    root.mainloop()