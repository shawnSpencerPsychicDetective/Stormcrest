import os


def make_directory(path, dir_name):
    # The path argument is the absolute path of the directory where the new directory has to be made
    # The dir_name argument is the name of the new directory created inside the directory pointed to by path

    full_path = os.path.join(path, dir_name)

    # makedirs creates intermediate folders if needed, and exist_ok=True avoids an error if it already exists
    os.makedirs(full_path, exist_ok=True)

    return full_path
