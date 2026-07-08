from pathlib import Path

from .chat import chat


def main():
    chat(str(Path.cwd()))


if __name__ == "__main__":
    main()
