class TeamEngine:
    def __init__(self, team):
        self.team = team
    
        self.disponible_unities = []
        self.active_unities     = []
        self.offline_unities    = []

        self.active_unities_index = 0
        self.active_unity = None

        def prev(self, jump=0):
            if self.active_unities_index <= 0:
                self.active_unities_index = len(self.active_unities) - 1
            else:
                self.active_unities_index -= 1
            self.active_unities_index += jump
            self.active_unity = self.active_unities[self.active_unities_index]
        
        def define(self):
            self.disponible_unities = self.team.unities
            if self.active_unities == []:
                self.active_unities = self.disponible_unities[:3]
            for unities in self.disponible_unities:
                if unities not in self.active_unities:
                    if unities not in self.offline_unities:
                        self.offline_unities.append(unities) 

        def next(self):
            if self.active_unities_index >= len(self.active_unities) - 1:
                self.active_unities_index = 0
            else:
                self.active_unities_index += 1
            self.active_unity = self.active_unities[self.active_unities_index]