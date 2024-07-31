from GameSim.BehaviourSelectors.Possessor.PossessorActionSelector import \
    PossessorActionSelector


class DictionaryPossessorSelector(PossessorActionSelector):
    def __init__(self, sim: "GameSim"):
        super().__init__(sim)
