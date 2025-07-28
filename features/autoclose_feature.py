# features/autoclose_feature.py

import tkinter as tk

# Auto-close setting status
autoclose_enabled = tk.BooleanVar(value=False)

def setup_autoclose_ui(root):
    checkbox = tk.Checkbutton(
        root,
        text="Close after copy",
        variable=autoclose_enabled
    )
    checkbox.pack(anchor="w", padx=10, pady=5)

def should_autoclose():
    return autoclose_enabled.get()
