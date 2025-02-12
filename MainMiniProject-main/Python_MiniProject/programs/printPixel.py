import tkinter as tk
import coordsData
import numpy as np

def draw_coordinates(canvas, coordinates,sx=1, sy=1, end=[0,0]):
    coordinate = coordinates*np.array([sx,sy])
    print(coordinates[1])
    for (x, y) in coordinate:
        canvas.create_line(x+end[0]+50,y+50, x+end[0]+50, y+50+1, fill='black')
    return coordinate[len(coordinate)-1]

def main(coordinates):

    root = tk.Tk()
    root.title("Black Pixel Coordinates")

    canvas = tk.Canvas(root, width=1300, height=1200, bg='white')
    canvas.pack()
    end=0
    end=np.add(end,draw_coordinates(canvas, coordinates[0],0.25,0.25))
    print("End Type:{}".format(end),type(end))
    root.mainloop()

image_path = "C:\\Users\\Piyush\\Desktop\Code\\Python_MiniProject\\database\\alphabets_config\\alphabets.jpg" 

coordinates = coordsData.getData(image_path)

main(coordinates)
