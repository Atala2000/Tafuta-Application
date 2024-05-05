import os
from models.users.database import DataStorage

def test_command():
    os.system("echo 'I am a boy'")
    print(f"{DataStorage.url_object.password}")


if __name__ == "__main__":
    test_command()
