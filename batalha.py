import json

# This will give us a base template for each class until we import characters
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

# Guerreiro has a special ability to heal himself
class Guerreiro(Personagem):
    def especial(self):
        self.vida += 25
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")

class Mago(Personagem):
    pass

class Arqueiro(Personagem):
    pass

# We will import the character using this to use later
def importar_personagens(caminho):
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    with open(caminho, 'r') as file:
        data = json.load(file)
    
    personagens = []
    for item in data:
        if item['classe'] == 'Guerreiro':
            personagens.append(Guerreiro(item['nome'], item['vida'], item['ataque']))
        elif item['classe'] == 'Mago':
            personagens.append(Mago(item['nome'], item['vida'], item['ataque']))
        elif item['classe'] == 'Arqueiro':
            personagens.append(Arqueiro(item['nome'], item['vida'], item['ataque']))
    
    return personagens, len(personagens)

# After we import the character, this will be called to sort them by life
def ordenar_personagens_por_vida(personagens):
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    return sorted(personagens, key=lambda p: p.vida)

# This will import the character from thhe "personagens.json" file
personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

# This will then sort them by life
personagens = ordenar_personagens_por_vida(personagens)

# This will show all the characters that were imported
print(personagens[0])
print(personagens[1])
print(personagens[2])

# Sequence of combat
personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])