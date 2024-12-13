import json

class HOA:
    households = {}
    monthly_cost_per_household = 0
    
    def __init__(self, monthly_cost_per_household):
        self.monthly_cost_per_household = monthly_cost_per_household

    def add_household(self, num_members, terrain_area, monthly_cost):
        id = len(self.households.keys()) + 1
        self.households[id] = Household(id, num_members, terrain_area, monthly_cost)
    
    def get_household(self, id):
        return self.households[id]
    
    def remove_household(self, id):
        self.households[id] = None
    
    def get_monthly_revenue(self):
        revenue = 0
        for household in self.households.values():
            if household != None:
                revenue += household.monthly_cost - self.monthly_cost_per_household
        return revenue
    
    def __str__(self):
        lines = ""
        for household in self.households.values():
            if household != None:
                lines += str(household) + "\n"
            else:
                lines += "-\t-\t-\t-\n"
        return lines
    
    def save_json(self, path):
        households_dict = {k: v.to_dict() for k, v in self.households.items() if v is not None}
        with open(path, 'w') as json_file:
            json.dump(households_dict, json_file, indent=4)
                    
                    
class Household:
    id = 0
    num_members = 0
    terrain_area  = 0 
    monthly_cost = 0
    
    def __init__(self, id, num_members, terrain_area, monthly_cost):
        self.id = id
        self.num_members = num_members
        self.terrain_area = terrain_area
        self.monthly_cost = monthly_cost
    
    def __str__(self):
        return f"{self.id} {self.num_members} {self.terrain_area} {self.monthly_cost}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'num_members': self.num_members,
            'terrain_area': self.terrain_area,
            'monthly_cost': self.monthly_cost
        }

                   
hoa = HOA(10)

hoa.add_household(2, 100, 50)
hoa.add_household(4, 250, 150)
hoa.add_household(1, 50, 25)

hoa.remove_household(2)

hoa.save_json('info.json')

print(hoa)