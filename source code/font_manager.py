import tkinter.font as tkfont  # Import the font module from Tkinter

def configure():
    # Function to configure default font settings for the Tkinter application

    family = "Helvetica"  # Set the desired font family to "Helvetica"

    # Get the default font used in the application 
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=12, family=family)  # Configure the default font to use the Helvetica family and size 12

    # Get the font used in text widgets 
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=10, family=family)  # Configure the text font to use the Helvetica family and size 10

    # Get the font used in fixed-width text 
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=10, family=family)  # Configure the fixed font to use the Helvetica family and size 10
