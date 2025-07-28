import tkinter as tk
from tkinter import simpledialog
import pyperclip

from db import (
    connect_db, add_text, get_all_texts,
    delete_text, update_text
)
from ui import create_main_window, create_frame, create_add_button
from features.delete_feature import handle_delete
from features.search_feature import setup_search_ui
from features.edit_feature import handle_edit
from features.categories_feature import setup_categories_ui, assign_category_ui  # ⬅️ new
from features.autoclose_feature import setup_autoclose_ui, should_autoclose

conn, cursor = connect_db()
root = create_main_window()
frame = create_frame(root)

def copy_text(text):
    pyperclip.copy(text)
    if should_autoclose():
        root.destroy()


def refresh_list(texts=None):
    for widget in frame.winfo_children():
        widget.destroy()
    if texts is None:
        texts = get_all_texts(cursor)

    for text_id, text in texts:
        item_frame = tk.Frame(frame)
        item_frame.pack(fill="x", pady=2)

        btn_copy = tk.Button(item_frame, text=text, command=lambda t=text: copy_text(t), width=20, anchor="w")
        btn_copy.pack(side="left", padx=5)

        btn_edit = tk.Button(item_frame, text="✏️", command=lambda i=text_id, t=text: edit_text(i, t), width=3)
        btn_edit.pack(side="left", padx=5)

        btn_delete = tk.Button(item_frame, text="🗑", command=lambda i=text_id: delete_text_and_refresh(i), width=3)
        btn_delete.pack(side="right", padx=5)

        # دکمه دسته‌بندی
        btn_cat = tk.Button(item_frame, text="📂", width=3)
        btn_cat.pack(side="right", padx=5)

        menu = assign_category_ui(root, text_id, cursor, conn, refresh_list)
        if menu:
            btn_cat.bind("<Button-1>", lambda e, m=menu: m.tk_popup(e.x_root, e.y_root))

def delete_text_and_refresh(text_id):
    delete_text(cursor, conn, text_id)
    refresh_list()

def edit_text(text_id, current_text):
    new_text = simpledialog.askstring("Edit Text", "Modify text:", initialvalue=current_text)
    if new_text and new_text != current_text:
        update_text(cursor, conn, text_id, new_text)
        refresh_list()

def handle_add():
    new_text = simpledialog.askstring("New Text", "Enter text:")
    if new_text:
        add_text(cursor, conn, new_text)
        refresh_list()

create_add_button(root, handle_add)
setup_autoclose_ui(root)
setup_search_ui(root, frame)
setup_categories_ui(root, refresh_list)  # ⬅️ new
refresh_list()
root.mainloop()
