import tkinter
import customtkinter  # credit to Tom Schimansky
from PIL import Image, ImageTk
import os

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


# def button_callback():
#     print("Button click", combobox_1.get())
#
#
# def slider_callback(value):
#     progressbar_1.set(value)



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

        self.button = customtkinter.CTkButton(self, border_color="#D35B58", fg_color="#c0392b", hover_color="#e74c3c", image=refresh_image, text="", command=self.create_new_window)
        self.button.pack(side="top", padx=40, pady=40)




    def button_function(self):
        print("Login pressed")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def create_new_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")
        self.overrideredirect(True)




if __name__ == "__main__":
    app = App()
    app.start()


# frame_1 = customtkinter.CTkFrame(master=window)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)
#
# label_1 = customtkinter.CTkLabel(master=frame_1, justify=tk.LEFT, text="Lady")
# label_1.pack(pady=12, padx=10)
#
# progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
# progressbar_1.pack(pady=12, padx=10)
#
# button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Daddy")
# button_1.pack(pady=12, padx=10)
#
# slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
# slider_1.pack(pady=12, padx=10)
# slider_1.set(0.5)
#
# entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
# entry_1.pack(pady=12, padx=10)
#
# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=12, padx=10)
# optionmenu_1.set("CTkOptionMenu")
#
# combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# combobox_1.pack(pady=12, padx=10)
# combobox_1.set("CTkComboBox")
#
# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=12, padx=10)
#
# radiobutton_var = tk.IntVar(value=1)
#
# radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
# radiobutton_1.pack(pady=12, padx=10)
#
# radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
# radiobutton_2.pack(pady=12, padx=10)
#
# switch_1 = customtkinter.CTkSwitch(master=frame_1)
# switch_1.pack(pady=12, padx=10)






