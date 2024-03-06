#1
import os
def list_directories_and_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)
def list_all_directories_and_files(path):
    for root, directories, files in os.walk(path):
        print(f"\nRoot Directory: {root}")
        print("Directories:")
        for directory in directories:
            print(os.path.join(root, directory))
        print("\nFiles:")
        for file in files:
            print(os.path.join(root, file))
# Specify the path
path = '/path/to/your/directory'
# List directories and files
print("List of Directories and Files:")
list_directories_and_files(path)
# List all directories and files
print("\nList of All Directories and Files:")
list_all_directories_and_files(path)

#2
import os
def check_path_access(path):
    # Check existence
    if os.path.exists(path):
        print(f"{path} exists.")
        # Check readability
        if os.access(path, os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")
        # Check writability
        if os.access(path, os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")
        # Check executability (for directories or files with execute permission)
        if os.access(path, os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")
# Specify the path
path = '/path/to/your/file_or_directory'
# Check path access
check_path_access(path)

#3
import os
def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        # Extract filename and directory portions
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")
# Specify the path
path = '/path/to/your/file_or_directory'
# Test the path
test_path(path)

#4
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return -1
# Specify the path to the text file
file_path = '/path/to/your/text_file.txt'
# Count the lines in the text file
line_count = count_lines(file_path)
if line_count != -1:
    print(f"Number of lines in '{file_path}': {line_count}")

#5
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List written to file successfully.")
    except IOError:
        print("Error writing to file.")

# Specify the path to the file
file_path = '/path/to/your/output_file.txt'
# List to write to file
data_list = ["apple", "banana", "orange", "grape"]
# Write list to file
write_list_to_file(file_path, data_list)

#6
import string
def generate_text_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        file_name = letter + '.txt'
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}.")
generate_text_files()

#7
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except IOError:
        print("Error copying file.")
# Specify the paths to the source and destination files
source_file = '/path/to/your/source_file.txt'
destination_file = '/path/to/your/destination_file.txt'
# Copy the contents of the source file to the destination file
copy_file(source_file, destination_file)

#8
import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.R_OK | os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"You don't have permission to delete '{file_path}'.")
    else:
        print(f"The file '{file_path}' does not exist.")
# Specify the path to the file to be deleted
file_path = '/path/to/your/file_to_delete.txt'
# Delete the file
delete_file(file_path)
