# ui.py
import tkinter as tk

def create_main_window():
    root = tk.Tk()
    root.title("Clipboard Manager")
    root.geometry("400x500")
    return root

def create_frame(parent):
    frame = tk.Frame(parent)
    frame.pack(pady=10, fill="both", expand=True)
    return frame

def create_add_button(parent, command):
    btn = tk.Button(parent, text="Add New Text", command=command)
    btn.pack(pady=5)
