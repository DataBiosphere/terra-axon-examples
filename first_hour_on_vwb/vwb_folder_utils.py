import re
import subprocess
import sys
import tempfile
  

# Constants for parsing output of CLI command `terra folder tree`.
FIRST_LINE_REGEX = r"^\├\─\─(.*\))*$"
LEAF_REGEX = r"^\│(\s*)\├\─\─(.*)$"
LAST_LEAF_REGEX = r"^\│(\s*)\└\─\─(.*)$"
LAST_LINE_REGEX = r"^(\s)*\└\─\─(.*)$"
CLEAN_LINE_TO_YAML_REGEX = r"^(.*)\s\((.*)\)$"


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
    with cli_output_tree as cli_tree:
        cli_tree.write(cli_output)
        # Rewind to start of file for reading.
        cli_tree.seek(0)
        # Define variables for setting up list of dictionaries as tree.
        depth = 0
        root = {"folder": "root", "id": "0", "children": []}
        parents = []
        node = root
        # 3) Parse file, replacing symbols with tabs.
        with parsed_tree as output_file:
            for line in cli_tree:
                line = re.sub(FIRST_LINE_REGEX,r'\1', line)
                line = re.sub(LAST_LINE_REGEX, r'\1\2', line, re.MULTILINE)
                line = line.strip()
                while re.search(LEAF_REGEX, line):
                    line = re.sub(LEAF_REGEX, r'\t\1\2', line, re.MULTILINE)
                while re.search(LAST_LEAF_REGEX, line):
                    line = re.sub(LAST_LEAF_REGEX, r'\t\1\2', line, re.MULTILINE)
                line += "\n"
                line = re.sub(CLEAN_LINE_TO_YAML_REGEX,r'\1 : \2',line,re.MULTILINE)
                output_file.write(line)
            # Rewind temp file to beginning before parsing.
            parsed_tree.seek(0)
            # 4) Parse text tree into list of dictionaries.
            for line in parsed_tree:
                folder_name, folder_id = line.split(' : ')
                line = line.rstrip()
                newDepth = len(line) - len(line.lstrip("\t")) + 1
                if newDepth < depth:
                    parents = parents[:newDepth]
                elif newDepth == depth + 1:
                    parents.append(node)
                elif newDepth > depth + 1:
                    raise Exception("Invalid file")
                depth = newDepth
                node = {"folder": folder_name.strip(), "id": folder_id.strip(), "children": []}         
                # add the new node into its parent's children
                parents[-1]["children"].append(node)
        # 5) Close temporary files & return list of dictionaries.
        parsed_tree.close()
        cli_tree.close()
        return root["children"]


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