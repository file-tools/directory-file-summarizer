import os

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
                folder_info[folder_name] = (file_count, dir_count)

    return folder_info

def write_to_file(folder_info, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for folder_name, (file_count, dir_count) in sorted(folder_info.items()):
            if dir_count > 0:
                f.write(f"{folder_name} ({dir_count} folders, {file_count} files)\n")
            else:
                f.write(f"{folder_name} ({file_count} files)\n")

if __name__ == "__main__":
    folder_path = "/Users/Reess/Desktop/TestFoldertoScan/"
    output_file = "/Users/Reess/Desktop/TestFoldertoScan/folder_info.txt"

    folder_info = count_files(folder_path)
    write_to_file(folder_info, output_file)

    print("Folder information written to", output_file)

