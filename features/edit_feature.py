# features/edit_feature.py
from db import update_text
from tkinter import simpledialog

def add_edit_buttons(parent, text_id, text, cursor, conn, refresh_callback, copy_callback):
    import tkinter as tk

    item_frame = tk.Frame(parent)
    item_frame.pack(fill="x", pady=2)

    btn_copy = tk.Button(item_frame, text=text, command=lambda t=text: copy_callback(t), width=25, anchor="w")
    btn_copy.pack(side="left", padx=5)

    btn_edit = tk.Button(item_frame, text="✏️", command=lambda: handle_edit(text_id, text, cursor, conn, refresh_callback), width=3)
    btn_edit.pack(side="right", padx=5)

def handle_edit(text_id, current_text, cursor, conn, refresh_callback):
    new_text = simpledialog.askstring("Edit Text", "Modify text:", initialvalue=current_text)
    if new_text and new_text != current_text:
        update_text(cursor, conn, text_id, new_text)
        refresh_callback()
