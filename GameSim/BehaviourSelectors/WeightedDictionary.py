from random import random
from typing import List, Tuple


class WeightedDictionary:
    def __init__(self, dict_values: List[Tuple[str, float]]) -> None:
        self.dictionary: dict = {}
        incremental_weight = 0.0
        for key, weight in dict_values:
            self.dictionary[key] = weight
            incremental_weight += weight
        if incremental_weight < 99 or incremental_weight > 101:
            raise Exception(f"Weights must add to 100. {incremental_weight}")

    def get_weighted_random_value(self) -> str:
        rand = (random() * 100) + 1
        incremental = 0
        for key in self.dictionary.keys():
            incremental += self.dictionary[key]
            if rand < incremental:
                return key
        raise Exception(f"Did not match anything. {rand} vs {incremental}")

    def keys(self) -> list[str]:
        return list(self.dictionary.keys())
