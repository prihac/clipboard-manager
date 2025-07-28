# main.py
import tkinter as tk
from tkinter import simpledialog
import pyperclip

from db import connect_db, add_text, get_all_texts
from ui import create_main_window, create_frame, create_add_button
from features.delete_feature import add_delete_buttons  # We'll write this next

conn, cursor = connect_db()
root = create_main_window()
frame = create_frame(root)

def copy_text(text):
    pyperclip.copy(text)

def refresh_list():
    for widget in frame.winfo_children():
        widget.destroy()
    texts = get_all_texts(cursor)
    for text_id, text in texts:
        add_delete_buttons(frame, text_id, text, cursor, conn, refresh_list, copy_text)

def handle_add():
    new_text = simpledialog.askstring("New Text", "Enter text:")
    if new_text:
        add_text(cursor, conn, new_text)
        refresh_list()

create_add_button(root, handle_add)
refresh_list()
root.mainloop()
