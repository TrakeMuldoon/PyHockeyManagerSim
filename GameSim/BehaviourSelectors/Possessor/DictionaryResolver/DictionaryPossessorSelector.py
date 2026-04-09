from typing import List, TextIO

from GameSim import GameSim
from GameSim.BehaviourSelectors.Possessor.DictionaryResolver.ProbabilitiesFileParser import ProbabilitiesFileParser
from GameSim.BehaviourSelectors.Possessor.DictionaryResolver.TableSelector import TableSelector
from GameSim.BehaviourSelectors.Possessor.PossessorActionSelector import PossessorActionSelector

PARSER: ProbabilitiesFileParser = ProbabilitiesFileParser()

class DictionaryPossessorSelector(PossessorActionSelector):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)
        file: TextIO = open("Tables/Possessor/BaseProbabilitesByPosition.hmsp")
        self.action_table: TableSelector = self._build_action_table_from_base_file(file)

    def _build_action_table_from_base_file(self, file: TextIO) -> TableSelector:
        return PARSER.parse_base_probabilities_file(file)

    def select_action(self) -> str:
        pos = self.game_sim.puck_possessor.position   # e.g. "LD" (short form)
        zone = self.game_sim.puck_zone                # e.g. 17 (int)
        wd = self.action_table[pos][zone]             # TableSelector → WeightedDictionary
        return wd.get_weighted_random_value()

    def get_output_actions(self) -> List[str]:
        return ["PASS_BACK",
                "PASS_LATERAL",
                "PASS_FORWARD",
                "CARRY_BACK",
                "CARRY_LATERAL",
                "CARRY_FORWARD",
                "SHOOT_LIGHT",
                "SHOOT_HARD",
                "HOLD"]
