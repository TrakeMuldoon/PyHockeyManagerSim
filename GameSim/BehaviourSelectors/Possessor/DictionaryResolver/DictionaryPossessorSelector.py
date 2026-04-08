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

        action_table: TableSelector = self._build_action_table_from_base_file(file)

    def _build_action_table_from_base_file(self, file: TextIO) -> TableSelector:
        table_selector: TableSelector = PARSER.parse_base_probabilities_file(file)
        return table_selector
    def select_action(self) -> str:
        return "HOLD"

    def get_output_actions(self) -> List[str]:
        return ["HOLD"]
