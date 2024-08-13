import tkinter as tk  # Importing tkinter for GUI components
import font_manager as fonts  # Importing the font_manager for custom fonts
from check_video import CheckVideos  # Importing CheckVideos class
from create_video_list import CreateVideoList  # Importing CreateVideoList class
from update_video import UpdateVideos  # Importing UpdateVideos class
from new_gui import new_gui  # Importing new_gui function

# Function to handle the "Check Videos" button click event
def check_videos_clicked():
    status_lbl.configure(text="Check Videos button clicked!")  # Update the status label
    CheckVideos(tk.Toplevel(window))  # Open a new window with the CheckVideos interface

# Function to handle the "Create Video List" button click event
def create_videos_clicked():
    status_lbl.configure(text="Create Videos List button clicked!")  # Update the status label
    CreateVideoList(tk.Toplevel(window))  # Open a new window with the CreateVideoList interface

# Function to handle the "Update Videos" button click event
def update_videos_clicked():
    status_lbl.configure(text="Update Videos button clicked!")  # Update the status label
    UpdateVideos(tk.Toplevel(window))  # Open a new window with the UpdateVideos interface

# Function to handle the "New GUI" button click event
def new_gui_clicked():
    status_lbl.configure(text="New GUI button clicked!")  # Update the status label
    new_gui(tk.Toplevel(window))  # Open a new window with the new GUI interface

# Main window setup
window = tk.Tk()  # Create the main application window
window.geometry("550x150")  # Set the window size
window.title("Video Player")  # Set the window title
window.configure(bg="lightblue")  # Set the background color

fonts.configure()  # Configure the fonts using the font_manager

# Header label with instructions
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below:", bg="lightblue")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Position the header label

# Button to check videos
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)  # Position the button

# Button to create a video list
create_video_list_btn = tk.Button(window, text="Create Video List", command=create_videos_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)  # Position the button

# Button to update videos
update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)  # Position the button

# Button for new GUI
new_gui_button = tk.Button(window, text="New GUI", command=new_gui_clicked)
new_gui_button.grid(row=1, column=3, padx=10, pady=10)  # Position the button

# Status label to display messages based on button clicks
status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="lightblue")
status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)  # Position the status label

# Start the main application loop
window.mainloop()
