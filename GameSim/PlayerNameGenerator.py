import os
from random import random

class _innerGenerator:
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    ln_path = "..\\Reference\\LastNames.txt"
    fn_path = "..\\Reference\\FirstNames.txt"
    full_fn_path = os.path.join(script_dir, fn_path)
    full_ln_path = os.path.join(script_dir, ln_path)


    def __init__(self):
        with open(self.full_ln_path, encoding="utf-8") as ln_file:
            self.last_names = ln_file.read().splitlines()

        with open(self.full_fn_path, encoding="utf-8") as fn_file:
            self.first_names = fn_file.read().splitlines()


class PlayerNameGenerator:
    _generator = _innerGenerator()

    @staticmethod
    def random_last_name():
        index = random() * len(PlayerNameGenerator._generator.last_names)
        index = int(index)
        last_name = PlayerNameGenerator._generator.last_names[index]
        return last_name

    @staticmethod
    def random_first_name():
        index = random() * len(PlayerNameGenerator._generator.first_names)
        index = int(index)
        last_name = PlayerNameGenerator._generator.first_names[index]
        return last_name
