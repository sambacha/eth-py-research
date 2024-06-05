import os
import json
from unittest.mock import mock_open, patch
from your_module import save_generated_statediff

def test_save_generated_statediff():
    generated_statediff = {"key1": "value1", "key2": "value2"}
    filename = "test_statediff.json"
    
    with patch("builtins.open", mock_open()) as mock_file:
        save_generated_statediff(generated_statediff, filename)
        
        mock_file.assert_called_once_with(filename, 'w')
        mock_file.return_value.write.assert_called_once_with(
            json.dumps(generated_statediff, indent=2)
        )

def test_save_generated_statediff_file_created():
    generated_statediff = {"key1": "value1", "key2": "value2"}
    filename = "test_statediff.json"
    
    with patch("builtins.open", mock_open()) as mock_file:
        save_generated_statediff(generated_statediff, filename)
        
        assert os.path.exists(filename)
        
        with open(filename, 'r') as file:
            saved_statediff = json.load(file)
            assert saved_statediff == generated_statediff
        
    os.remove(filename)

def test_save_generated_statediff_empty_dict():
    generated_statediff = {}
    filename = "test_statediff.json"
    
    with patch("builtins.open", mock_open()) as mock_file:
        save_generated_statediff(generated_statediff, filename)
        
        mock_file.assert_called_once_with(filename, 'w')
        mock_file.return_value.write.assert_called_once_with(
            json.dumps(generated_statediff, indent=2)
        )
