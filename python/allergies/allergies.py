ALLERGY_MAP = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128 }

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return self.score & ALLERGY_MAP[item] != 0

    @property
    def lst(self):
        return [item for item, mask in ALLERGY_MAP.items() if self.score & mask != 0]
