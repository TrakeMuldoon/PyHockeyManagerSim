import os
from random import random
from typing import Set
from GameSim.Team import Team


class _inner_generator:
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    cities_path = "../../Reference/Cities.txt"
    names_path = "../../Reference/TeamNames.txt"
    full_city_path = os.path.join(script_dir, cities_path)
    full_name_path = os.path.join(script_dir, names_path)

    def __init__(self):
        with open(self.full_city_path, encoding="utf-8") as city_file:
            self.city_names = city_file.read().splitlines()

        with open(self.full_name_path, encoding="utf-8") as name_file:
            self.team_names = name_file.read().splitlines()


class TeamNameGenerator:
    _generator = _inner_generator()
    _teams_created: Set[str] = set()

    @staticmethod
    def populate_team_information(empty_team: Team):
        unique_name = False
        while not unique_name:
            index = random() * len(TeamNameGenerator._generator.city_names)
            index = int(index)

            # set location (City, Province, Country)
            empty_team.location = TeamNameGenerator._generator.city_names[index]

            # get city name
            city_name = empty_team.location.split("\t")[0]

            team_index = random() * len(TeamNameGenerator._generator.team_names)
            team_index = int(team_index)
            team_mascot = TeamNameGenerator._generator.team_names[team_index]

            full_name = f"{city_name} {team_mascot}"
            empty_team.team_name = full_name
            unique_name = full_name not in TeamNameGenerator._teams_created

        TeamNameGenerator._teams_created.add(full_name)
