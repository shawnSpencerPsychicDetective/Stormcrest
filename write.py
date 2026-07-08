import os


def write(absolute_folder_path, filename, filecontent):
    """
    Writes filecontent to a text file in the specified folder.

    Parameters:
        absolute_folder_path (str): Absolute path to the target folder.
        filename (str): Filename with or without .txt extension.
        filecontent (str): Content to write into the file.

    Returns:
        str: Absolute path of the written file.
    """

    if not os.path.isabs(absolute_folder_path):
        raise ValueError("absolute_folder_path must be an absolute path.")

    # Ensure .txt extension
    if not filename.lower().endswith(".txt"):
        filename += ".txt"

    # Create full file path
    file_path = os.path.join(absolute_folder_path, filename)

    # Overwrite if file already exists
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(filecontent))

    return file_path
