import cmd
from models.users.database import DataStorage

class Tafuta(cmd.Cmd):
    """
    Class for the console
    """
    prompt = "(Tafuta) "
    intro = "Welcome to the Lost and Found Console"

    def __init__(self):
        super().__init__(completekey='tab')
        self.data_storage = DataStorage()

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

    def do_all(self, arg):
        """
        Show all instances of a class
        """
        args = arg.split()
        if args:
            try:
                items = self.data_storage.all(args[0])
                for item in items:
                    print(item)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Please provide a class name")

    def do_help(self, arg):
        """
        Show help for a command
        """
        print("Help message")

if __name__ == "__main__":
    Tafuta().cmdloop()
