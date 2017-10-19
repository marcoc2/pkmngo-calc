# -*- coding: utf-8 -*-

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pokemon', help='Name of the Pokémon to calculate CP')
parser.add_argument('level', type=int, help='Level of the Pokémon')
parser.add_argument('atk_iv', type=int, help='Attack IV')
parser.add_argument('def_iv', type=int, help='Defense IV')
parser.add_argument('sta_iv', type=int, help='Status IV')

pokemons = {}

# #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
with open('dataset/pokemon.csv', 'rb') as csvfile:
    pokemon_database = csv.DictReader(csvfile)
    for entry in pokemon_database:
        pokemons[entry['Name']] = {'hp': entry['HP'],
                                   'atk': entry['Attack'],
                                   'def': entry['Defense'],
                                   'spatk': entry['Sp. Atk'],
                                   'spdef': entry['Sp. Def'],
                                   'speed': entry['Speed']
                                  }
    print "Pokémons read from CSV: {0}".format(str(len(pokemons)))

args = parser.parse_args()
pokemon = args.pokemon

Hp = pokemons[pokemon]['hp']
Atk = pokemons[pokemon]['atk']
Def = pokemons[pokemon]['def']
SpA = pokemons[pokemon]['spatk']
SpD = pokemons[pokemon]['spdef']
Speed = pokemons[pokemon]['speed']

AtkIV = args.atk_iv
DefIV = args.def_iv
StaIV = args.sta_iv

PkmnLvl = args.level

GoHp = 2 * Hp

PA = (2 * (max(Atk, SpA) * (7/8.0) + min(Atk, SpA) * (1/8.0)))
GoAtk = round((PA * 0.85) + (PA * Speed/500.0))

PD = (2 * (max(Def, SpD)*(7/8.0) + min(Def, SpD) * (1/8.0)))
GoDef = round((PD * 0.85) + (PD * Speed/500.0))

lvl_const = 0.7903

AtkFactor = GoAtk + AtkIV
DefFactor = (GoDef + DefIV) ** 0.5
HpFactor = (GoHp + StaIV) ** 0.5
CP = (AtkFactor * DefFactor * HpFactor) * (lvl_const ** 2) / 10.0

print CP
