class hero():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = 100
        self.auto_atk_dmg = 10
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
    
hero_mm1 = hero("Moscov", "Marksman", "Attack damage")
hero_mage1 = hero("Kagura", "Mage", "Magic Damage")
hero_fighter1 = hero("Yu Zhong", "Fighter", "Attack damage")
hero_jungle1 = hero("Lancelot", "Jungle", "Burst Damage")
hero_tank1 = hero("Khufra", "Tank", "Damage Taker")

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} Basic Attack Damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.health}
{hero_mage1.dmg_type}
{hero_mage1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health}
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

{hero_jungle1.name}
{hero_jungle1.role}
{hero_jungle1.health}
{hero_jungle1.auto_atk_dmg}
{hero_jungle1.dmg_type}
{hero_jungle1.describe()}

{hero_tank1.name}
{hero_tank1.role}
{hero_tank1.health}
{hero_tank1.auto_atk_dmg}
{hero_tank1.dmg_type}
{hero_tank1.describe()}
''')

