import os
import yaml
from dvuploader import File


def os_walk(path):
    """Generator that yields all files in a directory tree.

    Args:
        path (str): The path to the directory to walk.
    """
    holding_dict = {'file': []}
    for root, dirs, files in os.walk(path):
        for file in files:
            holding_dict['file'].append({
                'filepath': os.path.join(root, file),
                'directory_label': dirs if dirs else None,  # Replace empty list with None
                'files': file
            })
    return holding_dict

def config_wizard():
    """Wizard to guide the user through the process of creating a config file.
    
    Returns:
        dict: A dictionary containing the user's input.
    """
    persistent_id = input("Please enter the persistent id: ")
    dataverse_url = input("Please enter the dataverse url: ")
    api_token = input("Please enter the API token: ")
    dir_path = input("Please enter the directory path: ")
    file_nested_dict = os_walk(dir_path)

    return {
        'persistent_id': persistent_id,
        'dataverse_url': dataverse_url,
        'api_token': api_token,
        'files': file_nested_dict
    }
