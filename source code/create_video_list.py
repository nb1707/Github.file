import tkinter as tk  # Import the Tkinter library for GUI creation
import video_library as lib  # Import custom video library module
import font_manager as fonts  # Import custom font manager module

def set_text(text_area, content):
    # Function to insert new content into a text widget
    text_area.insert(1.0, content)  # Insert content at the beginning (line 1, character 0)

def reset_function(text_area):
    # Function to clear all content from a text widget
    text_area.delete("1.0", tk.END)  # Delete all text from the start to the end

class CreateVideoList:
    def __init__(self, window):
        # Initialize the main window's properties like size, title, and background color
        window.geometry("550x350")  # Set the window size to 550x350 pixels
        window.title("Create Video List")  # Set the window title to "Create Video List"
        window.configure(bg="lightblue")  # Set the background color of the window to light blue
        self.video_list = []  # Initialize an empty list to store added videos
        # Create and position the label for video number input
        enter_lbl = tk.Label(window, text="Input Video Number", width=17, relief="solid", bg="red")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)  # Place the label in the first row, first column with padding
        # Create and position the entry widget for user input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Place the entry widget spanning three columns with padding
        # Create and position the "Add Video" button
        add_video_btn = tk.Button(window, text="Add Video", width=11, command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=1, padx=10, pady=10)  # Place the button in the first row, second column with padding
        # Create and position the "Reset Video" button
        reset_video_btn = tk.Button(window, text="Reset Video", width=11, command=self.reset_video_clicked)
        reset_video_btn.grid(row=1, column=1, padx=10, pady=10)  # Place the button in the second row, second column with padding
        # Create and position the "Play Playlist" button
        play_video_list_btn = tk.Button(window, text="Play Playlist", width=11, command=self.play_playlist_clicked)
        play_video_list_btn.grid(row=2,column=1,rowspan=3,padx=10,pady=10)#Place the button in the third row, second column spanning three rows 
        # Create and position a Text widget to display the playlist
        self.playlist_txt = tk.Text(window, width=50, height=9, borderwidth=2, relief="solid")
        self.playlist_txt.grid(row=1, column=0, padx=10, pady=10)  # Place the text widget in the second row, first column with padding
        # Create and position a label to show status messages in red text
        self.status_lbl = tk.Label(window, width=80, text="", font=("Helvetica", 10), fg="red", anchor="w", bg="lightblue")
        self.status_lbl.grid(row=5, column=0, columnspan=4, padx=10, pady=10)  # Span the label across all columns with padding
        # Create and position another label for additional status or error messages in red text
        self.updated_lbl = tk.Label(window, width=80, text="", font=("Helvetica", 10), fg="red", anchor="w", bg="lightblue")
        self.updated_lbl.grid(row=6, column=0, columnspan=4, padx=10, pady=10)  # Span the label across all columns with padding

    def reset_video_clicked(self):#Method called when "Reset Video" button is clicked to reset the playlist
        reset_function(self.playlist_txt)  # Clear the playlist text area
        self.status_lbl.configure(text="")  # Clear the status label
        self.updated_lbl.configure(text="")  # Clear the updated label
        self.video_list = []  # Clear the video list
        self.status_lbl.configure(text="Reset Video button was clicked!")  # Update the status label
    def add_video_clicked(self):#Method called when "Add Video" button is clicked to add a video to the playlist
        key = self.input_txt.get()  # Get the video number from the entry widget
        if key in self.video_list:  # Check if the video is already in the list
            self.updated_lbl.configure(text="Video is already added!")  # Show a message if the video is already added
        else:
            name = lib.get_name(key)  # Retrieve the video name using the video number
            if name is not None:  # If the video is found in the library
                detail_playlist = f"{name}\n"  # Format the video details
                current_video = self.playlist_txt.get("1.0", "end")  # Get the current playlist content
                if key not in current_video:  # Check if the video is not already listed
                    set_text(self.playlist_txt, detail_playlist)  # Add the video details to the playlist text area
                    self.video_list.append(key)  # Add the video number to the video list
                    self.updated_lbl.configure(text="Video added!") #Update the label to confirm the video was added
                else:
                    self.updated_lbl.configure(text="Video is already added!")#Show a message if the video is already in the playlist
            elif key == "":  # If no video number is entered
                self.updated_lbl.configure(text="A video number is required! Please enter a valid number (01 to 08).")
            else:  # If the video number is not found
                self.updated_lbl.configure(text=f"Video {key} not found! Please enter a valid number (01 to 08).")
        self.status_lbl.configure(text="Add Video button was clicked!")  # Update the status label
    def play_playlist_clicked(self):#Method called when "Play Playlist" button is clicked to play all videos in the playlist
        if not self.video_list:  # Check if the playlist is empty
            self.updated_lbl.configure(text="No videos in the playlist! Please add a video before playing.")
        else:
            for key in self.video_list:  # Loop through each video in the playlist
                lib.increment_play_count(key)  # Increment the play count for each video
            self.updated_lbl.configure(text="")  # Clear any previous messages
        self.status_lbl.configure(text="Play Playlist button was clicked!")  # Update the status label

if __name__ == "__main__":
    # Main entry point; initializes the Tkinter window and the CreateVideoList class
    window = tk.Tk()  # Create the main application window
    fonts.configure()  # Apply font configurations using the font manager
    CreateVideoList(window)  # Instantiate the CreateVideoList class, passing the window as an argument
    window.mainloop()  # Start the Tkinter event loop to keep the window open and responsive
