import re
import subprocess
import sys
import tempfile
  

# Constants for parsing output of CLI command `terra folder tree`.
FIRST_PARENT_REGEX = r"^\├\─\─\s(.+)$"
LAST_PARENT_REGEX = r"^\└\─\─(.+)$"
LEAF_REGEX = r"^\│(\s+)\├\─\─(.+)$"
LAST_LEAF_REGEX = r"^\│(\s+)\└\─\─(.+)$"
DANGLING_LINE_REGEX = r"^(\s+)\└\─\─(.+)$"
TOP_LEVEL_CLEAN_LINE_TO_YAML_REGEX = r"^(.*)\s\((.*)\)$|^[\s*](.*)\s\((.*)\)\s*$"
CLEAN_LINE_TO_YAML_REGEX = r"^(\s+)(.*)\s\((.*)\)\s*$"

def parse_tree(cli_output : str = None):
    """
    Returns a representation of the workspace folder tree in the form of a list of dictionaries.
    """
    # 0) Create temp files for reading/writing text representation of folder tree.
    sys.stdout.flush()
    cli_output_tree = tempfile.NamedTemporaryFile(mode = 'w+', delete=False)
    parsed_tree = tempfile.NamedTemporaryFile(mode = 'w+', delete=False)

    # 1) Get workspace folder tree, if not provided.
    if cli_output is None:
        cli_folder_tree_output = subprocess.run(
            ["terra", "folder", "tree"], capture_output=True, text=True
        )
        cli_output = cli_folder_tree_output.stdout

    # 2) Write workspace folder tree to temp file.
    with open(cli_output_tree.name, "w+") as cli_tree:
        cli_tree.write(cli_output)
        # Rewind to start of file for reading.
        cli_tree.seek(0)
        # Define variables for setting up list of dictionaries as tree.
        indentation = []
        indentation.append(0)
        depth = 0
        root = {"folder": "root", "id": "0", "depth": 0, "children": []}
        parents = []
        node = root
        # 3) Parse file, replacing symbols with tabs.
        with open(parsed_tree.name, "w+") as output_file:
            for line in cli_tree:
                # print(f"line: {line}")
                match_first_parent = re.search(FIRST_PARENT_REGEX,line)
                if match_first_parent:
                    line = re.sub(FIRST_PARENT_REGEX, r'\1', line, re.MULTILINE)
                match_last_parent = re.search(LAST_PARENT_REGEX, line)
                if match_last_parent:
                    line = re.sub(LAST_PARENT_REGEX, r'\1', line, re.MULTILINE)
                    line = line.strip()
                match_leaf = re.search(LEAF_REGEX, line)
                if match_leaf:
                    line = re.sub(LEAF_REGEX, r'\1\2', line, re.MULTILINE)
                match_last_leaf = re.search(LAST_LEAF_REGEX, line)
                if match_last_leaf:
                    line = re.sub(LAST_LEAF_REGEX, r'\1\2', line, re.MULTILINE)
                match_dangling_line = re.search(DANGLING_LINE_REGEX, line)
                if match_dangling_line:
                    line = re.sub(DANGLING_LINE_REGEX, r'\1\2', line, re.MULTILINE)
                match = re.search(CLEAN_LINE_TO_YAML_REGEX,line)
                if match:
                    line = re.sub(CLEAN_LINE_TO_YAML_REGEX,r'\1\2:\3\n',line,re.MULTILINE)
                else:
                    line = re.sub(TOP_LEVEL_CLEAN_LINE_TO_YAML_REGEX,r'\1:\2\n',line,re.MULTILINE)
                print(f"line: {line}")
                output_file.write(line)
            # Rewind temp file to beginning before parsing.
            output_file.seek(0)
            # 4) Parse text tree into list of dictionaries.
            lines = [line.rstrip() for line in output_file.readlines()]
            non_empty_lines = [line for line in lines if line != '']
            for line in non_empty_lines:
                # line = line[:-1]
                content = line.lstrip()
                currentIndentation = len(line) - len(content) + 1
                folder_name, folder_id = content.split(':')

                # If new line's indentation is shallower than previous, we need to remove items from the list
                if currentIndentation < indentation[-1]:
                    while currentIndentation < indentation[-1]:
                        depth -= 1
                        indentation.pop()
                    if currentIndentation != indentation[-1]:
                        raise RuntimeError("Bad formatting")
                    parents = parents[:depth]
                # If new line's indentation is deeper, we need to add the previous node
                elif currentIndentation > indentation[-1]:
                    depth += 1
                    indentation.append(currentIndentation)
                    parents.append(node)
                # Create new node
                node = {"folder": folder_name.strip(), "id": folder_id.strip(), "depth" : depth, "children": []}
                parents[-1]['children'].append(node)
        # 5) Close temporary files & return list of dictionaries.
        print(root["children"])
        parsed_tree.close()
        cli_tree.close()
        return(root["children"])


def get_folder_id(name: str, tree: [] = None):
    """
    Given the name of a folder in the workpace and a list of dictionaries
    representing the VWB workspace's folder tree, returns the ID corresponding to the folder name,
    if it exists; else returns None.
    """
    for item in tree:
        current_name = item['folder'].strip()
        if current_name == name:
            return item['id']
        folder_id_from_children = get_folder_id(name, item['children'])
        if folder_id_from_children is not None:
            return folder_id_from_children
    return None

def get_folders_with_depth(workspace_id: str, depth: int):
    """
    Given the workspace ID of a data collection, and a desired depth ( >= 1),
    returns a list of folders in the workspace with that depth.
    """
    # 1) Get workspace folder tree, if not provided.
    cli_folder_tree_output = subprocess.run(
        ["terra", "folder", "tree", f"--workspace={workspace_id}"], capture_output=True, text=True
    )
    cli_output = cli_folder_tree_output.stdout
    print(f"cli_output:\n{cli_output}")
    
    # 2) Parse tree to list of dictionaries.
    tree = parse_tree(cli_output)
    folders_at_depth = []
    for item in tree:
        if item['depth'] == depth:
            folders_at_depth.append(item['folder'].strip())
    # 3) Return list of versions.
    return folders_at_depth

def get_potential_versions(workspace_id: str):
    """
    Given a workspace ID, returns the top-level folders for that directory 
    which are eligible for publication as a data collection version.
    """
    return get_folders_with_depth(workspace_id, depth = 1)