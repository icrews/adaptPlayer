from asyncio import subprocess
import imp
from multiprocessing.connection import wait
from time import sleep
import tkinter as tk
from tkinter import simpledialog
import customtkinter # credit to Tom Schimansky
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
import spotipy
import webbrowser
import subprocess
from subprocess import Popen, PIPE
import os
import multiprocessing
import socketserver
import http.server


window = customtkinter.CTk()
window.title("adaptPlayer")
window.geometry("600x400")

low_genre = []
mid_genre = []
high_genre = []
max_genre = []


def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)

# Generate playlist based off of genres
def generatePlaylist():
    
    possibleG = spotifyObj.recommendation_genre_seeds()
    print(possibleG)

# Run server for authentication experience
# subprocess.call('python miniServer.py', shell=True)
# def run_webserver():
#     os.chdir("./www/public")
#     PORT = 5000
#     Handler = http.server.SimpleHTTPRequestHandler
#     httpd = socketserver.TCPServer(('0.0.0.0', PORT), Handler)

#     #the following throws an exception
#     #with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
#     #    print("serving at port", PORT)

#     httpd.serve_forever(poll_interval=0.5)

#     return


# p = multiprocessing.Process(target=run_webserver, args=())
# p.daemon = True
# p.start()

# print("Server is up and running")


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


generatePlaylist()


# Application UI Layout
frame_1 = customtkinter.CTkFrame(master=window)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tk.LEFT)
label_1.pack(pady=12, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=12, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=12, padx=10)

radiobutton_var = tk.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.pack(pady=12, padx=10)

# Render the application
window.mainloop()
label = tk.Label(text = "Creating a test desktop window")
label.grid(column=0, row=0)