"""This test module tests changes made to console.py during this project"""

import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.place import Place
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        create_instance_id = "12345"
        instance = storage.all()[Place].get(created_instance_id)

        # Check if the instance exists
        self.assertTrue(instance is not None)

if __name__ == "__main__":
    unittest.main()
