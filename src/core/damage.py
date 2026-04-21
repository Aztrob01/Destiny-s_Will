def sk_damage(user, target, amount=int, can_miss=False):
    if can_miss:
        import random
        miss = 0.05 + (target.combat_profile.attr.main['dex'] / 100)
        chance = random.uniform(0.01, 1)

        if chance <= miss:
            return False
    
    target.combat_profile.stats['hp']['current'] -= amount
    user.combat_profile.history['dealt']['damage_by_skills'] += amount

    if amount > user.combat_profile.history['dealt']['highest_damage_dealt']:
        user.combat_profile.history['dealt']['highest_damage_dealt'] = amount
    
    return True