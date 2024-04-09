import cmd

"""
This module contains the console class which is used to interact with the user
"""

class Tafuta(cmd.Cmd):
    """
    Class for the console
    """
    prompt = "(Tafuta) "
    intro = "Welcome to the Lost and Found Console"

    def do_quit(self, arg):
        """
        Quit the console
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console
        """
        return True

    def emptyline(self):
        """
        Do nothing
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class
        """
        pass

    def do_show(self, arg):
        """
        Show an instance of a class
        """
        pass

    def do_destroy(self, arg):
        """
        Destroy an instance of a class
        """
        pass

    def do_all(self, arg):
        """
        Show all instances of a class
        """
        pass

    def do_update(self, arg):
        """
        Update an instance of a class
        """
        pass

    def do_help(self, arg):
        """
        Show help for a command
        """
        

if __name__ == "__main__":
    Tafuta().cmdloop()
