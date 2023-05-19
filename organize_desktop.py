import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")  # Path to your desktop

def organize_desktop():
    for filename in os.listdir(desktop_path):
        if filename == "organize_desktop.py":  # Exclude this script from organization
            continue

        file_path = os.path.join(desktop_path, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            destination_folder = os.path.join(desktop_path, file_extension[1:])

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, filename)

            # Move the file to the destination folder
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_folder}")

    print("Desktop organization complete!")

if __name__ == "__main__":
    organize_desktop()
