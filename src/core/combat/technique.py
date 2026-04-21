import pygame, random, operator

class Technique:
    def __init__(self, name, type, req):
        self.name         = name
        self.type         = type
        self.requirements = req

        self.data         = None
        self.typeoftarget = None
        self.typeofarea   = None
        self.targetrange  = 1

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

        return True


class Passive:
    def __init__(self):
        self.data  = {
            'usage': { 'times': 0, 'total': 0, },
            'transfer': { 'times_used': 0 } }

class Pact:
    def __init__(self):
        self.data = {
            'usage': { 'times': 0, 'total': 0, 'limit': 15 },
            'transfer': { 'times_used': 0 } }

class Active:
    def __init__(self):
        self.data = { 
            'usage': { 'times': 0, 'total': 0, },
            'transfer': { 'times_used': 0, 'complete': 0, 'blocked': 0 } }

                
            
