import subprocess
from pathlib import Path


def bash(command, absolute_folder_path):
    """
    Execute a shell command in the specified directory and return its output.

    Args:
        command (str): Shell command to execute.
        absolute_folder_path (str): Absolute path to the working directory.

    Returns:
        str: Combined stdout and stderr output.

    Raises:
        FileNotFoundError: If the directory does not exist.
        RuntimeError: If the command execution fails.
    """
    working_dir = Path(absolute_folder_path)

    if not working_dir.exists():
        raise FileNotFoundError(f"Directory does not exist: {absolute_folder_path}")

    if not working_dir.is_dir():
        raise NotADirectoryError(f"Not a directory: {absolute_folder_path}")

    try:
        result = subprocess.run(
            command, cwd=str(working_dir), shell=True, capture_output=True, text=True
        )

        output = result.stdout
        if result.stderr:
            output += result.stderr

        return output.strip()

    except Exception as e:
        raise RuntimeError(f"Failed to execute command: {e}")
