class CombatBuffer:
    def __init__(self):
        
        self.last_round          = 0
        self.actual_round        = 0
        self.get_hitted          = 0
        self.get_hitted_by       = None
        self.allies              = []
        self.enemies             = []


        self.rounds_played       = 0
        self.total_damage_dealt  = 0
        self.min_damage          = 0
        self.max_damage          = 0
        self.total_healed_self   = 0
        self.total_healed_allies = 0
        self.total_healed        = 0 
        self.min_heal            = 0
        self.max_heal            = 0
        self.total_damage_mitg   = 0

        # ----------------

        self.ba_times  = 0
        self.ba_total_damage = 0
        self.ba_total_heal   = 0
        self.ba_min_damage   = 0
        self.ba_max_damage   = 0

        self.sk0_times = 0 # skill 0 is passive
        self.sk0_total_damage = 0
        self.sk0_total_heal   = 0
        self.sk0_total_blocked = 0
        self.sk0_min_damage   = 0
        self.sk0_max_damage   = 0
        self.sk0_min_healed   = 0
        self.sk0_max_healed   = 0

        self.sk1_times = 0
        self.sk1_total_damage = 0
        self.sk1_total_heal   = 0
        self.sk1_total_blocked = 0
        self.sk1_min_damage   = 0
        self.sk1_max_damage   = 0
        self.sk1_min_healed   = 0
        self.sk1_max_healed   = 0

        self.sk2_times = 0
        self.sk2_total_damage = 0
        self.sk2_total_heal   = 0
        self.sk2_total_blocked = 0
        self.sk2_min_damage   = 0
        self.sk2_max_damage   = 0
        self.sk2_min_healed   = 0
        self.sk2_max_healed   = 0

        self.sk3_times = 0
        self.sk3_total_damage = 0
        self.sk3_total_heal   = 0
        self.sk3_total_blocked = 0
        self.sk3_min_damage   = 0
        self.sk3_max_damage   = 0
        self.sk3_min_healed   = 0
        self.sk3_max_healed   = 0

        self.sk4_times = 0
        self.sk4_total_damage = 0
        self.sk4_total_heal   = 0
        self.sk4_total_blocked = 0
        self.sk4_min_damage   = 0
        self.sk4_max_damage   = 0
        self.sk4_min_damage   = 0
        self.sk4_max_damage   = 0


    def reset(self):
        self.last_round          = 0

        self.rounds_played       = 0
        self.total_damage_dealt  = 0
        self.min_damage          = 0
        self.max_damage          = 0
        self.total_healed_self   = 0
        self.total_healed_allies = 0
        self.total_healed        = 0 
        self.min_heal            = 0
        self.max_heal            = 0
        self.total_damage_mitg   = 0

        # ----------------

        self.ba_times  = 0
        self.ba_total_damage = 0
        self.ba_total_heal   = 0
        self.ba_min_damage   = 0
        self.ba_max_damage   = 0

        self.sk0_times = 0 # skill 0 is passive
        self.sk0_total_damage = 0
        self.sk0_total_heal   = 0
        self.sk0_total_blocked = 0
        self.sk0_min_damage   = 0
        self.sk0_max_damage   = 0
        self.sk0_min_healed   = 0
        self.sk0_max_healed   = 0

        self.sk1_times = 0
        self.sk1_total_damage = 0
        self.sk1_total_heal   = 0
        self.sk1_total_blocked = 0
        self.sk1_min_damage   = 0
        self.sk1_max_damage   = 0
        self.sk1_min_healed   = 0
        self.sk1_max_healed   = 0

        self.sk2_times = 0
        self.sk2_total_damage = 0
        self.sk2_total_heal   = 0
        self.sk2_total_blocked = 0
        self.sk2_min_damage   = 0
        self.sk2_max_damage   = 0
        self.sk2_min_healed   = 0
        self.sk2_max_healed   = 0

        self.sk3_times = 0
        self.sk3_total_damage = 0
        self.sk3_total_heal   = 0
        self.sk3_total_blocked = 0
        self.sk3_min_damage   = 0
        self.sk3_max_damage   = 0
        self.sk3_min_healed   = 0
        self.sk3_max_healed   = 0

        self.sk4_times = 0
        self.sk4_total_damage = 0
        self.sk4_total_heal   = 0
        self.sk4_total_blocked = 0
        self.sk4_min_damage   = 0
        self.sk4_max_damage   = 0
        self.sk4_min_damage   = 0
        self.sk4_max_damage   = 0

    def update(self, buffer, target): # the wrost possible just because i acephalic
        target.history.rounds_played       += self.rounds_played
        target.history.total_damage_dealt  += self.total_damage_dealt
        target.history.min_damage          += self.min_damage
        target.history.max_damage          += self.max_damage
        target.history.total_healed_self   += self.total_healed_self
        target.history.total_healed_allies += self.total_healed_allies
        target.history.total_healed        += self.total_healed
        target.history.min_heal            += self.min_heal
        target.history.max_heal            += self.max_heal
        target.history.total_damage_mitg   += self.total_damage_mitg

        # ----------------

        target.history.ba_times  += self.ba_times
        target.history.ba_total_damage += self.ba_total_damage
        target.history.ba_total_heal   += self.ba_total_heal
        target.history.ba_min_damage   += self.ba_min_damage
        target.history.ba_max_damage   += self.ba_max_damage

        target.history.sk0_times += self.sk0_times
        target.history.sk0_total_damage += self.sk0_total_damage
        target.history.sk0_total_heal   += self.sk0_total_heal
        target.history.sk0_total_blocked += self.sk0_total_blocked
        target.history.sk0_min_damage   += self.sk0_min_damage
        target.history.sk0_max_damage   += self.sk0_max_damage
        target.history.sk0_min_healed   += self.sk0_min_healed
        target.history.sk0_max_healed   += self.sk0_max_healed

        target.history.sk1_times += self.sk1_times
        target.history.sk1_total_damage += self.sk1_total_damage
        target.history.sk1_total_heal   += self.sk1_total_heal
        target.history.sk1_total_blocked += self.sk1_total_blocked
        target.history.sk1_min_damage   += self.sk1_min_damage
        target.history.sk1_max_damage   += self.sk1_max_damage
        target.history.sk1_min_healed   += self.sk1_min_healed
        target.history.sk1_max_healed   += self.sk1_max_healed

        target.history.sk2_times += self.sk2_times
        target.history.sk2_total_damage += self.sk2_total_damage
        target.history.sk2_total_heal   += self.sk2_total_heal
        target.history.sk2_total_blocked += self.sk2_total_blocked
        target.history.sk2_min_damage   += self.sk2_min_damage
        target.history.sk2_max_damage   += self.sk2_max_damage
        target.history.sk2_min_healed   += self.sk2_min_healed
        target.history.sk2_max_healed   += self.sk2_max_healed

        target.history.sk3_times += self.sk3_times
        target.history.sk3_total_damage += self.sk3_total_damage
        target.history.sk3_total_heal   += self.sk3_total_heal
        target.history.sk3_total_blocked += self.sk3_total_blocked
        target.history.sk3_min_damage   += self.sk3_min_damage
        target.history.sk3_max_damage   += self.sk3_max_damage
        target.history.sk3_min_healed   += self.sk3_min_healed
        target.history.sk3_max_healed   += self.sk3_max_healed

        target.history.sk4_times += self.sk4_times
        target.history.sk4_total_damage += self.sk4_total_damage
        target.history.sk4_total_heal   += self.sk4_total_heal
        target.history.sk4_total_blocked += self.sk4_total_blocked
        target.history.sk4_min_damage   += self.sk4_min_damage
        target.history.sk4_max_damage   += self.sk4_max_damage
        target.history.sk4_min_healed   += self.sk4_min_healed
        target.history.sk4_max_healed   += self.sk4_max_healed