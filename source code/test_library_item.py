from library_item import LibraryItem  # Importing the LibraryItem class from the library_item module

def test_default_rating(): #Tests the default attributes of the LibraryItem class. 
    #Verifies that a new LibraryItem instance has the expected default values for rating and play_count.
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 0)  # Create a LibraryItem instance with default rating
    assert item.name == "Tom and Jerry"  # Check if the name attribute is set correctly
    assert item.director == "Fred Quimby"  # Check if the director attribute is set correctly
    assert item.rating == 0  # Check if the rating attribute is set to the default value
    assert item.play_count == 0  # Check if the play_count attribute is initialized to 0
def test_video_details(): #Tests the attribute assignment of the LibraryItem class.
    #Ensures that the LibraryItem instance's attributes are set correctly based on the constructor parameters.
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)  # Create a LibraryItem instance with a specific rating
    assert item.name == "Tom and Jerry"  # Check if the name attribute matches the input
    assert item.director == "Fred Quimby"  # Check if the director attribute matches the input
    assert item.rating == 4  # Check if the rating attribute is set correctly
    assert item.play_count == 0  # Ensure the play_count attribute is initialized to 0
def test_info(): #Tests the info method of the LibraryItem class.
    #Verifies that the info method returns the correctly formatted string with the item's details.
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)  # Create a LibraryItem instance with a specific rating
    assert item.info() == "Tom and Jerry - Fred Quimby ****"  # Check if the formatted string matches the expected output
def test_stars(): #Tests the stars method of the LibraryItem class.
    #Validates that the stars method returns a string of asterisks representing the item's rating.
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)  # Create a LibraryItem instance with a specific rating
    assert item.stars() == "****"  # Check if the stars method returns the correct number of asterisks based on the rating
def test_play_count(): #Tests the increment functionality of the play_count attribute in the LibraryItem class.
    #Ensures that the play_count attribute increments as expected.
    item = LibraryItem("Tom and Jerry", "Fred Quimby", 4)  # Create a LibraryItem instance with a specific rating
    item.play_count += 1  # Increment the play_count attribute
    assert item.play_count == 1  # Check if the play_count attribute has been updated correctly
