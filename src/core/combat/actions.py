import pygame, random, operator

class Technique:
    def __init__(self, name, type, req, data):
        self.name = name
        self.type = type
        self.requirements = req
        self.data = data
        self.targettype = None

    def data_copy(self, user):
        pass

    def data_save(self, user):
        pass

    def data_apply(self, user):
        pass

    def require(self, user, combat):

        ops = {
            ">": operator.gt,
            ">=": operator.ge,
            "<": operator.lt,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne
        }

        for requirements in self.requirements:
            if requirements[0] == 'combat':
                entry = combat[requirements[1]]

            if requirements[0] == 'usage':
                entry = self.data[requirements[0]][requirements[1]]

            if requirements[0] == 'user':
                entry = user.profile.stats[requirements[1]]
        
            if not ops[requirements[2]](entry, requirements[3]):
                return False

        return ops[requirements[2]](entry, requirements[3])




class Passive:
    def __init__(self):
        pass

class Pact:
    def __init__(self):
        pass

class Active:
    def __init__(self):
        pass

class Ac1(Technique):
    def __init__(self):
        super().__init__("Direct Attack", Active(), [("usage", "times", "<", 15)], None)
        self.targettype = ('single', 'enemy')



skills = {
    'passive':{},
    'pacts': {},
    'skills': {},
    'ultimate': {}     
}
