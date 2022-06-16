from tkinter import simpledialog

from cefpython3 import cefpython as cef
import spotipy
import webbrowser
import tkinter
import customtkinter  # credit to Tom Schimansky
from PIL import Image, ImageTk
import os
import sys
import platform
import logging as _logging
import tkinter.filedialog
import Diagnostics.diagnostic_to_metric as diagnostic_to_metric, Diagnostics.system as system
import json

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))
embeded_code = ''


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

# Generate playlist based off of genres
def generatePlaylist():
    global embeded_code
    # Generate new playlist based on cpu usage
    usage = diagnostic_to_metric.genre_from_cpu()
    newPlaylist = spotifyObj.recommendations(seed_genres=usage,limit=25)

    #print the content in an easy to read format(derived from JSON)
    track_list = newPlaylist['tracks']
    list_of_songs = []
    list_of_song_names = []
    for tracks in track_list:
        list_of_song_names.append(tracks['name'])
        list_of_songs.append(tracks['uri'])
    #print(json.dumps(newPlaylist,indent=4, sort_keys=4))


    #create playlist
    playlist_name = 'Genres: '
    for genre in usage:
        playlist_name = playlist_name + ' ' + genre
    print(playlist_name)
    playlist_description = 'Songs inspired with '
    for genre in usage:
        playlist_description = playlist_description + ' ' + genre
    print(playlist_description)
    spotifyObj.user_playlist_create(user=spotifyObj.me()['id'],name=playlist_name,public=True,description=playlist_description)

    #identify id of newest playlist
    prePlaylists = spotifyObj.user_playlists(user=spotifyObj.me()['id'])
    playlist = prePlaylists['items'][0]['id']

    #add 25 songs
    spotifyObj.user_playlist_add_tracks(user=spotifyObj.me()['id'], playlist_id=playlist, tracks=list_of_songs)

    # Retrieve embedded code of playlist
    url = prePlaylists['items'][0]['external_urls']['spotify']
    embeded_code = f'<iframe style=\"border-radius:12px\" src=\"{url}\" width=\"100%\" height=\"380\" frameBorder=\"0\" allowfullscreen=\"\" allow=\"autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture\"></iframe>'


# Spotify API connection and setup
# Be sure to set environment variables with API client ids.
# SPOTIFY_CLIENT_ID (Required)
# SPOTIPY_CLIENT_SECRET (Required)
# SPOTIPY_REDIRECT_URI (Maybe  on this one)

scope = 'user-top-read user-read-playback-state streaming ugc-image-upload playlist-modify-public'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://google.com/'
#os.environ['SPOTIPY_CLIENT_SECRET'] = ''
#os.environ['SPOTIFY_CLIENT_ID'] = ''
try:
    auth_manager = spotipy.oauth2.SpotifyOAuth(show_dialog=True, scope=scope)
    spotifyObj = spotipy.Spotify(auth_manager=auth_manager)
    auth_url = auth_manager.get_authorize_url()
    #webbrowser.open_new_tab(auth_url)
    auth_manager.get_auth_response()
    # msg = "Please copy and paste the URL you were redirected to after clicking the green \"Agree\" button."
    # ROOT = tk.Tk()
    # ROOT.withdraw()
    # user_input = simpledialog.askstring()
    # #title="Validation", prompt=msg
    # print(spotifyObj.me()['id'])
    generatePlaylist()
except KeyboardInterrupt:
    print("I messed up.")


if __name__ == "__main__":
    app = App()
    app.start()
