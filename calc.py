import math
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')

args = parser.parse_args()

Hp = args.integers[0]
Atk = args.integers[1]
Def = args.integers[2]
SpA = args.integers[3]
SpD = args.integers[4]
Speed = args.integers[5]

AtkIV = args.integers[6]
DefIV = args.integers[7]
StaIV = args.integers[8]

PkmnLvl = args.integers[9]

GoHp = 2 * Hp

PA = ( 2*( max( (Atk),(SpA) )*(7/8)+min( (Atk),(SpA) )*(1/8) ) )
GoAtk = round( (PA*0.85)+(PA*Speed/500) )

PD = ( 2*( max( (Def),(SpD) )*(7/8)+min( (Def),(SpD) )*(1/8) ) )
GoDef = round( (PD*0.85)+(PD*Speed/500) )

lvl_const = 0.7903

AtkFactor = GoAtk + AtkIV
DefFactor = ( GoDef + DefIV ) ** 0.5
HpFactor = ( GoHp + StaIV ) ** 0.5
CP = ( AtkFactor * DefFactor * HpFactor ) * ( lvl_const ** 2 ) / 10

print CP
