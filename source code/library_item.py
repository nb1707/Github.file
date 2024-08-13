class LibraryItem:
    def __init__(self, name, director, rating=0):
        # Initialize a LibraryItem object with a name, director, rating, and play count
        self.name = name  # The name of the video or library item
        self.director = director  # The director of the video or library item
        self.rating = rating  # The rating of the item, default is 0 if not provided
        self.play_count = 0  # Initialize the play count to 0

    def info(self):
        # Return a formatted string with the name, director, and rating in stars
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        # Generate a string of stars corresponding to the rating
        stars = ""  # Initialize an empty string to store stars
        for i in range(self.rating):  # Loop through the number of stars equal to the rating
            stars += "*"  # Append a star for each iteration
        return stars  # Return the final string of stars
