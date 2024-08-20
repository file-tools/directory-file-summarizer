import os
import datetime

# Function to get file metadata
def get_file_metadata(file_path):
    try:
        # Get file size
        file_size = os.path.getsize(file_path)
        
        # Get file type
        file_type = os.path.splitext(file_path)[-1].strip('.').upper()
        
        # Get file creation time
        creation_time = os.path.getctime(file_path)
        creation_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Get file modification time
        modification_time = os.path.getmtime(file_path)
        modification_time = datetime.datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

        return {
            "Filename": os.path.basename(file_path),
            "File Size (bytes)": file_size,
            "File Type": file_type,
            "Creation Date": creation_time,
            "Modification Date": modification_time
        }
    except Exception as e:
        return None

# Function to display metadata in a table
def display_metadata(metadata):
    if metadata is not None:
        print("\nFile Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("\nError: Unable to retrieve file metadata.")

# Main function
def main():
    file_path = input(r"Enter the file path: ")  # Use a raw string (r"") here

    # Check if the file exists
    if os.path.isfile(file_path):
        metadata = get_file_metadata(file_path)
        display_metadata(metadata)
    else:
        print("\nError: The specified file does not exist.")

if __name__ == "__main__":
    main()
