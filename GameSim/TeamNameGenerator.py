import os
from random import random

class _inner_generator:
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    cities_path = "..\\Reference\\Cities.txt"
    names_path = "..\\Reference\\TeamNames.txt"
    full_city_path = os.path.join(script_dir, cities_path)
    full_name_path = os.path.join(script_dir, names_path)


    def __init__(self):
        with open(self.full_city_path, encoding="utf-8") as city_file:
            self.city_names = city_file.read().splitlines()

        with open(self.full_name_path, encoding="utf-8") as name_file:
            self.team_names = name_file.read().splitlines()


class TeamNameGenerator:
    _generator = _inner_generator()
    _teams_created = {}

    @staticmethod
    def populate_team_information(empty_team):
        index = random() * len(TeamNameGenerator._generator.city_names)
        index = int(index)

        #set location (City, Provice, Country)
        empty_team.location = TeamNameGenerator._generator.city_names[index]

        #get city name
        city_name = empty_team.location.split("\t")[0]

        team_index = random() * len(TeamNameGenerator._generator.team_names)
        team_index = int(index)
        team_mascot = TeamNameGenerator._generator.team_names[team_index]

        empty_team.team_name = f"{city_name} {team_mascot}"
