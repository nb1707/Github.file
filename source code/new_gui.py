import tkinter as tk  # Importing tkinter for creating GUI components
import tkinter.scrolledtext as tkst  # Importing scrolledtext to create a scrollable text area
import video_library as lib  # Importing the video_library module for managing video data
import font_manager as fonts  # Importing font_manager to apply custom fonts
from PIL import Image, ImageTk  # Importing PIL for image handling
import random  # Importing random for selecting a random video

def set_text(text_area, content):
    """
    Clears the content of the text_area and sets new content.
    Args: text_area (tk.Text): The text area widget to update.
    content (str): The content to display in the text area.
    """
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

def add_text(text_area, content):
    """
    Adds content to the end of the text_area.
    
    Args:
    text_area (tk.Text): The text area widget to update.
    content (str): The content to add to the text area.
    """
    text_area.insert(tk.END, content)

def reset_text(text_area):
    """
    Clears the content of the text_area.
    Args: text_area (tk.Text): The text area widget to clear.
    """
    text_area.delete("1.0", tk.END)

class new_gui:
    def __init__(self, window):
        """
        Initializes the GUI components and layout.
        Args: window (tk.Tk): The main window of the application.
        """
        window.geometry("1920x1080")  # Set the size of the window
        window.title("New GUI")  # Set the title of the window
        self.video_list = []  # List to keep track of videos added to the playlist
        window.configure(background="light blue")  # Set the background color of the window

        # Create and place widgets for video number input
        enter_video_lbl = tk.Label(window, text="Enter Video No.", width=15, anchor="w", bg="red", relief="solid")
        enter_video_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.input_number_txt = tk.Entry(window, width=5)
        self.input_number_txt.grid(row=0, column=1, padx=10, pady=10)

        # Create and place widgets for video rating input
        enter_new_rating_lbl = tk.Label(window, text="Enter New Rating", width=15, anchor="w", bg="red", relief="solid")
        enter_new_rating_lbl.grid(row=0, column=2, padx=10, pady=10)
        self.input_rating_txt = tk.Entry(window, width=5)
        self.input_rating_txt.grid(row=0, column=3, padx=10, pady=10)

        # Create and place text areas for displaying video list, playlist, and video details
        self.video_list_txt = tkst.ScrolledText(window, height=17, width=20, borderwidth=2, relief="solid")
        self.video_list_txt.grid(row=1, column=1, rowspan=7, padx=10, pady=10)
        self.play_list_txt = tk.Text(window, height=10, width=40, borderwidth=2, relief="solid")
        self.play_list_txt.grid(row=2, column=2, columnspan=2, rowspan=4, padx=10, pady=10)
        self.check_video_txt = tk.Text(window, height=5, width=40, borderwidth=2, relief="solid")
        self.check_video_txt.grid(row=6, column=2, columnspan=2, rowspan=2, padx=10, pady=10)

        # Create and place buttons for various actions
        update_video_button = tk.Button(window, text="Update Video", width=12, command=self.update_video_clicked)
        update_video_button.grid(row=2, column=0, padx=10, pady=10)
        check_video_button = tk.Button(window, text="Check Video", width=12, command=self.check_video_clicked)
        check_video_button.grid(row=3, column=0, padx=10, pady=10)
        play_video_button = tk.Button(window, text="Play Video", width=12, command=self.play_video_clicked)
        play_video_button.grid(row=4, column=0, padx=10, pady=10)
        add_video_button = tk.Button(window, text="Add Video", width=12, command=self.add_video_clicked)
        add_video_button.grid(row=5, column=0, padx=10, pady=10)
        reset_video_button = tk.Button(window, text="Reset Video", width=12, command=self.reset_video_clicked)
        reset_video_button.grid(row=6, column=0, padx=10, pady=10)
        random_video_button = tk.Button(window, text="Random Video", width=12, command=self.random_video_clicked)
        random_video_button.grid(row=7, column=0, padx=10, pady=10)

        # Create and place status labels for displaying messages
        self.status_label = tk.Label(window, text="", width=80, font=("Helvetica", 12), fg="red", anchor="w", bg="light blue")
        self.status_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
        self.updated_status_label = tk.Label(window, text="", width=80, font=("Helvetica", 12), fg="red", anchor="w", bg="light blue")
        self.updated_status_label.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

        # Dictionary to map video numbers to image file paths
        self.picture_library = {
            "01": "picture/tomandjerry.jpg",
            "02": "picture/breakfastattiffany's.jpg",
            "03": "picture/Casablanca.jpg",
            "04": "picture/thesoundofmusic.jpg",
            "05": "picture/gonewiththewind.jpg",
            "06": "picture/richierich.jpg",
            "07": "picture/homealone.jpg",
            "08": "picture/mrbeansholiday.jpg"
        }

        # Create and place a label for displaying video images
        self.picture_lbl = tk.Label(window, bg="light blue")
        self.picture_lbl.grid(row=1, column=7, rowspan=7, columnspan=7, padx=10, pady=10)

    def update_video_clicked(self):
        """
        Handles the click event for the 'Update Video' button.
        Updates the rating of a video based on the user input.
        """
        key = self.input_number_txt.get()  # Get video number from input
        new_rating_1 = self.input_rating_txt.get()  # Get new rating from input
        name = lib.get_name(key)  # Get the video name using the video number
        if name is not None:
            if new_rating_1.isdigit():
                new_rating = int(new_rating_1)
                if 0 <= new_rating <= 5:
                    lib.set_rating(key, new_rating)  # Update the video rating in the library
                    update_rating = lib.get_rating(key)  # Get the updated rating
                    self.updated_status_label.configure(text=f'"{name}" already updated rating to {update_rating}')
                    video_list = lib.list_all()  # Get the updated list of videos
                    set_text(self.video_list_txt, video_list)  # Display the updated video list
                else:
                    self.updated_status_label.configure(text="Invalid rating! Please enter a valid rating (0 to 5)")
            else:
                self.updated_status_label.configure(text="Invalid rating! Please enter a valid rating (0 to 5)")
        elif key == "":
            self.updated_status_label.configure(text="Require a video number! Please enter a valid video number (01 to 08) in the box above")
        else:
            self.updated_status_label.configure(text=f'Video {key} not found! Please enter a valid video number (01 to 08) in the box above')
        self.status_label.configure(text="Update Video button was clicked!")

    def check_video_clicked(self):
        """
        Handles the click event for the 'Check Video' button.
        Displays the details of a video based on the user input.
        """
        key = self.input_number_txt.get()  # Get video number from input
        name = lib.get_name(key)  # Get the video name using the video number
        if name is not None:
            director = lib.get_director(key)  # Get the director of the video
            rating = lib.get_rating(key)  # Get the rating of the video
            play_count = lib.get_play_count(key)  # Get the play count of the video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.check_video_txt, video_details)  # Display the video details
            self.create_image(key)  # Display the video image
        elif key == "":
            self.updated_status_label.configure(text="Require a video number! Please enter a valid video number (from 01 to 08) in the box")
            self.create_image(key)
        else:
            self.updated_status_label.configure(text=f'Video {key} not found! Please enter a valid video number (from 01 to 08) in the box')
            self.create_image(key)
        self.status_label.configure(text="Check Video button was clicked!")

    def play_video_clicked(self):
        """
        Handles the click event for the 'Play Video' button.
        Increments the play count of all videos in the playlist.
        """
        if not self.video_list:
            self.updated_status_label.configure(text="There is no video in the playlist! Please add a video before running the playlist")
        for key in self.video_list:
            lib.increment_play_count(key)  # Increment the play count of the video
            self.updated_status_label.configure(text="")
        self.status_label.configure(text="Play Video button was clicked!")

    def reset_video_clicked(self):
        """
        Handles the click event for the 'Reset Video' button.
        Clears all text areas, status labels, and resets the playlist.
        """
        reset_text(self.play_list_txt)  # Clear the playlist text area
        reset_text(self.video_list_txt)  # Clear the video list text area
        reset_text(self.check_video_txt)  # Clear the video details text area
        self.status_label.configure(text="")  # Clear the status label
        self.updated_status_label.configure(text="")  # Clear the updated status label
        self.picture_lbl.configure(image="")  # Clear the displayed image
        self.video_list = []  # Reset the video list
        self.status_label.configure(text="Reset Video button was clicked!")

    def add_video_clicked(self):
        """
        Handles the click event for the 'Add Video' button.
        Adds a video to the playlist based on the user input.
        """
        key = self.input_number_txt.get()  # Get video number from input
        if key in self.video_list:
            self.updated_status_label.configure(text="Video is already added!")
        else:
            name = lib.get_name(key)  # Get the video name using the video number
            if name is not None:
                detail_playlist = f"{name}\n"
                current_video = self.play_list_txt.get("1.0", "end")
                if key not in current_video:
                    add_text(self.play_list_txt, detail_playlist)  # Add video details to the playlist
                    self.video_list.append(key)  # Add the video key to the video list
                    self.updated_status_label.configure(text="Video added!")
                    self.create_image(key)  # Display the video image
                else:
                    self.updated_status_label.configure(text="Video is already added!")
            elif key == "":
                self.updated_status_label.configure(text="Require a video number! Please enter a valid video number (01 to 08) in the box above")
                self.create_image(key)
            else:
                self.updated_status_label.configure(text=f'Video {key} not found! Please enter a valid video number (01 to 08) in the box above')
                self.create_image(key)
        self.status_label.configure(text="Add Video button was clicked!")

    def random_video_clicked(self):
        """
        Handles the click event for the 'Random Video' button.
        Adds a random video to the playlist and displays its details.
        """
        all_keys = list(lib.library.keys())  # Get all video keys from the library
        if all_keys:
            random_key = random.choice(all_keys)  # Select a random video key
            self.add_video_clicked_for_key(random_key)  # Add the random video to the playlist
            
            # Display video information in check_video_txt
            name = lib.get_name(random_key)
            director = lib.get_director(random_key)
            rating = lib.get_rating(random_key)
            play_count = lib.get_play_count(random_key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.check_video_txt, video_details)  # Display the video details
            
            # Display video image
            self.create_image(random_key)  # Display the video image
            
            # Update status labels
            self.status_label.configure(text="Random Video button was clicked!")
            self.updated_status_label.configure(text="Random video added and details shown!")
        else:
            self.updated_status_label.configure(text="No videos available in the library.")

    def add_video_clicked_for_key(self, key):
        """
        Helper function to add a video to the playlist based on the provided key.
        
        Args:
        key (str): The video key to add.
        """
        if key in self.video_list:
            self.updated_status_label.configure(text="Video is already added!")
        else:
            name = lib.get_name(key)  # Get the video name using the video number
            if name is not None:
                detail_playlist = f"{name}\n"
                current_video = self.play_list_txt.get("1.0", "end")
                if key not in current_video:
                    add_text(self.play_list_txt, detail_playlist)  # Add video details to the playlist
                    self.video_list.append(key)  # Add the video key to the video list
                    self.updated_status_label.configure(text="Video added!")
                    self.create_image(key)  # Display the video image
                else:
                    self.updated_status_label.configure(text="Video is already added!")
            elif key == "":
                self.updated_status_label.configure(text="Require a video number! Please enter a valid video number (01 to 08) in the box above")
                self.create_image(key)
            else:
                self.updated_status_label.configure(text=f'Video {key} not found! Please enter a valid video number (01 to 08) in the box above')
                self.create_image(key)
        self.status_label.configure(text="Random Video button was clicked!")

    def create_image(self, key):
        """
        Displays the image associated with the given video key.
        
        Args:
        key (str): The video key for which to display the image.
        """
        picture_key = self.picture_library.get(key)  # Get the image file path for the video key
        if picture_key:
            picture = Image.open(picture_key)  # Open the image file
            picture = picture.resize((250, 290))  # Resize the image
            tk_picture = ImageTk.PhotoImage(picture)  # Convert the image to a format suitable for Tkinter
            self.picture_lbl.configure(image=tk_picture)  # Update the label to display the image
            self.picture_lbl.picture = tk_picture  # Keep a reference to the image to avoid garbage collection
        else:
            self.picture_lbl.configure(image="")  # Clear the image display if no picture is found

if __name__ == "__main__":
    window = tk.Tk()  # Create the main window
    fonts.configure()  # Apply custom fonts
    new_gui(window)  # Initialize and run the GUI
    window.mainloop()  # Start the Tkinter event loop
