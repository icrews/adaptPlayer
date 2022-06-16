import tkinter
from cefpython3 import cefpython as cef
import customtkinter  # credit to Tom Schimansky
from PIL import Image, ImageTk
import os
import sys
import platform
import logging as _logging
import tkinter.filedialog

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


# def button_callback():
#     print("Button click", combobox_1.get())
#
#
# def slider_callback(value):
#     progressbar_1.set(value)

# Fix for PyCharm hints warnings
WindowUtils = cef.WindowUtils()

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

# Globals
logger = _logging.getLogger("tkinter_.py")

# Constants
# Tk 8.5 doesn't support png images
IMAGE_EXT = ".png" if tkinter.TkVersion > 8.5 else ".gif"


def button_function():
    print("Login pressed")


class App(customtkinter.CTk):


    APP_NAME = "DaddyApp"
    WIDTH = 350
    HEIGHT = 1200

    def __init__(self, *args, **kwargs):
        # Setup
        super().__init__(*args, **kwargs)
        play_image = ImageTk.PhotoImage(Image.open(PATH + "/images/play.png"))
        pause_image = ImageTk.PhotoImage(Image.open(PATH + "/images/pause.png"))
        next_image = ImageTk.PhotoImage(Image.open(PATH + "/images/next.png"))
        back_image = ImageTk.PhotoImage(Image.open(PATH + "/images/back.png"))
        refresh_image = ImageTk.PhotoImage(Image.open(PATH + "/images/rotate.png"))
        setting_image = ImageTk.PhotoImage(Image.open(PATH + "/images/setting.png"))
        close_image = ImageTk.PhotoImage(Image.open(PATH + "/images/close.png"))


        # Size Control
        self.title(App.APP_NAME)
        self.resizable(False,False)
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.attributes('-alpha', 0.5) # Transparent Window
        self.overrideredirect(True)

        image = Image.open(PATH + "/images/OratorBG.png").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)
        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        self.button_2 = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c",
                                              image=close_image, text="", command=self.close_button)
        self.button_2.pack(side="right", padx=40, pady=40)
        self.button = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c",
                                              image=refresh_image, text="", command=self.create_new_window)
        self.button.pack(side="top", padx=40, pady=40)
        self.button_3 = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c",
                                                image=setting_image, text="", command=self.open)
        self.button_3.pack(side="bottom", padx=40, pady=40)


    def close_button(self):
        self.destroy()

    def on_closing(self, event=0):
        self.destroy()

    def create_new_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")
        self.overrideredirect(True)

    def open(self):
        PathPy = tkinter.filedialog.askopenfilename(title="Open a file", filetypes=[('PYTHON file', '.py')])
        os.system('%s %s' % (sys.executable, PathPy))

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()








