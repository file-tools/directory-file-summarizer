import os

# Try to import configuration from config.py
try:
    from config.config import folder_path, output_file, indentation, space_d0, space_d1, space_d2, space_d3
except ImportError:
    print("Configuration not found. Make sure you have a valid config.py.")
    exit(1)

def count_files(folder_path):
    folder_info = {}  # Dictionary to store folder names and file counts

    for root, dirs, files in os.walk(folder_path):
        if root == folder_path:
            level = 0
        else:
            level = root[len(folder_path) + len(os.path.sep):].count(os.path.sep)

        if level <= 6:
            folder_name = os.path.basename(root)

            # Skip processing if folder_name is empty
            if folder_name:
                file_count = len(files)
                dir_count = len(dirs)
                folder_info[root] = (file_count, dir_count, level)

    return folder_info

def write_to_file(folder_info, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        prev_level = -1  # To track the previous level

        for folder, (file_count, dir_count, level) in sorted(folder_info.items()):
            indentation_string = indentation * level

            # Add separators based on the level difference and if they are defined
            separators = [space_d0, space_d1, space_d2, space_d3]  # Add more separator variables as needed
            separator = separators[level] if level < len(separators) and separators[level] is not None else ""
            if separator:
                f.write(f"{separator}\n")

            if dir_count > 0:
                folder_line = f"{indentation_string}{os.path.basename(folder)} ({dir_count} folders, {file_count} files)"
            else:
                folder_line = f"{indentation_string}{os.path.basename(folder)} ({file_count} files)"

            f.write(f"{folder_line}\n")

if __name__ == "__main__":
    folder_info = count_files(folder_path)
    write_to_file(folder_info, output_file)

    print("Folder hierarchy written to", output_file)
