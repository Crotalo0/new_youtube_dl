from popup_manager import PopupManager
from download_manager import DownloadManager
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from time import perf_counter
import utils
import threading


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.save_path = ""
        self.popup_manager = PopupManager(self)
        self.create_widgets()

    def create_widgets(self):
        self["padx"] = 10
        self["pady"] = 5

        def clear():
            url_entry.delete(0, "end")

        def save_path():
            self.save_path = filedialog.askdirectory()
            if self.save_path:
                save_path_label["text"] = self.save_path

        def downloader():
            link = url_entry.get()
            if not link:
                messagebox.showwarning("Input Error", "Please enter a YouTube URL")
                return

            download_choice = download_choice_var.get()
            if not self.save_path:
                messagebox.showwarning("Save Path", "Please select a save path")
                return

            self.popup_manager.show_progress_popup(
                "Downloading", "Download in progress..."
            )
            start = perf_counter()

            def download_task():
                try:
                    dm = DownloadManager(self.save_path)

                    if download_choice == "audio":
                        audio_path = dm.download_audio(link)
                        self.popup_manager.close_popup()
                        messagebox.showinfo("Success", "Audio downloaded successfully!")
                    else:
                        video_path = dm.download_video(link)
                        audio_path = dm.download_audio(link)

                        self.popup_manager.show_progress_popup(
                            "Merging",
                            "Merging video and audio. This may take a while...",
                        )

                        dm.merge_video_audio(video_path, audio_path)
                        self.popup_manager.close_popup()
                        messagebox.showinfo(
                            "Success", "Video and audio merged successfully!"
                        )

                except Exception as e:
                    print(e)
                    self.popup_manager.close_popup()
                    messagebox.showerror(
                        "Error",
                        "An error occurred. Check your internet connection and the link.",
                    )
                finally:
                    end = perf_counter()
                    hour, minutes, seconds = utils.sec_converter(end - start)
                    messagebox.showinfo(
                        "Finished",
                        f"Process completed in {int(hour)}h {int(minutes)}m {int(seconds)}s.",
                    )

            # Run the download and merge process in a separate thread
            download_thread = threading.Thread(target=download_task)
            download_thread.start()

        url_frame = ttk.LabelFrame(self, text=" YouTube URL ", relief=tk.RIDGE)
        url_frame.grid(
            row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S, padx=10, pady=10
        )

        url_label = ttk.Label(url_frame, text="Enter URL:")
        url_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)

        url_entry = ttk.Entry(url_frame)
        url_entry.grid(row=0, column=1, sticky=tk.E, pady=5, padx=10, ipadx=90)

        right_click_menu = tk.Menu(self, tearoff=0)
        right_click_menu.add_command(label="Clear", command=clear)
        url_entry.bind(
            "<Button-3>",
            lambda event: right_click_menu.tk_popup(event.x_root, event.y_root),
        )

        choice_frame = ttk.LabelFrame(self, text=" Download Option ", relief=tk.RIDGE)
        choice_frame.grid(
            row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S, padx=10, pady=10
        )

        download_choice_var = tk.StringVar(value="both")
        audio_radio = ttk.Radiobutton(
            choice_frame, text="Only Audio", variable=download_choice_var, value="audio"
        )
        audio_radio.grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)

        both_radio = ttk.Radiobutton(
            choice_frame,
            text="Audio and Video",
            variable=download_choice_var,
            value="both",
        )
        both_radio.grid(row=1, column=0, sticky=tk.W, pady=5, padx=10)

        path_frame = ttk.LabelFrame(self, text=" Save Location ", relief=tk.RIDGE)
        path_frame.grid(
            row=2, column=0, sticky=tk.E + tk.W + tk.N + tk.S, padx=10, pady=10
        )

        save_path_btn = ttk.Button(
            path_frame, text="Select Save Path", command=save_path
        )
        save_path_btn.grid(row=0, column=0, sticky=tk.W, pady=5, padx=10)

        save_path_label = ttk.Label(
            path_frame, text="No folder selected", font=("Calibri", 10, "italic")
        )
        save_path_label.grid(row=0, column=1, sticky=tk.W, pady=5, padx=10)

        download_btn = ttk.Button(self, text="Download", command=downloader)
        download_btn.grid(
            row=3, column=0, sticky=tk.W, pady=20, padx=10, ipadx=40, ipady=10
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
