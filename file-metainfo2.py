import os
import shlex

# Function to get a normalized file path
def get_normalized_path():
    input_path = input("Enter the file path: ")
    
    # Remove backslashes from the input path
    input_path = input_path.replace('\\', '')
    
    # Normalize the input path
    normalized_path = os.path.normpath(input_path)
    
    return normalized_path

# Main function
def main():
    normalized_file_path = get_normalized_path()

    if os.path.isfile(normalized_file_path):
        metadata = get_file_metadata(normalized_file_path)
        display_metadata(metadata)
    else:
        print("\nError: The specified file does not exist.")

if __name__ == "__main__":
    main()
