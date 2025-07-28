# features/autoclose_feature.py
import tkinter as tk

def setup_autoclose_ui(root):
    autoclose_enabled = tk.BooleanVar(root, value=False)
    frame = tk.Frame(root)
    frame.pack(fill="x", pady=5)

    checkbox = tk.Checkbutton(frame, text="Auto-close after copy", variable=autoclose_enabled)
    checkbox.pack(side="left", padx=5)

    return autoclose_enabled

def should_autoclose(autoclose_var):
    return autoclose_var.get()
