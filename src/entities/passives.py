class SkillContext:
    def __init__(self):
        self.allies = []

class PassiveEngine:
    def __init__(self, name, passive):
        self.name    = name
        self.passive = passive
        self.context = SkillContext()

    def active(self, user):
        self.passive(user)


class SkillEngine:
    def __init__(self, active, passive):
        self.active  = active
        self.passive = passive
        self.context = SkillContext()
    
    def set(self, user):
        self.passive(user)
    
    def use(self, user, target):
        self.active(user, target)


    
    #TODO passive.set() para settar as regras da passiva, como os alvos
        #TODO passive.use() para usar a passiva após a aplicação das regras
        # * o mesmo deve servir como regra para as skills que curam aliados
        # * ou possuem condições especificas 
        # skills database

    
    

        