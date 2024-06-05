#!/usr/bin/env python3
"""
make_statediff

"""
import requests
import json
import sys

def make_statediff(node_url, tx_hash):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "trace_replayTransaction",
        "params": [tx_hash, ["stateDiff"]],
        "id": 1,
    }

    response = requests.post(node_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Invalid JSON response:", response.text)
            return

        if 'result' in data:
            result = data['result']
            print(result)
            timestamp = int(time.time())
            save_generated_statediff(result, f'generated_statediff_{timestamp}.json')
        else:
            print("Generation of State Diff could not be completed. Reason:", data.get('error', 'Unknown error'))
    else:
        print(response.content)
        print("Failed to connect to the node or transaction tracing not supported.")

def save_generated_statediff(generated_statediff, filename):
    with open(filename, 'w') as file:
        json.dump(generated_statediff, file, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python make_statediff.py <node_url> <tx_hash>")
        sys.exit(1)

    node_url = sys.argv[1]
    tx_hash = sys.argv[2]
    make_statediff(node_url, tx_hash)