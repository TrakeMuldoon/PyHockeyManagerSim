from enum import Enum
from io import TextIOWrapper
from typing import List, Tuple, TextIO
import re

from GameSim.BehaviourSelectors.Possessor.DictionaryResolver.TableSelector import TableSelector
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary

class BaseFileParserState(Enum):
    ROOT = 1
    IN_POSITION = 2

PROBABILITIES_REGEX_PATTERN = "(N\((\d+)\) ?PB\((\d+)\) ?PL\((\d+)\) ?PF\((\d+)\) ?CB\((\d+)\) ?CL\((\d+)\) ?CF\((\d+)\) ?SS\((\d+)\) ?SH\((\d+)\))"


ACTION_NAMES = ["HOLD", "PASS_BACK", "PASS_LATERAL", "PASS_FORWARD",
                "CARRY_BACK", "CARRY_LATERAL", "CARRY_FORWARD", "SHOOT_LIGHT", "SHOOT_HARD"]

class ProbabilitiesFileParser:
    def __init__(self):
        pass

    def parse_base_probabilities_file(self, file: TextIO) -> TableSelector:
        STATE = BaseFileParserState.ROOT
        current_position = None

        for line in file:
            if line.startswith("#"):
                # this is a comment line
                continue

            if STATE == BaseFileParserState.ROOT:
                if line == '\n': # Empty Line
                    continue

                new_pos = re.search("^(LD|RD|LW|RW|C)$", line)
                if new_pos:
                    current_position = new_pos.group(1)
                    STATE = BaseFileParserState.IN_POSITION
                    continue

            if STATE == BaseFileParserState.IN_POSITION:
                if line == '\n': # Empty Line
                    STATE = BaseFileParserState.ROOT
                    continue


                weights_table: List[Tuple[str, float]] = self.parse_rule_line(line)
                line_dict = WeightedDictionary(weights_table)
                # TODO: store line_dict against current_position and zone_select

    def parse_rule_line(self, line: str) -> List[Tuple[str, float]]:
        #{ZONE_SELECT}:\t*({ACTION_SET_NAME}|{ACTION_PROBABILITIES})

        zone_select_pattern = "^(\w+)\:\s+"
        pattern = zone_select_pattern + PROBABILITIES_REGEX_PATTERN + "$"
        zone_match = re.search(zone_select_pattern, line)
        rule_match = re.search(pattern, line)
        if not rule_match:
            raise Exception("Failure to parse probabilities file. Fix it.", line)

        weights_table = []
        for index, name in enumerate(ACTION_NAMES):
            weights_table.append((name, float(rule_match.group(index + 3))))
        return weights_table

    def parse_probability_tuple(self, s: str) -> Tuple[str, float]:
        parsed = re.search(r"\w{1,2}\((\d+)\)", s)
        return int(parsed.group(1))
