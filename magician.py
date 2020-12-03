"""
Chapitre 11.4

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *
from spellcaster import *
from weapon_user import *


class Magician(WeaponUser, Spellcaster):
	# MRO: Mag -> WP -> SC -> Ch
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.using_magic = False
		self.known_commands.update({
			"magic": self.do_magic,
			"physical": self.do_physical
		})

	# TODO: Surcharger la méthode `compute_damage`
	def compute_damage(self, other):
		# Si on veut et peut utiliser de la magie (`will_use_spell()`):
		if self.will_use_spell():
			# TODO: Utiliser le `compute_damage` de `Spellcaster`
			return Spellcaster.compute_damage(self, other)
		# Sinon
		else:
			# TODO: Utiliser le `compute_damage` de `WeaponUser`
			return WeaponUser.compute_damage(self, other)

	def will_use_spell(self):
		return self.using_magic and self.can_use_spell()

	def do_magic(self, defender):
		self.using_magic = True
		self.do_attack(defender)

	def do_physical(self, defender):
		self.using_magic = False
		self.do_attack(defender)
