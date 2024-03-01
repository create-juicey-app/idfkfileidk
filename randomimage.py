import os
import random

def open_random_file():
    current_dir = os.getcwd()
    files = [file for file in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, file))]
    valid_extensions = ['.mp4', '.mp3', '.webp', '.jpg', '.jpeg', '.png', '.gif', '.mov', '.wav']
    valid_files = [file for file in files if os.path.splitext(file)[1].lower() in valid_extensions]

    if valid_files:
        random_file = random.choice(valid_files)
        file_path = os.path.join(current_dir, random_file)
        
        os.startfile(file_path)
        print(f"Opening random file: {random_file}")
    else:
        print("No valid files found.")

if __name__ == "__main__":
    open_random_file()
