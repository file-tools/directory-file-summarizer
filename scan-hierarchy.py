import os
from config import folder_path, output_file, indentation

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
        for folder, (file_count, dir_count, level) in sorted(folder_info.items()):
            indentation_string = indentation * level
            
            if dir_count > 0:
                folder_line = f"{indentation_string}{os.path.basename(folder)} ({dir_count} folders, {file_count} files)"
            else:
                folder_line = f"{indentation_string}{os.path.basename(folder)} ({file_count} files)"
            
            f.write(f"{folder_line}\n")

if __name__ == "__main__":
    folder_info = count_files(folder_path)
    write_to_file(folder_info, output_file)

    print("Folder hierarchy written to", output_file)
