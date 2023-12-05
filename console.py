#!/usr/bin/python3
"""console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """console class for HBNB; AirBnb clone
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """implements the quit command
        """
        return True

    def do_EOF(self, line):
        """implements EOF input
        """
        print()
        return True

    def emptyline(self):
        """implements empty line as command
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
