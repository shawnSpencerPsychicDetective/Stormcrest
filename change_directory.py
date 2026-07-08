from pathlib import PureWindowsPath


def change_directory(current_directory, child_directory=None):
    if child_directory is None:
        # Move one level up
        parent = PureWindowsPath(current_directory).parent
        parent_str = str(parent)
        # add trailing \ to match your examples
        return parent_str if parent_str.endswith("\\") else parent_str + "\\"

    # Move into child directory
    new_path = PureWindowsPath(current_directory) / child_directory
    new_path_str = str(new_path)
    return new_path_str if new_path_str.endswith("\\") else new_path_str + "\\"
