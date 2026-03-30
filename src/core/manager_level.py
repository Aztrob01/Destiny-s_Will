from core.unities.entities.entities import Entities
from core.unities.entities.enemy    import dmy, gob
import random

class LevelBuilder:
    def __init__(self, data_level):
        self.data_level = data_level

    def generate_battleground(self):
        background = self.data_level['battleground']
        return background
    
    def generate_enemies(self):

        entities_dict = {
            'dmy': dmy,
            'gob': gob,
        }

        entities = []
        output = []
        slots = random.randint(1, 5)

        for inds in self.data_level['enemies']: 
            entities.append(self.data_level['enemies'][inds])

        for i in range(slots):
            gen_chance = random.uniform(0, 1)
            for ents in entities:
                if gen_chance <= ents[2]:
                    if ents[0] in entities_dict:
                        output.append(Entities(entities_dict[ents[0]]()))
        
        return output
