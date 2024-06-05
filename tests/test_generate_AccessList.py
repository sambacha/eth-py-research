import json
from unittest.mock import patch
from your_module import generate_access_list_from_statediff

def test_generate_access_list_from_statediff_with_storage_changes():
    state_diff = {
        'result': {
            'stateDiff': {
                '0x1234': {
                    'storage': {
                        '0x0000': {'from': '0x00', 'to': '0x01'},
                        '0x0001': {'from': '0x00', 'to': '0x02'}
                    }
                },
                '0x5678': {
                    'storage': {
                        '0x0000': {'from': '0x00', 'to': '0x03'}
                    }
                }
            }
        }
    }
    
    expected_access_list = [
        {'address': '0x1234', 'storageKeys': ['0x0000', '0x0001']},
        {'address': '0x5678', 'storageKeys': ['0x0000']}
    ]
    
    access_list = generate_access_list_from_statediff(state_diff)
    
    assert access_list == expected_access_list

def test_generate_access_list_from_statediff_without_storage_changes():
    state_diff = {
        'result': {
            'stateDiff': {
                '0x1234': {
                    'balance': {'from': '0x00', 'to': '0x100'}
                },
                '0x5678': {
                    'nonce': {'from': '0x00', 'to': '0x01'}
                }
            }
        }
    }
    
    expected_access_list = []
    
    access_list = generate_access_list_from_statediff(state_diff)
    
    assert access_list == expected_access_list

def test_generate_access_list_from_statediff_empty_state_diff():
    state_diff = {
        'result': {
            'stateDiff': {}
        }
    }
    
    expected_access_list = []
    
    access_list = generate_access_list_from_statediff(state_diff)
    
    assert access_list == expected_access_list
