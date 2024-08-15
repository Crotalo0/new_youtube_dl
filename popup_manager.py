import tkinter as tk
from tkinter import ttk


class PopupManager:
    def __init__(self, parent):
        self.parent = parent
        self.popup = None
        self.progress_bar = None

    def show_progress_popup(self, title="Progress", message=""):
        if self.popup is not None:
            self.close_popup()

        self.popup = tk.Toplevel(self.parent)
        self.popup.title(title)

        frame = ttk.Frame(self.popup, padding=10)
        frame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        label = ttk.Label(frame, text=message, wraplength=300)
        label.grid(row=0, column=0, pady=10, padx=20)

        self.progress_bar = ttk.Progressbar(
            frame, orient="horizontal", mode="indeterminate"
        )
        self.progress_bar.grid(row=1, column=0, pady=10, padx=20, sticky=tk.E + tk.W)

        self.popup.geometry("350x150")
        self.progress_bar.start(10)

    def update_progress(self, value):
        if self.progress_bar:
            self.progress_bar["value"] = value
            self.progress_bar.update()

    def close_popup(self):
        if self.popup is not None:
            self.progress_bar.stop()
            self.popup.destroy()
            self.popup = None
            self.progress_bar = None
