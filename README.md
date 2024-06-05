# Ethereum python research scripts

> [!NOTE] 
> This project is a collection of Python scripts for Ethereum research and analysis. The scripts are designed to interact with an Ethereum node using the JSON-RPC API and provide various functionalities, such as generating access lists, extracting state diffs, and more.

## Requirements

- RPC with `trace_replayTransaction` enabled

## Abstract

The script generates and reads a JSON file containing Ethereum state differences (`stateDiff`), processes the data to extract account addresses and their respective storage keys, and generates an access list. This list can be useful for various purposes, such as optimizing Ethereum transactions or understanding changes in the state.


### Access List

> Generates an access list from the state diff of an Ethereum transaction.

The `generate_access_list_from_statediff` function takes the JSON response from an Ethereum node's `eth_getTransactionReceipt` RPC method, which includes the `stateDiff` field. It then iterates through the state diff, extracting the accounts and their modified storage slots, and returns an access list in the format expected by the Ethereum client.

The access list is a list of dictionaries, where each dictionary has two keys:
- `"address"`: the address of the account
- `"storageKeys"`: a list of the modified storage slots for that account

This access list can be used to optimize the execution of the transaction by only accessing the accounts and storage slots that were modified, rather than the entire state.


### State Diff JSON Format

```jsonc
{
  "jsonrpc": "2.0",
  "result": {
    "stateDiff": {
      "0x9162accd2bf58dcf5f5d46e5818117e3f5cd8333": {
        "balance": {"*": {"from": "0x1e8b422a215aff2a", "to": "0x1c8a6a7b5aa9727a"}},
        "code": "=",
        "nonce": {"*": {"from": "0x259", "to": "0x25a"}},
        "storage": {}
      },
      "0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5": {
        "balance": {"*": {"from": "0xcbf2d42250f0eb19", "to": "0xcbf2e3a93cf93319"}},
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
      // Additional accounts...
    }
  },
  "id": 1
}
```

### Access List JSON Format

```jsonc
[
  {
    "address": "0x9162accd2bf58dcf5f5d46e5818117e3f5cd8333",
    "storageKeys": []
  },
  {
    "address": "0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5",
    "storageKeys": []
  }
  // Additional accounts...
]
```

## License

This project is licensed under the UPL-1.0 License

