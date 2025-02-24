# Write a program to print the contents of a directory using the os module.

import os

def list_directory_contents(directory_path):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(directory_path)
        print(f"Contents of the directory '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the directory path as a variable
directory_path = "/pyJourney"  # Replace with the actual directory path
list_directory_contents(directory_path)
