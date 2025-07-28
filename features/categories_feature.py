# features/categories_feature.py
import tkinter as tk
from tkinter import simpledialog
from db import get_all_categories, add_category, update_text_category

def setup_categories_ui(root, refresh_callback):
    frame = tk.Frame(root)
    frame.pack(fill="x", pady=5)

    lbl = tk.Label(frame, text="Categories:")
    lbl.pack(side="left", padx=5)

    cursor = refresh_callback.__globals__['cursor']
    conn = refresh_callback.__globals__['conn']

    def update_categories():
        return get_all_categories(cursor)

    categories = update_categories()
    category_names = [name for _, name in categories]
    selected_category = tk.StringVar(value="All")

    def on_category_selected(*args):
        name = selected_category.get()
        if name == "All":
            refresh_callback()
        else:
            cid = next((cid for cid, cname in categories if cname == name), None)
            texts = cursor.execute("SELECT id, content FROM texts WHERE category_id=?", (cid,)).fetchall()
            refresh_callback(texts=texts)

    option_menu = tk.OptionMenu(frame, selected_category, "All", *category_names, command=lambda _: on_category_selected())
    option_menu.pack(side="left")

    def add_new_category():
        new_cat = simpledialog.askstring("New Category", "Enter new category name:")
        if new_cat:
            add_category(cursor, conn, new_cat)
            nonlocal categories
            categories = update_categories()
            menu = option_menu["menu"]
            menu.delete(0, "end")
            menu.add_command(label="All", command=lambda: selected_category.set("All"))
            for name in [n for _, n in categories]:
                menu.add_command(label=name, command=lambda v=name: selected_category.set(v))
            selected_category.set(new_cat)
            on_category_selected()

    btn_add_cat = tk.Button(frame, text="Add Category", command=add_new_category)
    btn_add_cat.pack(side="left", padx=5)

def assign_category_ui(parent, text_id, cursor, conn, refresh_callback):
    categories = get_all_categories(cursor)

    def assign(cat_name):
        category_id = next((cid for cid, name in categories if name == cat_name), None)
        if category_id:
            update_text_category(cursor, conn, text_id, category_id)
            refresh_callback()

    if categories:
        menu = tk.Menu(parent, tearoff=0)
        for _, name in categories:
            menu.add_command(label=name, command=lambda n=name: assign(n))
        return menu
    return None
 