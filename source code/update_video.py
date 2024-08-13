import tkinter as tk  # Import the tkinter module for creating the GUI
import video_library as lib  # Import the video_library module to access video-related functions
import font_manager as fonts  # Import the font_manager module to configure font settings

def set_text(text_area, content):
    # A utility function to set the content of a text area
    text_area.delete("1.0", tk.END)  # Delete any existing content in the text area
    text_area.insert(1.0, content)  # Insert the new content at the start of the text area

class UpdateVideos:
    def __init__(self, window):
        # Constructor to initialize the UpdateVideos class and set up the GUI
        window.geometry("420x320")  # Set the window size to 420x320 pixels
        window.title("Update Videos")  # Set the window title to "Update Videos"
        window.configure(bg="lightblue")  # Set the background color of the window to light blue
        # Label for entering the video number
        entervideo_lbl = tk.Label(window, text="Enter Video Number", width=20, relief="solid", bg="red")
        entervideo_lbl.grid(row=0, column=0, sticky="W", padx=10, pady=10)  # Place the label in the grid layout
        # Entry box for inputting the video number
        self.input_number_txt = tk.Entry(window, width=3)
        self.input_number_txt.grid(row=0, column=1, sticky="W", padx=10, pady=10)  # Place the entry box next to the label
        # Label for entering the new rating
        enter_new_rating_lbl = tk.Label(window, text="Enter New Rating", width=20, relief="solid", bg="red")
        enter_new_rating_lbl.grid(row=1, column=0, sticky="W", padx=10, pady=10)  # Place the label in the grid layout
        # Entry box for inputting the new rating
        self.input_rating_txt = tk.Entry(window, width=3)
        self.input_rating_txt.grid(row=1, column=1, padx=10, pady=10)  # Place the entry box next to the label
        # Text area to display the update status
        self.update_txt = tk.Text(window, width=52, height=7, wrap="none")
        self.update_txt.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place the text area in the grid layout
        # Button to trigger the video update process
        update_video_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)
        update_video_btn.grid(row=0, column=2, rowspan=2, sticky="W", padx=10, pady=10)  # Place the button next to the entry boxes
        # Label to display the status of the update process
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="red", bg="lightblue")
        self.status_lbl.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)#Place the status label at the bottom of the window
        # Label to display any additional messages or errors
        self.updated_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="red", bg="lightblue")
        self.updated_lbl.grid(row=6, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Place the message label below the status label

    def update_video_clicked(self):
        # Method to handle the update video button click event
        key = self.input_number_txt.get()  # Get the video number entered by the user
        new_rating_1 = self.input_rating_txt.get()  # Get the new rating entered by the user
        name = lib.get_name(key)  # Retrieve the video name based on the video number
        if name:  # If the video exists
            if new_rating_1.isdigit():  # Check if the entered rating is a valid digit
                new_rating = int(new_rating_1)  # Convert the rating to an integer
                if 0 <= new_rating <= 5:  # Check if the rating is within the valid range (0 to 5)
                    lib.set_rating(key, new_rating)  # Update the video rating in the library
                    update_rating = lib.get_rating(key)  # Retrieve the updated rating
                    new_details = f"\"{name}\" rating updated to {update_rating}"  # Create a message with the updated rating
                    set_text(self.update_txt, new_details)  # Display the updated rating in the text area
                    self.updated_lbl.configure(text="")  # Clear any previous messages
                else:
                    self.updated_lbl.configure(text="Invalid rating! Please enter a valid rating (0 to 5)")  # Display an error for an invalid rating
            else:
                self.updated_lbl.configure(text="Invalid rating! Please enter a valid rating (0 to 5)")  # Display an error for non-numeric input
        elif not key:  # If the video number is not entered
            self.updated_lbl.configure(text="Please enter a valid video number (01 to 08)")  # Display an error for missing video number
        else:  # If the video is not found
            self.updated_lbl.configure(text=f"Video {key} not found! Please enter a valid video number (01 to 08)")#Display an error for a non-existent video

        self.status_lbl.configure(text="Update video button clicked!")  # Update the status label

if __name__ == "__main__":
    window = tk.Tk()  # Create the main application window
    fonts.configure()  # Apply font configurations from the font_manager module
    UpdateVideos(window)  # Create an instance of UpdateVideos and pass the main window to it
    window.mainloop()  # Start the Tkinter main loop to run the application
