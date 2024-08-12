import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from core.authentication import register_user
from ui.utils import create_label, create_entry, create_button, define_colors

class RegistrationWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app  # Store the app instance
        master.title("Register")

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

        # Create main container frame for registration form
        self.form_frame = ctk.CTkFrame(self.main_frame, bg_color=self.SECONDARY_COLOR, corner_radius=12, width=450, height=700)
        self.form_frame.pack(side="right", fill="both", expand=True)

        # Configure grid for centering elements
        self.form_frame.grid_propagate(False)  # Prevent the frame from resizing
        self.form_frame.grid_rowconfigure(0, weight=0)  # Adjusted weight to push elements down
        self.form_frame.grid_rowconfigure(1, weight=0)
        self.form_frame.grid_rowconfigure(2, weight=0)
        self.form_frame.grid_rowconfigure(3, weight=0)
        self.form_frame.grid_rowconfigure(4, weight=0)  # Increased weight for spacing below button

        # Create widgets using reusable functions
        self.first_name_label = create_label(self.form_frame, "First Name:", self.TEXT_COLOR, ("Arial", 16))
        self.first_name_label.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="e")

        self.first_name_entry = create_entry(self.form_frame, "Enter your first name", self.TEXT_COLOR, ("Arial", 16))
        self.first_name_entry.grid(row=0, column=1, padx=(10, 20), pady=10, sticky="w")  

        self.last_name_label = create_label(self.form_frame, "Last Name:", self.TEXT_COLOR, ("Arial", 16))
        self.last_name_label.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="e")

        self.last_name_entry = create_entry(self.form_frame, "Enter your last name", self.TEXT_COLOR, ("Arial", 16))
        self.last_name_entry.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="w")  

        self.email_label = create_label(self.form_frame, "Email Address:", self.TEXT_COLOR, ("Arial", 16))
        self.email_label.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="e")

        self.email_entry = create_entry(self.form_frame, "Enter your email", self.TEXT_COLOR, ("Arial", 16))
        self.email_entry.grid(row=2, column=1, padx=(10, 20), pady=10, sticky="w")  

        self.password_label = create_label(self.form_frame, "Password:", self.TEXT_COLOR, ("Arial", 16))
        self.password_label.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="e")

        self.password_entry = create_entry(self.form_frame, "Enter your password", self.TEXT_COLOR, ("Arial", 16), show="*")
        self.password_entry.grid(row=3, column=1, padx=(10, 20), pady=10, sticky="w")  

        self.confirm_password_label = create_label(self.form_frame, "Confirm Password:", self.TEXT_COLOR, ("Arial", 16))
        self.confirm_password_label.grid(row=4, column=0, padx=(20, 10), pady=10, sticky="e")

        self.confirm_password_entry = create_entry(self.form_frame, "Confirm your password", self.TEXT_COLOR, ("Arial", 16), show="*")
        self.confirm_password_entry.grid(row=4, column=1, padx=(10, 20), pady=10, sticky="w")  

        self.register_button = create_button(self.form_frame, "Register", self.register, "#007BFF", self.SECONDARY_COLOR, ("Arial", 16))
        self.register_button.grid(row=5, columnspan=2, padx=20, pady=(10, 20))

        # Already have an account? link
        self.login_link = create_button(self.form_frame, "Already have an account? Login", self.show_login, self.SECONDARY_COLOR, "#007BFF", ("Arial", 14))
        self.login_link.grid(row=6, columnspan=2, padx=5, pady=(5, 20))  # Adjusted padding for spacing

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            self.show_error_message("Error", "Passwords do not match.")
            return

        if register_user(email, password, first_name, last_name):
            self.show_info_message("Success", "Registration Successful!")
            self.show_login(None)
        else:
            self.show_error_message("Error", "Registration failed. Please try again.")

    def show_info_message(self, title, message):
        """Show an info message box."""
        tk.messagebox.showinfo(title, message)

    def show_error_message(self, title, message):
        """Show an error message box."""
        tk.messagebox.showerror(title, message)

    def show_login(self, event=None):
        """Switch to the login window using the app instance."""
        self.app.show_login_window()
