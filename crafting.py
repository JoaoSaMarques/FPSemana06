import random

class Recipe:

    items = []
    result = None
    
    def __init__(self, items, result):
        self.items = items
        self.result = result
    
    def __str__(self):
        rec = ""
        for item in self.items:
            rec += f"{item.name}({item.id}) + "
        return f"{rec[:-3]} = {self.result.name}({self.result.id})"
    
    def craft(self):
        return self.result
        
class Item: 
    id = 0
    name = ""
    
    def __init__(self, name):
        self.id = self.ID().generate()
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
    class ID:
        
        def __init__(self):
            pass
        
        def generate(self):
            return random.randint(0, 100000000)
            
class EchantedItem(Item):
    enchantment = ""
    
    def __init__(self, name, enchantment):
        super().__init__(name)
        self.enchantment = enchantment        
          
class Storage:
    storage = {}
    
    def __init__(self):
        pass
    
    def add_items(self, items):
        for item in items:
            self.storage[item.name] = item
    
    def get(self, name):
        return self.storage[name]
          
    def add_item(self, item):
        self.storage[item.name] = item
        
    def del_item(self, item):
        self.storage.pop(item.name)
    
    def __str__(self):
        dic = "STORAGE\n"
        for item in self.storage.values():
            dic += f"{item.name}\t{item.id}\n"
        return dic
        
chest = Storage()
chest.add_items([Item("Iron"), 
                Item("Wood"), 
                Item("Iron Sword"), 
                Item("Lapis")])
print(chest)

iron_sword_recipe = Recipe(
    [chest.get("Iron"), chest.get("Iron")], 
    Item("Iron Sword")
    )
print(iron_sword_recipe)
chest.add_item(iron_sword_recipe.craft())

enchanted_iron_sword_recipe = Recipe(
    [chest.get("Iron"), chest.get("Wood"), chest.get("Lapis")], 
    EchantedItem("Enchanted Iron Sword", "Silk Touch")
    )
print(enchanted_iron_sword_recipe, "\n")
chest.add_item(enchanted_iron_sword_recipe.craft())

print(chest)