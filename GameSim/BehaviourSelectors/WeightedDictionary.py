from random import Random
from typing import List, Tuple


# TODO implement class stuff to make it act more like a dictionary
# TODO Disallow value updating
class WeightedDictionary:
    r = Random()
    initalized = False

    def __init__(self, dict_values: List[Tuple[str, float]]) -> None:
        self.dictionary: dict = {}
        incremental_weight = 0.0
        for key, weight in dict_values:
            self.dictionary[key] = weight
            incremental_weight += weight
        if incremental_weight < 99 or incremental_weight > 101:
            raise Exception(f"Weights must add to 100. {incremental_weight}")

    def get_weighted_random_value(self) -> str:
        rand = WeightedDictionary.r.random() * 100
        incremental_weight = 0
        for key, weight in self.dictionary.items():
            incremental_weight += weight
            if rand < incremental_weight:
                return key
        raise Exception(f"Did not match anything. {rand} vs {incremental_weight}")

    def keys(self) -> list[str]:
        return list(self.dictionary.keys())
