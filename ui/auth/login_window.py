import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from core.authentication import authenticate_user
from ui.utils import create_label, create_entry, create_button, define_colors

class LoginWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app  # Store the app instance
        master.title("Login")

        # Set the appearance mode and color theme
        ctk.set_appearance_mode("Light")  # "Dark" or "Light"
        ctk.set_default_color_theme("blue")  # Predefined theme: "blue"

        # Define colors
        colors = define_colors()
        self.PRIMARY_COLOR = colors['PRIMARY_COLOR']
        self.SECONDARY_COLOR = colors['SECONDARY_COLOR']
        self.TEXT_COLOR = colors['TEXT_COLOR']

        # Set window size
        master.geometry("900x700")

        # Create a frame to hold the image and form side by side
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill="both", expand=True)

        # Load and display the image on the left side
        self.image_frame = tk.Frame(self.main_frame, width=450, height=700)
        self.image_frame.pack(side="left", fill="both", expand=True)

        image = Image.open("resources/images/auth-hero.jpg")
        self.image = ImageTk.PhotoImage(image.resize((450, 700)))
        self.image_label = tk.Label(self.image_frame, image=self.image)
        self.image_label.pack(fill="both", expand=True)

        # Create main container frame for login form
        self.form_frame = ctk.CTkFrame(self.main_frame, bg_color=self.SECONDARY_COLOR, width=450, height=700)
        self.form_frame.pack(side="right", fill="both", expand=True)

        # Configure grid for centering elements
        self.form_frame.grid_propagate(False)  # Prevent the frame from resizing
        self.form_frame.grid_rowconfigure(0, weight=2)
        self.form_frame.grid_rowconfigure(1, weight=0)
        self.form_frame.grid_rowconfigure(2, weight=0)
        self.form_frame.grid_rowconfigure(3, weight=0)
        self.form_frame.grid_rowconfigure(4, weight=0)
        self.form_frame.grid_rowconfigure(5, weight=2)
        

        
        # Create widgets using reusable functions
        self.username_label = create_label(self.form_frame, "Username:", self.TEXT_COLOR, ("Arial", 16))
        self.username_label.grid(row=1, column=0, pady=0, sticky="e")

        self.username_entry = create_entry(self.form_frame, "Enter username", self.TEXT_COLOR, ("Arial", 16))
        self.username_entry.grid(row=1, column=1, sticky="w")  

        self.password_label = create_label(self.form_frame, "Password:", self.TEXT_COLOR, ("Arial", 16))
        self.password_label.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="e")

        self.password_entry = create_entry(self.form_frame, "Enter password", self.TEXT_COLOR, ("Arial", 16), show="*")
        self.password_entry.grid(row=2, column=1, sticky="w")  

        self.login_button = create_button(self.form_frame, "Login", self.login, "#007BFF", self.SECONDARY_COLOR, ("Arial", 16))
        self.login_button.grid(row=3, columnspan=2, padx=20, pady=10)

        # Register Now link
        self.register_button = create_button(self.form_frame, "Don't have an account? Register Now", self.show_registration, self.SECONDARY_COLOR, "#007BFF", ("Arial", 14))
        self.register_button.grid(row=4, columnspan=2, padx=5, pady=(5, 20))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if authenticate_user(username, password):
            self.show_info_message("Success", "Login Successful!")
            self.master.destroy()
        else:
            self.show_error_message("Error", "Invalid username or password.")

    def show_info_message(self, title, message):
        """Show an info message box."""
        tk.messagebox.showinfo(title, message)

    def show_error_message(self, title, message):
        """Show an error message box."""
        tk.messagebox.showerror(title, message)

    def show_registration(self):
        """Switch to the registration window using the app instance."""
        self.app.show_registration_window()
