from root.utils import json_gets

class SaveManager:
    def __init__(self):
        self.state = 'waiting...'
        self.path = './src/game/users/save.json'
        self.model = {  
            "save_metadata": {
                "last_saved": "2026-03-26",
                "last_section": "2026-03-26 17:00",
                "game_version": None,
            },
            "player_data": {
                "gold": 1200,
                "inventory": "Clear",
                "localization": {
                    "map": "Training Ground - Guilhadard's Mansion",
                    "x": 0,
                    "y": 0
                },
                "active_party": None,
            },
            "party_data": {
                "slot_1": None,
                "slot_2": None,
                "slot_3": None,
                "slot_4": None,
            }
        }

    def load(self):
        pass