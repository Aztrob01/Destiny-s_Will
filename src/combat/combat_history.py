class CombatHistory:
    def __init__(self, user):
        self.user = user
        self.skills = []

        # ----------------

        self.rounds_played = 0
        self.total_damage_dealt  = 0
        self.min_damage = 0
        self.max_damage = 0
        self.total_healed_self   = 0
        self.total_healed_allies = 0
        self.total_healed = 0 
        self.min_heal = 0
        self.max_heal = 0

        self.total_damage_mitg = 0

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

    