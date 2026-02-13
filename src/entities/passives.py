class AnyContextMenu:
    def __init__(self):
        self.allies = []


# ------------------------------------

class PassiveEngine:
    def __init__(self, name, passive):
        self.name    = name
        self.passive = passive
        self.context = AnyContextMenu()

    def active(self, user):
        self.passive(user)

# ------------------------------------

class ContractContext:
    def __init__(self, rarities):
        self.times_activated  = 0
        self.times_setted     = 0
        self.times_to_use     = 30

class ContractEngine:
    def __init__(self, name, set, use):
        self.name     = name
        self.passive  = set
        self.active   = use
        self.context  = ContractContext()

    def set(self, user):
        self.passive(user)
    
    def use(self, user, target):
        self.active(user, target)

# ------------------------------------

class SkillEngine:
    def __init__(self, name, active, passive):
        self.name    = name
        self.active  = active
        self.passive = passive
        self.context = AnyContextMenu()
    
    def set(self, user):
        self.passive(user)
    
    def use(self, user, target):
        self.active(user, target)


    
    #TODO passive.set() para settar as regras da passiva, como os alvos
        #TODO passive.use() para usar a passiva após a aplicação das regras
        # * o mesmo deve servir como regra para as skills que curam aliados
        # * ou possuem condições especificas 
        # skills database

    
    

        