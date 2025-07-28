# features/search_feature.py

from db import search_texts
from ui import display_texts

def setup_search_ui(root, display_frame):
    import tkinter as tk

    search_var = tk.StringVar()

    search_entry = tk.Entry(root, textvariable=search_var)
    search_entry.pack(fill='x', padx=5, pady=5)

    def update_display(*args):
        query = search_var.get()
        if query.strip():
            results = search_texts(query)
        else:
            results = search_texts("")  # Show all
        display_texts(display_frame, results)

    search_var.trace_add("write", update_display)

   # Initial display of all texts
    display_texts(display_frame, search_texts(""))
