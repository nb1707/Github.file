from library_item import LibraryItem  # Import the LibraryItem class from the library_item module

# Create a dictionary to store the library items
library = {
    "01": LibraryItem("Tom and Jerry", "Fred Quimby", 4),
    "02": LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5),
    "03": LibraryItem("Casablanca", "Michael Curtiz", 2),
    "04": LibraryItem("The Sound of Music", "Robert Wise", 1),
    "05": LibraryItem("Gone with the Wind", "Victor Fleming", 3),
    "06": LibraryItem("Richie Rich", "Donald Petrie", 4),
    "07": LibraryItem("Home Alone", "Chris Columbus", 4),
    "08": LibraryItem("Mr. Bean's Holiday", "Steve Bendelack", 5)
}

# Function to list all items in the library
def list_all():
    output = ""  # Initialize an empty string to accumulate the output
    for key in library:  # Iterate over each key in the library dictionary
        item = library[key]  # Retrieve the LibraryItem object associated with the key
        output += f"{key} {item.info()}\n"  # Append the key and item information to the output string
    return output  # Return the complete output string

# Function to get the name of a video based on its key
def get_name(key):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        return item.name  # Return the name of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        return None  # Return None if the key is not found

# Function to get the director of a video based on its key
def get_director(key):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        return item.director  # Return the director of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        return None  # Return None if the key is not found

# Function to get the rating of a video based on its key
def get_rating(key):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        return item.rating  # Return the rating of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        return -1  # Return -1 if the key is not found

# Function to set the rating of a video based on its key
def set_rating(key, rating):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        item.rating = rating  # Update the rating of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        pass  # Do nothing if the key is not found

# Function to get the play count of a video based on its key
def get_play_count(key):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        return item.play_count  # Return the play count of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        return -1  # Return -1 if the key is not found

# Function to increment the play count of a video based on its key
def increment_play_count(key):
    try:
        item = library[key]  # Try to retrieve the LibraryItem object using the key
        item.play_count += 1  # Increment the play count of the item if found
    except KeyError:  # Handle the case where the key is not found in the library
        pass  # Do nothing if the key is not found
