# features/delete_feature.py
import tkinter as tk
from db import delete_text

def add_delete_buttons(parent, text_id, text, cursor, conn, refresh_callback, copy_callback):
    item_frame = tk.Frame(parent)
    item_frame.pack(fill="x", pady=2)

    btn_copy = tk.Button(item_frame, text=text, command=lambda t=text: copy_callback(t), width=30, anchor="w")
    btn_copy.pack(side="left", padx=5)

    btn_delete = tk.Button(item_frame, text="🗑", command=lambda i=text_id: handle_delete(i, cursor, conn, refresh_callback), width=3)
    btn_delete.pack(side="right", padx=5)

def handle_delete(text_id, cursor, conn, refresh_callback):
    delete_text(cursor, conn, text_id)
    refresh_callback()
