from tkinter import simpledialog
import spotipy
import webbrowser
import tkinter
import customtkinter  # credit to Tom Schimansky
from PIL import Image, ImageTk
import os
import Diagnostics.diagnostic_to_metric as diagnostic_to_metric, Diagnostics.system as system

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


# def button_callback():
#     print("Button click", combobox_1.get())
#
#
# def slider_callback(value):
#     progressbar_1.set(value)


low_genre = []
mid_genre = []
high_genre = []
max_genre = []

class App(customtkinter.CTk):

    APP_NAME = "DaddyApp"
    WIDTH = 350
    HEIGHT = 1200

    def close_button(self):
        self.destroy()

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
        self.geometry("350x1200+100+100")

        image = Image.open(PATH + "/images/OratorBG.png").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)
        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c",
                                              image=refresh_image, text="", command=self.create_new_window)
        self.button.pack(side="top", padx=40, pady=40)
        self.button = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c",
                                              image=close_image, text="", command=self.close_button())
        self.button.pack(side="right", padx=40, pady=40)
    
    def create_new_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")
        self.overrideredirect(True)
    

        



    def button_function(self):
        print("Login pressed")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

# Generate playlist based off of genres
def generatePlaylist():
    
    newPlaylist = spotifyObj.recommendations(seed_genres=diagnostic_to_metric.genre_from_cpu(),)
    

# Spotify API connection and setup
# Be sure to set environment variables with API client ids.
# SPOTIFY_CLIENT_ID (Required)
# SPOTIPY_CLIENT_SECRET (Required)
# SPOTIPY_REDIRECT_URI (Maybe  on this one)

scope = 'user-top-read user-read-playback-state streaming ugc-image-upload playlist-modify-public'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://google.com/'
try:
    auth_manager = spotipy.oauth2.SpotifyOAuth(show_dialog=True, scope=scope)
    spotifyObj = spotipy.Spotify(auth_manager=auth_manager)
    print("I theoretically worked.")
    auth_url = auth_manager.get_authorize_url()
    #webbrowser.open_new_tab(auth_url)
    #auth_manager.get_auth_response()
    # msg = "Please copy and paste the URL you were redirected to after clicking the green \"Agree\" button."
    # ROOT = tk.Tk()
    # ROOT.withdraw()
    # user_input = simpledialog.askstring()
    # #title="Validation", prompt=msg
except:
    print("I messed up.")


if __name__ == "__main__":
    app = App()
    app.start()
