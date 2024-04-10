import cmd
from models.users.database import DataStorage

MODELS_ARRAY = ["Users", "Items", "Connected_Items"]


class Tafuta(cmd.Cmd):
    """
    Class for the console
    """

    prompt = "(Tafuta) "
    intro = "Welcome to the Lost and Found Console"

    def __init__(self):
        super().__init__(completekey="tab")
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

    def do_test(self, arg):
        """
        Prints out the command
        """
        args = arg.split()
        print(args)

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
        if args and args[0] in MODELS_ARRAY:
            try:
                items = self.data_storage.all(args[0])
                for item in items:
                    print(item)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Allowed classnames are: ")
            for model_class in MODELS_ARRAY:
                print(model_class)
            print()

    def do_create(self, arg):
        """
        Initial setup to create the models on specified database
        """
        self.data_storage.create()

    def do_help(self, arg):
        """
        Show help for a command
        """
        super().do_help(arg)

    def do_delete(self, arg):
        """
        Delete an instance of a class
        """
        args = arg.split()
        if args and args[0] in MODELS_ARRAY:
            try:
                object_instance = self.data_storage.get(args[0], args[1])
                self.data_storage.delete(object_instance)
                print(f"Deleted {args[0]} with id {args[1]}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Allowed classnames are: ")
            for model_class in MODELS_ARRAY:
                print(model_class)
            print()


if __name__ == "__main__":
    Tafuta().cmdloop()
