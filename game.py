"""
Chapitre 11.4

Fonctions pour simuler un combat.
"""

import random

import utils
from character import *
from magician import *


"""Interactif avec 1 utilisateur. 

Choisir le perso? Pas besoin d'avance, peux le faire plus tard.

Commandes:
	Tous les personnages:
		X Attaquer
		X Passer notre tour
	Warrior:
		Position aggressive
		Position défensive
		Position normale
	Magician:
		Utilise magie/arme
		
"Commande" == texte
Action == méthode
entrer nom d'une command -> exécuter une méthode
"""

def deal_damage(attacker, defender):
	damage, crit = attacker.compute_damage(defender)
	# TODO: Obtenir l'arme utilisée par l'attaquant.
	#       Si aucune arme n'a été utilisée (last_move_used est None), on affiche "nothing"
	weapon_used = attacker.last_move_used.name if attacker.last_move_used is not None else "nothing"
	defender.take_damage(damage)
	print(f"  {attacker.name} used {weapon_used}")
	if crit:
		print("    Critical hit!")
	print(f"    {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	is_player_turn = True
	attacker = c1
	defender = c2
	turns = 1
	print(f"{attacker.name} would like to battle.")
	print(f"{defender.name} accepted!")
	available_commands = [cmd_name for cmd_name in attacker.know_commands.keys()]
	print(f"Available commands: {available_commands}")

	while True:
		if is_player_turn: # C'est le joueur
			while True:
				cmd_name = input("Choose your move: ")
				if cmd_name in attacker.know_commands:
					attacker.know_commands[cmd_name](defender)
					break
				else:
					print("Unknown cmd.")
		else: # C'est le NPC
			#deal_damage(attacker, defender)
			attacker.do_attack(defender)
		if defender.hp == 0:
			print(f"  {defender.name } is sleeping with the fishes.")
			break
		turns += 1
		attacker, defender = defender, attacker
		is_player_turn = not is_player_turn
	return turns
