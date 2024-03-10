#!/usr/bin/python3
"""Module to test the HBNB
"""


import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """class for test Console
    """

    def test_do_EOF(self):
        """ EOF commmand test 
	"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    def test_do_quit(self):
        """ quit commmand test 
	"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)


    def test_do_emptyline(self):
        """ emptyline command test 
	"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)


    def test_help(self):
        """ help command test 
	"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
	Documented commands (type help <topic>)
		"""
        self.assertEqual(s, f.getvalue())


    def test_do_all(self):
        """Tests the do_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")


if __name__ == "__main__":
    unittest.main()
