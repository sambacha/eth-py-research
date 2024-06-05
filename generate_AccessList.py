#!/usr/bin/env python3
"""
Reads `state_diff.json` from make_statediff.py

1. **read_json_file**:
    - Reads a JSON file from the specified path and returns the parsed JSON data.
    - Raises a `FileNotFoundError` if the file does not exist.

2. **generate_access_list_from_statediff**:
    - Processes the JSON data to extract account addresses and their respective storage keys from the `stateDiff`.
    - Returns a list of accounts and their storage keys.

3. **Main Execution Block**:
    - Reads the JSON data from the file.
    - Calls the `generate_access_list_from_statediff` function with the JSON data.
    - Prints the generated access list in a formatted JSON structure.

"""
import os
import json

def read_json_file(file_path):
    """Read a JSON file and return the parsed JSON data."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_access_list_from_statediff(state_diff):
    """Generate an access list from the given stateDiff JSON data."""
    access_list = []
    # Iterate through each account in the stateDiff
    for account, diff in state_diff['result']['stateDiff'].items():
        # Initialize the list of storageKeys for this account
        storage_keys = []
        # Check if 'storage' changes are present for this account
        if 'storage' in diff:
            # Iterate through each storage slot change
            for slot, change in diff['storage'].items():
                # Add the slot to the list
                storage_keys.append(slot)
        # Append the account and its storage keys to the access list
        if storage_keys:
            access_list.append({"address": account, "storageKeys": storage_keys})
    return access_list

if __name__ == "__main__":
    file_path = 'state_diff.json'  # Path to your JSON file
    try:
        state_diff = read_json_file(file_path)
        access_list = generate_access_list_from_statediff(state_diff)
        print(json.dumps(access_list, indent=2))
    except Exception as e:
        print(f"Error: {e}")
