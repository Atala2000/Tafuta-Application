#!/usr/bin/env python3
"""
Module that contains the console class
"""

import cmd
from models.users.database import DataStorage
from models.users import models
from datetime import datetime
import os

MODELS = {
    "users": models.Users,
    "items": models.Items,
    "connected_items": models.Connected_Items,
}


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
        if args and args[0].lower() in MODELS:
            try:
                items = self.data_storage.all(MODELS[args[0]])
                print(f"Instance of {args[0]}")
                for item in items:
                    print()

                    for key, value in item.__dict__.items():
                        if key != "_sa_instance_state":
                            print(f"{key}: {value}")
                    print()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Allowed classnames are: ")
            for model_class in MODELS:
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

    def do_test_object(self, arg):
        """
        Creates test objects
        Usage is `test_object` <classname> <firstname> <lastname> <email> <password>
        """
        try:
            args = arg.split()
            if len(args) < 1:
                print(
                    f"""Insufficient arguments provided. Usage is `test_object` <classname> <firstname>
                <lastname> <email> <password>
                """
                )
                return

            object_type = args[0]
            if object_type == "user" and len(args) == 6:
                self.data_storage.add(
                    models.Users(
                        first_name=args[1],
                        last_name=args[2],
                        email=args[3],
                        password=args[4],
                        phone_no=int(args[5]),
                    )
                )
                print("User object created successfully.")

            elif object_type == "items" and len(args) == 6:
                self.data_storage.add(
                    models.Items(
                        date_found=datetime.now(),
                        location_found=args[1],
                        description=args[2],
                        filename=args[3],
                        category=args[4],
                        users_id=int(args[5]),
                    )
                )
                print("Item object created successfully.")
            elif object_type == "connected_items" and len(args) == 6:
                self.data_storage.add(
                    models.Connected_Items(
                        item_id=args[1],
                        owner_id=args[2],
                        reporter_id=args[3],
                        date_connected=args[4],
                        location_connected=args[5],
                    )
                )
                print("Connected item object created successfully.")
            else:
                print("Invalid arguments provided.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def do_delete(self, arg):
        """
        Delete an instance of a class
        """
        args = arg.split()
        if args and args[0].lower() in MODELS:
            try:
                object_instance = self.data_storage.get(MODELS[args[0]], int(args[1]))
                self.data_storage.delete(object_instance)
                print(f"Deleted {args[0]} with id {args[1]}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Allowed classnames are: ")
            for model_class in MODELS:
                print(model_class)
            print()

    def do_total(self, arg):
        """
        Returns a count of the selected class
        Args:
            arg (str): Classname
        """
        if not arg:
            print("Usage: total <classname>")
            return

        classname = arg.strip()

        # Assuming MODELS_ARRAY is defined elsewhere in your code
        if classname in MODELS:
            try:
                count = self.data_storage.count(MODELS[classname])
                print(f"Total count of {classname}: {count}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid class name. Allowed classnames are:")
            print(", ".join(MODELS))

    def do_backup(self, arg):
        """
        Creates a backup file of the current database storage
        """
        from models.users.database import DataStorage
        credentials = {
            'database_name': DataStorage.url_object.database,
            'database_user': DataStorage.url_object.username,
        }
        sql_command
        try:
            os.system(f"mysqldump -u -{credentials.get('database_user')} -p -{credentials.get('database_name')} > data-dump.sql")
        except:
            print(f"An error occured")

if __name__ == "__main__":
    Tafuta().cmdloop()
