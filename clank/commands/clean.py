import os

def clean_bin_files_init_parser(parser):
    subparser = parser.add_parser("clean", help="Clean binary files")

def clean_bin_files():
    for file in os.listdir('.'):
        new_path = file + ".cpp"
        if os.path.isfile(new_path):
            os.remove(file)
            print(f"{file} removed")