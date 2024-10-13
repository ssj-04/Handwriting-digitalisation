import flet as ft
import flet.canvas as cv
import numpy as np 
import coordsData
import getPixel
import RefAlpha
end=[0,0]
Y=0
pvKey=""
def Main(image_path):
    #image_path = r"C:\Users\Piyush\Desktop\Code\Python_MiniProject\database\alphabets_config\Piyush_5000[1].png" 
    coordinates = coordsData.getData(image_path)
    x=1
    #print(coordinates[0])
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
        'z': coordinates[25]
    }
    #print(ref)
    refmin,refmax =min(coord[1] for coord in pixels["a"]), max(coord[1] for coord in pixels["a"] )
    ref=(refmin,refmax)
    for key in pixels:
        pixels[key]=getPixel.align(pixels[key],ref,key)
        #print(pixels["a"])
    #RefCoordinates = RefAlpha.getData(r"C:\Users\Piyush\Desktop\Code\Python_MiniProject\database\alphabets_config\table.jpg")
    #pixels = getPixel.scaling(pixels,RefCoordinates)

    def main(page: ft.Page):
        def draw_lines(e:ft.KeyboardEvent):
            global end, Y, pvKey
            if e.key ==" ":
                end[0]=end[0]+10
                print(" ",end="")
            elif e.key =='Enter':
                Y=Y+50
                end[0]=0
                print("\n")
            elif e.key =='Backspace':
                print("coming soon")
            else:
                print(e.key,end="")
                coord =(pixels[e.key.lower()])
                coord=np.add(coord,(end[0],50+Y)).tolist()
                end=(coord[len(coord)-1])
                end[0]=abs(end[0])
                for x,y in coord:
                    canvas.shapes.append(
                    cv.Line(x-500,y-300,x+1-500,y-300))
                page.update()

        page.title = "Draw Lines on Canvas"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        canvas = cv.Canvas(width=-500,height=-500)
        page.on_keyboard_event = draw_lines

        page.add(canvas)
    ft.app(target=main)

