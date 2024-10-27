import unittest
from guild import Guild
from rogue import Rogue
from warrior import Warrior
from wizard import Wizard

class testPlayableCharacters(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.guild = Guild("La Guilde", 10)
    self.rogue = Rogue("Bernard", 100, self.guild)
    self.warrior = Warrior("Titouan", 85, self.guild)
    self.wizard = Wizard("Philémon", 1_000_000, self.guild)

  def test_playable_character_can_die(self):
    self.warrior.health.points = 0
    self.assertFalse(self.warrior.is_alive(), "Your character is not dead even though they should be.")

  # Nécessite la méthode take_coins pour fonctionner
  def test_loot_dead_character(self):
    self.warrior.health.points = 0
    self.wizard.loot_dead_character(self.warrior)
    self.assertEqual(self.warrior.gold, 0, "You have not looted precisely all the opponent's gold.")
    self.assertEqual(self.wizard.gold, 1_000_085, "You have not looted precisely all the opponent's gold.")

  def test_drink_health_potion(self):
    self.rogue.health.points = 20
    self.rogue.drink_health_potion()
    self.assertEqual(self.rogue.health.points, 70, "The health potion is malfunctioning.")

    self.rogue.health.points = 80
    self.rogue.drink_health_potion()
    self.assertEqual(self.rogue.health.points, 100, "The health potion is malfunctioning.")

class testWizards(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.guild = Guild("La Guilde", 10)
    self.wizard = Wizard("Philémon", 1_000_000, self.guild)
    self.warrior = Warrior("Titouan", 85, self.guild)

  def test_is_instance_of_wizard(self):
    self.assertIsInstance(self.wizard, Wizard, "This is not an instance of Wizard")

  def test_init_wizard(self):
    self.wizard_temp = Wizard("Jako", 50, self.guild)
    self.assertEqual(self.wizard_temp.mana.points, 50)
    self.assertEqual(self.wizard_temp.name, "Jako")
    self.assertEqual(self.wizard_temp.attack_power, 60)
    self.assertEqual(self.wizard_temp.gold, 50)
    self.assertEqual(self.wizard_temp.guild, self.guild)


  def test_wizard_attack(self):
    self.wizard.attack(self.warrior)

    self.assertTrue(True if(self.warrior.health.points == 100 or self.warrior.health.points == 100 - self.wizard.attack_power) else False)
    self.assertEqual(self.wizard.mana.points, 0)

class testWarriors(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.guild = Guild("La Guilde", 10)
    self.warrior = Warrior("Titouan", 85, self.guild)
    self.wizard = Wizard("Philémon", 1_000_000, self.guild)

  def test_is_instance_of_warrior(self):
    self.assertIsInstance(self.warrior, Warrior, "This is not an instance of Warrior")

  def test_init_warrior(self):
    self.warrior_temp = Warrior("Justine", 150, self.guild)
    self.assertEqual(self.warrior_temp.rage.points, 50)
    self.assertEqual(self.warrior_temp.name, "Justine")
    self.assertEqual(self.warrior_temp.attack_power, 40)
    self.assertEqual(self.warrior_temp.gold, 150)
    self.assertEqual(self.warrior_temp.guild, self.guild)

  def test_warrior_attack(self):
    self.warrior.attack(self.wizard)

    self.assertTrue(True if(self.wizard.health.points == 100 or self.wizard.health.points == 100 - self.warrior.attack_power) else False)
    self.assertEqual(self.warrior.rage.points, 25)

class testRogues(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.guild = Guild("La Guilde", 10)
    self.rogue = Rogue("Bernard", 100, self.guild)
    self.wizard = Wizard("Philémon", 1_000_000, self.guild)
    self.warrior = Warrior("Titouan", 85, self.guild)

  def test_is_instance_of_rogue(self):
    self.assertIsInstance(self.rogue, Rogue, "This is not an instance of Rogue")

  def test_init_rogue(self):
    self.rogue_temp = Rogue("Raton", 0, self.guild)
    self.assertEqual(self.rogue_temp.name, "Raton")
    self.assertEqual(self.rogue_temp.attack_power, 110)
    self.assertEqual(self.rogue_temp.gold, 0)
    self.assertEqual(self.rogue_temp.guild, self.guild)

  def test_rogue_attack(self):
    self.rogue.attack(self.wizard)

    self.assertTrue(True if(self.wizard.health.points == 100 or self.wizard.health.points == 0) else False)
    
  def test_greet(self):
    self.rogue.greet(self.warrior)
    self.assertEqual(self.rogue.gold, 101)
    self.assertEqual(self.warrior.gold, 84)

if __name__ == '__main__':
    unittest.main()