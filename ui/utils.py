import customtkinter as ctk

def create_label(parent, text, text_color, font):
    return ctk.CTkLabel(parent, text=text, text_color=text_color, font=font)

def create_entry(parent, placeholder_text, text_color, font, show=None):
    return ctk.CTkEntry(parent, placeholder_text=placeholder_text, text_color=text_color, font=font, 
                        show=show, border_width=0, corner_radius=8)

def create_button(parent, text, command, fg_color, text_color, font):
    return ctk.CTkButton(parent, text=text, command=command, fg_color=fg_color, text_color=text_color, 
                        font=font, corner_radius=8)

def define_colors():
    return {
        'PRIMARY_COLOR': "#0033A0",  # Modern Blue
        'SECONDARY_COLOR': "#FFFFFF",  # White for the container
        'TEXT_COLOR': "#000000"  # Black text
    }
