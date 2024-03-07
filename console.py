#!/usr/bin/python3

"""The entry point to the console 
"""

import cmd
import re
import json 
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd) :
    """This class is the command interpretter
    """
    prompt = "(hbnb)"
    def default(self, line):
        """ If nothing happens do this
        """
        # to print (DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """ tests the commands syntax
        """
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)

        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False


    attr_and_value = ""
    if method == "update" and attr_or_dict:
        match_dict = re.search('^({.*})$', attr_or_dict)

