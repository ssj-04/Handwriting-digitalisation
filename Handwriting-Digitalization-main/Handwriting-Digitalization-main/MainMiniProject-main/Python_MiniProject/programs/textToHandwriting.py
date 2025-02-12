import tkinter as tk
from tkinter import messagebox,filedialog,ttk
from PIL import Image
import pytesseract 
import dup
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path


def extract_text_with_pytesseract(image_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image)
        
        return text.strip()
    except Exception as e:
        print(f"Error during text recognition: {e}")
        return None      

def display_text_editor(extracted_text,root):
    # Clear the window and display the text editor
    for widget in root.winfo_children():
        widget.destroy()
    
    # Textbox to display and edit extracted text
    text_box = tk.Text(root, wrap=tk.WORD, width=80, height=20)
    text_box.insert(tk.END, extracted_text)
    text_box.pack(padx=20, pady=20)

    # Button to convert the text to handwriting
    convert_button = tk.Button(root, text="Convert to Handwriting", command=lambda: convert_to_handwriting(text_box.get("1.0", tk.END).strip(),root))
    convert_button.pack(pady=10)
def upload_image(text,root):
    frame = ttk.Frame(root, padding=(20, 10, 20, 10), relief='flat')
    frame.pack(fill=tk.BOTH, expand=True)
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        progress = ttk.Progressbar(frame, orient="horizontal", mode="indeterminate")
        progress.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        progress.start()
        
        try:
            root.destroy()
            dup.Main(text,file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the image: {e}")

def convert_to_handwriting(text,root):
    try:
        # Clear all existing widgets in the window
        for widget in root.winfo_children():
            widget.destroy()
        frame = ttk.Frame(root, padding=(20, 10, 20, 10), relief='flat')
        frame.pack(fill=tk.BOTH, expand=True)
        upload_button = ttk.Button(frame, text="Upload Image", command=lambda: upload_image(text,root))
        upload_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error during handwriting conversion: {e}")


def Main(image_path,root):
    extracted_text = extract_text_with_pytesseract(image_path)
    if extracted_text:
        display_text_editor(extracted_text,root)
    else:
        messagebox.showerror("Error", "No text could be extracted from the image.")

    root.mainloop()