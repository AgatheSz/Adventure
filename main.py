from npc import Npc
from rogue import Rogue
from wizard import Wizard
from warrior import Warrior
from guild import Guild

guild = Guild("La Guilde", 10)
rogue = Rogue("Bernard", 100, guild)
wizard = Wizard("Philémon", 1_000_000, guild)
warrior = Warrior("Titouan", 85, guild)
npc = Npc("Jeannette", 1, "villager")


rogue.interact_with_npc(npc)

warrior.attack(rogue)
warrior.attack(rogue)
warrior.drink_potion()
rogue.attack(warrior)
rogue.greet(wizard)