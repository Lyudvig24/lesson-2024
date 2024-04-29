import os
import shutil


# List of files to exclude from sorting
excludeFiles = ['lessons.py','filter_file.txt','weather.py','randomwords.txt','types_file.py','crypto_stats.py','hangman_game.py','word_frequency_counter.py']

# Function to extract and return the file extension from a file name
def get_file_extension(file_name):
    # Check if the file name is empty or None
    if not file_name:
        return None  # Return None if the file name is empty or None
    # Split the file name by '.' to get the file extension
    # Use [-1] to access the last element of the resulting list, which is the file extension
    # Convert the file extension to lowercase to ensure consistency
    return file_name.split('.')[-1].lower()  # Return the lowercased file extension

# Function to sort files into directories based on their types
def file_types():

    # Dictionary to store file types and their corresponding file names
    data = {}

    # Loop through each file in the current directory
    for fileName in os.listdir('.'):

        # Check if the file is a regular file and not in the exclude list
        if os.path.isfile(fileName) and fileName not in excludeFiles:

             # Get the file extension
            type = get_file_extension(fileName)

            # Add the file to the corresponding file type in the data dictionary
            data.setdefault(type,[])
            data[type].append(fileName)
                
    # Loop through each file type in the data dictionary
    for type in data:

        # Get the list of files for the current file type
        files = data[type]

        # Create a directory for the file type if it doesn't exist
        if os.path.isdir(type) == False:
            os.makedirs(type)

        # Move each file to its corresponding directory
        for newFileName in files:
            shutil.move(newFileName, type + '/' + newFileName)
    # Return the sorted data dictionary
    return data
        
# Call the file_types function to sort files and print the result
print(file_types())
