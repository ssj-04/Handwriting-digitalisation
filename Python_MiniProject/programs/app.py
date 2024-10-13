import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import main
import new

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    root.destroy()
    new.Main(file_path)

def draw_striped_pattern(canvas, width, height, stripe_width=20):
    colors = ["#ffcccb", "#ffb6c1"]  # Alternating colors
    for i in range(0, height, stripe_width):
        color = colors[(i // stripe_width) % 2]
        canvas.create_rectangle(0, i, width, i + stripe_width, fill=color, outline=color)

root = tk.Tk()
root.title("Image Uploader")
root.geometry("850x700")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

  
title_bar = tk.Frame(root, bg="blue", relief='raised', bd=2)
title_bar.pack(fill=tk.X)

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame, width=800, height=600)
canvas.pack(expand=True)

draw_striped_pattern(canvas, 800, 600)

upload_button = ttk.Button(frame, text="Upload Image", command=upload_image)
upload_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
