from enum import Enum
from io import TextIOWrapper
from typing import List, Tuple, TextIO
import re

from GameSim.BehaviourSelectors.Possessor.DictionaryResolver.TableSelector import TableSelector
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary
from GameSim.SupportClasses.Positions import Position
from GameSim.SupportClasses.Zones import Zone

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

        tables = TableSelector("BaseProbabilitiesByPosition")  # tables[Position][Zone] = WeightedDictionary

        for raw_line in file:
            line = raw_line.strip()

            # skip comments
            if line.startswith("#"):
                continue

            if STATE == BaseFileParserState.ROOT:
                # skip blank lines
                if not line:
                    continue

                # detect start of a position block
                m = re.match(r"^(LD|RD|LW|RW|C|EX)$", line)
                if not m:
                    raise Exception(f"Unexpected line in ROOT: {line}")

                short_code = m.group(1)
                current_position = Position.from_short(short_code)
                if current_position not in tables:
                    tables[current_position] = {}
                STATE = BaseFileParserState.IN_POSITION
                continue

            if STATE == BaseFileParserState.IN_POSITION:
                # blank line ends this block
                if not line:
                    STATE = BaseFileParserState.ROOT
                    current_position = None
                    continue

                # parse zone selector
                zone_match = re.match(r"^(\w+):", line)
                if not zone_match:
                    raise Exception(f"Expected zone name in position block: {line}")
                zone_name = zone_match.group(1)

                # convert zone alias → list of ints
                try:
                    zone_values = getattr(Zone, zone_name).value
                except AttributeError:
                    raise Exception(f"Unknown zone alias '{zone_name}'", line)
                if isinstance(zone_values, int):
                    zone_values = [zone_values]

                # parse weights
                weights_table = self.parse_rule_line(line)
                weighted_dict = WeightedDictionary(weights_table)

                # store under Zone enums
                for z in zone_values:
                    zone_enum = Zone(z)
                    tables[current_position][zone_enum] = weighted_dict

        return tables

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
