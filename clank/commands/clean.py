import os

def clean_bin_files():
    for file in os.listdir('.'):
        new_path = file + ".cpp"
        if os.path.isfile(new_path):
            os.remove(file)
            print(f"{file} removed")