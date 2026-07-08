from pathlib import Path

from .bash import bash
from .fetch import fetch
from .forge_prompt import forge_prompt
from .generate import generate
from .make_directory import make_directory
from .read import read
from .search import search
from .write import write


def use_tool(tool_name, arguments, state):
    if tool_name == "get_cwd":
        return state["cwd"]

    if tool_name == "list":
        lst = []
        for item in Path(f"{state['cwd']}").iterdir():
            lst.append(item.name)
        return lst

    if tool_name == "change_directory":
        if len(arguments) == 0:
            if state["cwd"] == "C:\\":
                return False
            return True
        if arguments[0] is None:
            if state["cwd"] == "C:\\":
                return False
            return True
        lst = []
        for item in Path(f"{state['cwd']}").iterdir():
            lst.append(item.name)
        if arguments[0] in lst:
            return True
        return False

    if tool_name == "make_directory":
        try:
            make_directory(state["cwd"], arguments[0])
            return "Success"
        except:
            return "Failure"

    if tool_name == "read":
        return read(state["cwd"], arguments[0])

    if tool_name == "write":
        try:
            write(state["cwd"], arguments[0], arguments[1])
            return "Success"
        except:
            return "Failure"

    if tool_name == "bash":
        return bash(arguments[0], state["cwd"])

    if tool_name == "web_search":
        result = search(arguments[0])

        to_return = ""

        for url in result:
            to_return += url
            to_return += "\n"

        return to_return

    if tool_name == "fetch_url":
        return fetch(arguments[0])
