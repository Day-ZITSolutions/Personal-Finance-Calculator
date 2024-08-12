import tkinter as tk
from ui.auth.login_window import LoginWindow
from ui.auth.registration_window import RegistrationWindow

class PersonalFinanceManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        # Set the appearance mode and color theme for customtkinter
        ctk.set_appearance_mode("Light")  # "Dark" or "Light"
        ctk.set_default_color_theme("blue")  # Use custom blue color

        # Define colors
        self.PRIMARY_COLOR = "#0033A0"  # Modern Blue
        self.SECONDARY_COLOR = "#FFFFFF"  # White for contrast
        self.TEXT_COLOR = "#000000"  # Black text for readability

        # Configure window size to be full width and height
        self.root.geometry("900x700")  # Fixed window size (width x height)
        self.root.resizable(False, False)  # Disable resizing

        # Create the menu bar with custom styling
        self.menubar = tk.Menu(root, background=self.PRIMARY_COLOR, foreground=self.TEXT_COLOR, font=("Arial", 12))
        
        # File menu with custom styling
        self.filemenu = tk.Menu(self.menubar, tearoff=0, background=self.SECONDARY_COLOR, foreground=self.TEXT_COLOR, font=("Arial", 12))
        self.filemenu.add_command(label="Login", command=self.show_login_window, background=self.SECONDARY_COLOR, foreground=self.TEXT_COLOR)
        self.filemenu.add_command(label="Register", command=self.show_registration_window, background=self.SECONDARY_COLOR, foreground=self.TEXT_COLOR)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit, background=self.SECONDARY_COLOR, foreground=self.TEXT_COLOR)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Configure the menu
        root.config(menu=self.menubar)

        # Show the login window by default
        self.show_login_window()

    def clear_window(self):
        """Destroys all widgets in the root window, if it exists."""
        if self.root.winfo_exists():
            for widget in self.root.winfo_children():
                widget.destroy()

    def show_login_window(self):
        """Clears the window and shows the login window."""
        self.clear_window()
        LoginWindow(self.root, self)

    def show_registration_window(self):
        """Clears the window and shows the registration window."""
        self.clear_window()
        RegistrationWindow(self.root, self)

if __name__ == "__main__":
    import customtkinter as ctk  # Import customtkinter for custom styling
    root = tk.Tk()
    app = PersonalFinanceManagerApp(root)
    root.mainloop()
