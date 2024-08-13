import tkinter as tk  # Import the Tkinter library for creating GUI elements
import tkinter.scrolledtext as tkst  # Import ScrolledText widget for scrollable text areas
import video_library as lib  # Import custom video library module
import font_manager as fonts  # Import custom font manager module
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL for handling images in Tkinter

def set_text(text_area, content):
    # Function to clear existing text in a text widget and insert new content
    text_area.delete("1.0", tk.END)  # Delete all text from the start to the end
    text_area.insert("1.0", content)  # Insert new content at the start

class CheckVideos:
    def __init__(self, window):#Initialize the main window's properties like size, title, and background color
        window.geometry("600x380")  # Set the window size to 600x380 pixels
        window.title("Check Videos")  # Set the window title to "Check Videos"
        window.configure(bg="lightblue")  # Set the background color of the window to light blue
        # Create and position the "List All Videos" button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Place the button in the first row, first column with padding
        # Create and position the label asking the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number", width=17, relief="solid", bg="red")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Place the label in the first row, second column with padding
        # Create and position the entry widget for user input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Place the entry widget in the first row, third column with padding
        # Create and position the "Check Video" button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Place the button in the first row, fourth column with padding
        # Create and position a ScrolledText widget for listing all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", relief="solid")
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="W", padx=10, pady=10)#Span across multiple columns and rows with padding
        # Create and position a Text widget to display the selected video’s details
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none", relief="solid")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)#Place the text widget in the second row, fourth column with padding
        # Create and position a label to show status messages in red text
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="red", bg="lightblue")
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Span the label across all columns with padding
        # Create and position another label for additional status or error messages in red text
        self.updated_lbl = tk.Label(window, text="", font=("Helvetica", 10), fg="red", bg="lightblue")
        self.updated_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Span the label across all columns with padding
        # Dictionary mapping video numbers to their corresponding image file paths
        self.picture_library = {"01":"picture/tomandjerry.jpg","02":"picture/breakfastattiffany's.jpg",
            "03":"picture/Casablanca.jpg","04":"picture/thesoundofmusic.jpg","05":"picture/gonewiththewind.jpg",
            "06":"picture/richierich.jpg","07":"picture/homealone.jpg","08":"picture/mrbeansholiday.jpg"}
        # Create and position a label to display the video image
        self.picture_lbl = tk.Label(window, bg="lightblue")
        self.picture_lbl.grid(row=2, column=3, rowspan=2, padx=10, pady=10)#Place the label in the third column spanning multiple rows with padding

    def check_video_clicked(self):
        # Method called when "Check Video" button is clicked to retrieve and display video details
        key = self.input_txt.get()  # Get the video number from the entry widget
        name = lib.get_name(key)  # Retrieve the video name using the video number

        if name is not None:  # If the video is found in the library
            director = lib.get_director(key)  # Get the director's name
            rating = lib.get_rating(key)  # Get the video rating
            play_count = lib.get_play_count(key)  # Get the video play count
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # Format the video details
            set_text(self.video_txt, video_details)  # Display the video details in the text widget
            self.create_image(key)  # Display the corresponding video image
            self.updated_lbl.configure(text="")  # Clear any previous status messages
        elif key == "":  # If no video number is entered
            self.updated_lbl.configure(text="A video number is required! Please enter a valid video number (from 01 to 08).")
            self.create_image(key)  # Clear the image display
        else:  # If the video number is not found
            self.updated_lbl.configure(text=f"Video {key} not found! Please enter a valid video number (from 01 to 08).")
            self.create_image(key)  # Clear the image display

        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status label

    def list_videos_clicked(self):
        # Method called when "List All Videos" button is clicked to display all videos
        video_list = lib.list_all()  # Get the list of all videos from the library
        set_text(self.list_txt, video_list)  # Display the video list in the ScrolledText widget
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label

    def create_image(self, key):
        # Method to retrieve and display the image corresponding to the given video number
        picture_key = self.picture_library.get(key)  # Get the image file path from the dictionary
        if picture_key:  # If the image exists
            picture = Image.open(picture_key)  # Open the image file
            picture = picture.resize((170, 200))  # Resize the image to fit the label
            tk_picture = ImageTk.PhotoImage(picture)  # Convert the image to a format usable in Tkinter
            self.picture_lbl.configure(image=tk_picture)  # Set the image in the label
            self.picture_lbl.picture = tk_picture  # Store a reference to the image to prevent garbage collection
        else:  # If no image is found for the video number
            self.picture_lbl.configure(image="")  # Clear the image display

if __name__ == "__main__":
    # Main entry point; initializes the Tkinter window and the CheckVideos class
    window = tk.Tk()  # Create the main application window
    fonts.configure()  # Apply font configurations using the font manager
    CheckVideos(window)  # Instantiate the CheckVideos class, passing the window as an argument
    window.mainloop()  # Start the Tkinter event loop to keep the window open and responsive
