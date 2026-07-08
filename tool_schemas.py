from typing import TypedDict


class Tool(TypedDict):
    name: str
    description: str
    arguments: list
    returns: str


class Argument(TypedDict):
    arg: str
    datatype: str
    description: str


def define_tool(name, description, arguments, returns):
    return Tool(
        {
            "name": name,
            "description": description,
            "arguments": arguments,
            "returns": returns,
        }
    )


def define_argument(arg, datatype, description):
    return f"{arg} (Datatype: {datatype}, {description})"


ender = define_tool(
    "exit",
    "ends the conversation, can be invoked by a goodbye, cya later, exit, or any other such terminal responses",
    "this tool has no argument",
    "No result, this ends the conversation",
)

get_cwd = define_tool(
    "get_cwd",
    "returns the current working directory",
    "this tool has no argument",
    "current working directory",
)

lst = define_tool(
    "list",
    '''returns all the files and folders in the current working directory, can be activated by "list"''',
    "this tool has no argument",
    "list of all files and folders in the current working directory",
)

cd = define_tool(
    "change_directory",
    """Changes the current working directory""",
    "Directory name (if argument is None it moves to parent directory)",
    "Success or Failure",
)
mkdir = define_tool(
    "make_directory",
    "Creates a new directory within the current working directory",
    "Directory name",
    "Success or Failure",
)

reader = define_tool(
    "read",
    "reads a pdf, word, markdown, text, or odt file that exists within the Current Working Directory.",
    "file name",
    "File Content",
)

writer = define_tool(
    "write",
    "writes a text file within the Current Working Directory (note: if filename already exists, then it will overwrite that file).",
    "file name, file content",
    "Success or Failure",
)

bash = define_tool(
    "bash",
    "run a WINDOWS shell command within the current working directory",
    "windows shell command",
    "shell command output",
)

search = define_tool(
    "web_search", "find top 5 URLs based on a search query", "search query", "URLs"
)

fetch = define_tool(
    "fetch_url",
    "Provides the content of a specific url page",
    "URL",
    "URL page content",
)

tools = [get_cwd, ender, lst, cd, mkdir, reader, writer, bash, search, fetch]


def tool_arguments(Tool):
    args = "Arguments: "
    for argument in Tool["arguments"]:
        args += f"{argument}, "
    args += "\n"
    return args


def tool_schemas():
    stuff = ""
    for tool in tools:
        stuff += f"Tool Name: {tool['name']}\n"
        stuff += f"Description: {tool['description']}\n"
        stuff += tool_arguments(tool)
        stuff += f"Tool returns: {tool['returns']}\n"
        stuff += "*" * 10 + "\n"
    return stuff
